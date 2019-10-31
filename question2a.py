import random
import numpy as np
from question1 import RandomWalk
import seaborn as sns
import matplotlib.pyplot as plt

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
    sns.distplot(distributionLastPoint[distributionLastPoint != 0], bins=20, kde=False, rug=True, ax=axes[1]);
    sns.distplot(distributionAverageDist[distributionAverageDist != 0], bins=20, kde=False, rug=True, ax=axes[2]);
    axes[0].set_title('Distribution of Walk Lengths for 2000 Walks with Sticky Walls', fontsize=20)
    axes[1].set_title('Distribution of Euclindean Distance for Non Sticky fraction', fontsize=20)
    axes[2].set_title('Distribution of Average Distances \n to the Centroid for 2000 walks for Non-Sticky Fraction', fontsize=20)
    axes[0].set(xlabel='Distance', ylabel='# of times')
    axes[1].set(xlabel='Distance', ylabel='# of times')
    axes[2].set(xlabel='Distance', ylabel='# of times')

    f.set_size_inches(12, 15)
    plt.tight_layout()
    plt.savefig('question2a.jpg', dpi=500)
    plt.show()

    # Check fraction above 1000
    distributionLengthFraction = distributionLength
    distributionLengthFraction[distributionLengthFraction<999] = 0
    distributionLengthFraction[distributionLengthFraction==999] = 1
    print('Fraction of non sticky: ', np.sum(distributionLengthFraction)/2000)
    print('average from centroid:', walker.averageEuclidianDistance(walker.centroid()))