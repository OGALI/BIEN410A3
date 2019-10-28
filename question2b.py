import random
import numpy as np
from question1 import RandomWalk
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats


class RandomWalkSefAvoid(RandomWalk):
    def __init__(self, start, Nsteps):
        super().__init__(start, Nsteps)


    def fullWalk(self):
        for currentStep in range(1, self.Nsteps):
            while self.nextStep(currentStep) == 0:
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

        for i in range(self.Nsteps):
            if newX == self.positions[i,0] and newY == self.positions[i,1]:
                return 0

        self.positions[currentStep,] = (newX, newY)
        return 1



if __name__ == "__main__":
    walker = RandomWalkSefAvoid((0,0), 14)
    walker.fullWalk()
    walker.printer()