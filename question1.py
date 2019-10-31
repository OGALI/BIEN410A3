import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import ndimage
from sklearn.metrics.pairwise import euclidean_distances
import time
import concurrent.futures


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
        return np.mean(euclidean_distances(self.positions,[[0,0]]))


    def centroid(self):
        return ndimage.measurements.center_of_mass(self.positions)


    def printer(self):
        print(self.positions)


if __name__ == "__main__":
    nWalks = 1000
    nPoints = 1000
    distributionLastPoint = np.zeros(nWalks)
    distributionAverageDist = np.zeros(nWalks)


    def singleWalkObject(start, nPoints):
        walker = RandomWalk((0,0), nPoints)
        walker.fullWalk()
        return (walker.EuclidianDistanceLast(), walker.averageEuclidianDistance(start=walker.centroid()))


    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(singleWalkObject,(0,0),nPoints) for i in range(nWalks)]
        distributionLastPoint = [results[i].result()[0] for i in range(nWalks)]
        distributionAverageDist = [results[i].result()[1] for i in range(nWalks)]
    end = time.perf_counter()
    print(f'time {end-start}')



    f, axes = plt.subplots(2, 1)
    sns.distplot(distributionLastPoint, bins=20, kde=False, rug=True, ax=axes[0]);
    sns.distplot(distributionAverageDist, bins=20, kde=False, rug=True, ax=axes[1]);
    axes[0].set_title('Distribution of Euclidian Distances of the Last Point')
    axes[1].set_title('Distribution of Average Euclidian Distances')
    axes[0].set(xlabel='Distance', ylabel='# of times')
    axes[1].set(xlabel='Distance', ylabel='# of times')
    plt.tight_layout()
    plt.savefig('question1.jpg',dpi=500)
    plt.show()

    print(f'Distribution of Euclidian Distances of the Last Point Mean: {np.mean(distributionLastPoint)}')
    print(f'Distribution of Euclidian Distances of the Last Point STD: {np.std(distributionLastPoint)}')
    print(f'Distribution of Euclidian Distances of the Last Point median: {np.median(distributionLastPoint)}')

    print(f'Distribution of Average Euclidian Distance Mean: {np.mean(distributionAverageDist)}')
    print(f'Distribution of Average Euclidian Distance STD: {np.std(distributionAverageDist)}')
    print(f'Distribution of Average Euclidian Distance median: {np.median(distributionAverageDist)}')
