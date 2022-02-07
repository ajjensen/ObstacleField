#!/usr/bin/python3
from ObstacleField import ObstacleField
import matplotlib.pyplot as plt
import numpy as np
from Graph import Graph
from matplotlib import colors
from Route import Route
from queue import Queue

class GraphSearchPlanner:
    # TODO:
    #   x set start
    #   x set goal
    #   - plot
    #   - functionality to watch at every step
    #   - planners
    #   - store path
    #   - record number of iterations
    #   - record time
    #   - color path

    def __init__(self, obsFieldIn = ObstacleField()):
        self.obsFieldObj = obsFieldIn
        self.map = obsFieldIn.field
        self.graphObj = Graph(self.obsFieldObj.field)
        self.graph = self.graphObj.adj
        self.start = self.setStart()
        self.goal = self.setGoal()
        self.maxIterations = 1e6
        self.DijkstraSol = Route()
        self.DepthFirstSol = Route()
        self.BreadthFirstSol = Route()
        self.RandomSol = Route()

    def plotStart(self, ax):
        ax.plot(self.start[0], self.start[1], 'o', markersize=3, color="r", linewidth=3)

    def plotGoal(self, ax):
        ax.plot(self.goal[0], self.goal[1], 'o', markersize=3, color="b", linewidth=3)

    def plotPath(self, ax):
        curNode = self.BreadthFirstSol.get()

        while not self.BreadthFirstSol.empty():
            nextNode = self.BreadthFirstSol.get()
            ax.plot([curNode[0], nextNode[0]], [curNode[1], nextNode[1]], 'o', markersize=3, color="g", linewidth=3)


    def planBreadthFirst(self, update=False, ax=None):
        Q = Queue()
        Q.put(self.start)
        self.graph[self.start].setState_Alive()
        realTime = self.map
        if ax == None:
            fig, ax = plt.subplots()
        
        ax.imshow(realTime.T, cmap='Greys', interpolation='nearest', extent=None)
        self.plotStart(ax)
        self.plotGoal(ax)

        while not Q.empty():
            ind = Q.get()
            # print('pop: ', ind)
            curNode = self.graph[ind]

            if curNode.id == self.goal:
                self.BreadthFirstSol = Q
                self.plotPath(ax)
                return True
            
            for edge in curNode.edges:

                if self.graph[edge].isUnvisited():
                    if update:
                        ax.plot([curNode.id[0], edge[0]], [curNode.id[1], edge[1]], '.-', markersize=2, color='xkcd:grey', linewidth=1)
                        plt.pause(0.01)

                    self.graph[edge].setState_Alive()
                    Q.put(edge)
                    # print('insert: ', edge)
        
        self.BreadthFirstSol = Q
        return False




    def planDepthFirst(self):
        pass

    def planDijkstra(self):
        pass

    def planRandom(self):
        pass

    def setGoal(self):
        open = np.where(self.map == 0)
        x = open[0]
        y = open[1]
        last = len(x)

        goal = (x[last-1], y[last-1])
        return goal

    def setStart(self):
        open = np.where(self.map == 0)
        x = open[0]
        y = open[1]

        start = (x[0], y[0])
        return start
