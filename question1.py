import random
import numpy as np
import matplotlib.pyplot as plt

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
        # index = random.randint(low=0,high=3)
        # nextStep = self.step[index]
        previousX, previousY = self.positions[currentStep-1,]
        if nextStep == 'up':
            newX, newY = previousX, previousY + 1
        elif nextStep == 'down':
            newX, newY = previousX, previousY - 1
        elif nextStep == 'right':
            newX, newY = previousX + 1, previousY
        elif nextStep == 'left':
            newX, newY = previousX - 1, previousY +1
        self.positions[currentStep,] = (newX, newY)

    def EuclidianDistance(self):
        dist = np.linalg.norm(self.positions[0,]- self.positions[self.Nsteps -1,])
        return dist

    def averageEuclidianDistance(self):
        meanDist = np.linalg.norm(self.positions[0,] - self.positions)
        return meanDist/self.Nsteps

    def printer(self):
        print(self.positions)

walker = RandomWalk((0,0), 1000)
walker.fullWalk()
# walker.printer()
print(walker.EuclidianDistance())
print(walker.averageEuclidianDistance())