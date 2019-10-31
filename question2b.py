import random
import numpy as np
from question1 import RandomWalk
import seaborn as sns
import matplotlib.pyplot as plt


class RandomWalkSefAvoid(RandomWalk):
    def __init__(self, start, Nsteps):
        super().__init__(start, Nsteps)


    def fullWalk(self):
        for currentStep in range(1, self.Nsteps):
            flag = 0
            while self.nextStep(currentStep) == 0:
                self.nextStep(currentStep)
                flag = 1
        return flag


    def nextStep(self, currentStep):
        nextStep = random.choice(self.step)
        previousX, previousY = self.positions[currentStep-1,]
        if nextStep == 'up':
            newX, newY = previousX, previousY + 1
        if nextStep == 'down':
            newX, newY = previousX, previousY - 1
        if nextStep == 'right':
            newX, newY = previousX + 1, previousY
        if nextStep == 'left':
            newX, newY = previousX - 1, previousY

        for i in range(self.Nsteps):
            if newX == self.positions[i,0] and newY == self.positions[i,1]:
                return 1

        self.positions[currentStep,] = (newX, newY)
        return 0



if __name__ == "__main__":

    nWalks = 40000
    nPoints = 14
    distributionLastPoint = np.zeros(nWalks)
    distributionAverageDist = np.zeros(nWalks)
    fraction = np.zeros(nWalks)
    for i in range(nWalks):
        walker = RandomWalkSefAvoid((0, 0), nPoints)
        fraction[i] = walker.fullWalk()
        distributionLastPoint[i] = walker.averageEuclidianDistance(walker.centroid())
        distributionAverageDist[i] = walker.averageEuclidianDistance()

    f, axes = plt.subplots(4, 1)
    sns.distplot(distributionLastPoint, bins=10, kde=False, rug=True, ax=axes[0])
    sns.distplot(distributionAverageDist, bins=10, kde=False, rug=True, ax=axes[1])
    sns.distplot(distributionLastPoint[fraction==1], bins=10, kde=False, rug=True, ax=axes[2])
    sns.distplot(distributionAverageDist[fraction==1], bins=10, kde=False, rug=True, ax=axes[3])
    axes[0].set_title('Distribution of Euclidian Distances \n to the Last Point to the Origin', fontsize=20)
    axes[1].set_title('Distribution of Average Euclindean Distance to the Centroid', fontsize=20)
    axes[2].set_title('Distribution of Euclidian Distances \n to the Last Point to the Origin for Self-Avoiding Walks', fontsize=20)
    axes[3].set_title('Distribution of Average Euclidian Distance \n to the Last point to the origin for Self-Avoiding Walks', fontsize=20)
    axes[0].set(xlabel='Distance', ylabel='# of times')
    axes[1].set(xlabel='Distance', ylabel='# of times')
    axes[2].set(xlabel='Distance', ylabel='# of times')
    axes[3].set(xlabel='Distance', ylabel='# of times')
    f.set_size_inches(12, 15)
    plt.tight_layout()
    plt.savefig('question2b.jpg', dpi=500)
    plt.show()
    print('Fraction of stuff', np.sum(fraction) / 40000)