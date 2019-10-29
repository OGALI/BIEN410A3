import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import ndimage


class RandomWalk:
    step = ['up', 'down', 'right', 'left']


    def __init__(self, start, Nsteps):
        self.Nsteps = Nsteps
        self.positions = np.zeros((self.Nsteps, 2), dtype=int)
        self.positions[0,] = start


    def fullWalk(self):
        for currentStep in range(1, self.Nsteps):
            self.nextStep(currentStep)


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
        self.positions[currentStep,] = (newX, newY)


    def EuclidianDistanceLast(self, start=(0,0)):
        return np.linalg.norm(start - self.positions[self.Nsteps -1,])


    def averageEuclidianDistance(self, start=(0,0)):
        return np.mean(np.linalg.norm(self.positions- [0,0]))


    def centroid(self):
        return ndimage.measurements.center_of_mass(self.positions)


    def printer(self):
        print(self.positions)


if __name__ == "__main__":
    distributionLastPoint = np.zeros(1000)
    distributionAverageDist = np.zeros(1000)
    for i in range(1000):
        walker = RandomWalk((0,0), 1000)
        walker.fullWalk()
        distributionLastPoint[i] = walker.EuclidianDistanceLast()
        distributionAverageDist[i] = walker.averageEuclidianDistance(start=walker.centroid())


    f, axes = plt.subplots(2, 1)
    # f.title('Main title')
    sns.distplot(distributionLastPoint, bins=20, kde=False, rug=True, ax=axes[0]);
    axes[0].set_title('Distribution of Euclidian Distances of the Last Point')
    axes[1].set_title('Distribution of Average Euclidian Distances')

    axes[0].set(xlabel='Distance', ylabel='# of times')
    axes[1].set(xlabel='Distance', ylabel='# of times')

    sns.distplot(distributionAverageDist, bins=20, kde=False, rug=True, ax=axes[1]);
    plt.show()

