#!/usr/bin/python3
from random import randint
import matplotlib.pyplot as plt
from matplotlib import colors
import numpy as np
from Tetromino import Tetromino

class ObstacleField:
    'Common Obstacle Field object. Creates a field of randomly distributed Tetrominoes '

    dim = [0, 0]
    fieldSize = 0
    cov = 0
    field = []
    obsColor = ''
    spaceColor = ''
    obsGenerator = Tetromino()
    # obsScale = 1.0
    # showTicks = false


    def __init__(self, dimensionList=[128, 128], coverageRate=0.2):
        self.dim = dimensionList
        self.cov = coverageRate
        self.field = np.zeros((self.dim[0], self.dim[1]), np.int8)
        self.fieldSize = dimensionList[0] * dimensionList[1]

        self.__generateGrid()

    def showField(self, ax):
        # display the grid with obstacles

        # print(self.field)
        ax.imshow(self.field.T, cmap='Greys', interpolation='nearest', extent=None)
        return ax

    def getDim(self):
        # return self.field
        return self.dim

    def setDim(self, newDim):
        self.dim = newDim

    def getCov(self):
        return self.cov

    def setCov(self, newCov):
        self.cov = newCov

    def __randomLocation(self):
        # generate random location for a tetromino

        num = randint(0, self.fieldSize - 1)
        row = num // self.dim[1]
        col = num % self.dim[1]
        loc = np.array([row, col])

        return loc

    def __randomRotation(self, tet):
        # randomly rotate tetromino

        return tet

    def __placeObstacle(self, obs, loc):
        # add the obstacle to the field
        rowStart = loc[0]
        rowEnd = loc[0] + obs.shape[0]
        colStart = loc[1]
        colEnd = loc[1] + obs.shape[1]

        # If obstacle overlaps with edge of field
        if rowEnd >= self.dim[0] + 1:
            rowEnd = self.dim[0] + 1
            cutLoc = self.dim[0] - loc[0]
            obs = obs[0:cutLoc, :]

        if colEnd >= self.dim[1] + 1:
            colEnd = self.dim[1] + 1
            cutLoc = self.dim[1] - loc[1]
            obs = obs[:, 0:cutLoc]

        # If set cells at location equal to obstacle
        if colStart == colEnd:
            self.field[rowStart:rowEnd, colStart] = obs
        elif rowStart == rowEnd:
            self.field[rowStart, colStart:colEnd] = obs
        else:
            self.field[rowStart:rowEnd, colStart:colEnd] = obs

    def __generateGrid(self):
        # generate the grid from here

        numObs = 0
        curCov = 0

        while curCov < self.cov:

            obs = self.obsGenerator.getRandom()
            # obs = self.__randomRotation(obs)
            loc = self.__randomLocation()
            self.__placeObstacle(obs, loc)

            numObs = np.sum(self.field)
            curCov = numObs / self.fieldSize