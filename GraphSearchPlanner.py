#!/usr/bin/python3
from ObstacleField import ObstacleField
import matplotlib as plt
import numpy as np
from Graph import Graph
from matplotlib import colors
from Route import Route
from queue import Queue as q

class GraphSearchPlanner:
    # TODO:
    #   - set start
    #   - set goal
    #   - plot
    #   - functionality to watch at every step
    #   - planners
    #   - store path
    #   - record number of iterations
    #   - record time
    #   - color path

    def __init__(self, obsFieldIn = ObstacleField()):
        self.obsField = obsFieldIn
        self.graph = Graph(self.obsField.field)
        self.start = self.setStart()
        self.goal = self.setGoal()
        self.maxIterations = 1e6
        self.Dijkstra = Route()
        self.DepthFirst = Route()
        self.BreadthFirst = Route()
        self.Random = Route()

    def plot(self, ax, showObstacles = True, showGraph = False):
        pass

    def planBreadthFirst(self):
        pass

    def planDepthFirst(self):
        pass

    def planDijkstra(self):
        pass

    def planRandom(self):
        pass

    def setGoal(self):
        pass

    def setStart(self):
        pass
