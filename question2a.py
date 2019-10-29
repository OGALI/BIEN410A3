import random
import numpy as np
from question1 import RandomWalk
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

class RandomWalkSticky(RandomWalk):
    step = ['up', 'down', 'right', 'left']


    def __init__(self, start, Nsteps):
        super().__init__(start, Nsteps)


    def fullWalk(self):
        averageDistance = 0
        ED = 0
        for currentStep in range(1, self.Nsteps):
            if(self.nextStep(currentStep) == 0):
                break
        if currentStep == 999:
            averageDistance = self.averageEuclidianDistance()
            ED = self.EuclidianDistanceLast()
        return currentStep, averageDistance, ED


    def nextStep(self, currentStep):
        nextStep = random.choice(self.step)
        # index = random.randint(low=0,high=3)
        # nextStep = self.step[index]
        previousX, previousY = self.positions[currentStep-1,]
        if nextStep == 'up':
            newX, newY = previousX, previousY + 1
        if nextStep == 'down':
            newX, newY = previousX, previousY - 1
        if nextStep == 'right':
            newX, newY = previousX + 1, previousY
        if nextStep == 'left':
            newX, newY = previousX - 1, previousY
        self.positions[currentStep,] = (newX, newY)
        if newY == 20 or newY == -20:
            return 0
        else:
            return 1


if __name__ == "__main__":
    # walker  = RandomWalkSticky((0,0), 1000)
    # walker.fullWalk()
    nWalks = 2000
    nPoints = 1000 #nsteps = npoints -1
    distributionLength = np.zeros(nWalks)

    distributionLastPoint = np.zeros(nWalks)
    distributionAverageDist = np.zeros(nWalks)

    for i in range(nWalks):
        walker = RandomWalkSticky((0, 0), nPoints)
        distributionLength[i], distributionLastPoint[i], distributionAverageDist[i] = walker.fullWalk()


    f, axes = plt.subplots(3, 1)
    sns.distplot(distributionLength, kde=False, rug=True, ax=axes[0]);

    print(distributionLength)
    # Check fraction above 1000
    distributionLengthFraction = distributionLength
    distributionLengthFraction[distributionLengthFraction<999] = 0
    distributionLengthFraction[distributionLengthFraction==999] = 1
    print(len(distributionLengthFraction))
    print(np.sum(distributionLengthFraction)/2000)


    sns.distplot(distributionLastPoint[distributionLastPoint != 0], bins=20, kde=False, rug=True, ax=axes[1]);
    sns.distplot(distributionAverageDist[distributionAverageDist != 0], bins=20, kde=False, rug=True, ax=axes[2]);
    plt.show()

    print('average to centroid:', walker.averageEuclidianDistance(walker.centroid()))