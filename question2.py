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
        for currentStep in range(1, self.Nsteps):
            if(self.nextStep(currentStep) == 0):
                break
        # print(currentStep-1)
        return currentStep


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
    nSteps = 1000
    distributionLength = np.zeros(nWalks)
    for i in range(nWalks):
        walker = RandomWalkSticky((0, 0), nSteps)
        distributionLength[i] = walker.fullWalk()


    # f.title('Main title')
    sns.distplot(distributionLength, kde=False);
    # axes[0].set_title('Distribution of Number of Points')
    plt.title('Distributions of Number of Steps')
    plt.xlabel('# of steps')
    plt.show()

    print(distributionLength)
    # Check fraction above 1000
    distributionLengthFraction = distributionLength
    distributionLengthFraction[distributionLengthFraction<999] = 0
    distributionLengthFraction[distributionLengthFraction==999] = 1
    print(np.sum(distributionLengthFraction)/999)