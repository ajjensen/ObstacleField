#!/usr/bin/python3
import numpy as np
from Node import Node
import copy

class Graph:
    # This is a graph object which is defined by an adjacency list
    # 
    #   map         -   Array that represents the obstacle field. Empty = 0; Occupied = 1
    #   mapSize     -   Shape of the map object
    #   adj         -   Array of node objects. Node.id variables represent the index of 
    #                   the node in adj.
    #   neighbors   -   A dictinary containing the difference in indices for a cell and 
    #                   its neighboring cells
    #
    # map indices <--> adj indices Math:
    #  

    neighbors = {'topleft' : [-1, -1], \
        'top' : [-1, 0], \
        'topright' : [-1, 1], \
        'right' : [0, 1], \
        'bottomright' : [1, 1], \
        'bottom' : [1, 0], \
        'bottomleft' : [1, -1], \
        'left': [-1, 0]}

    def __init__(self, mapIn = np.zeros((128, 128), np.int8)):
        self.map = mapIn
        self.mapSize = np.shape(mapIn)
        self.adj = self.__createAdjList()

    def addNode(self, newNode):
        # Add a node to the graph

        pass

    def setMap(self):
        # set the map of the graph if not already set in constructor
        pass

    def __mapInd2AdjInd(self, mapInd):
        r = mapInd[0]
        c = mapInd[1]

        adjInd = r * self.mapSize[1] + c
        return adjInd

    def __adjInd2MapInd(self, adjInd):
        mapInd = adjInd
        return mapInd

    # Get all edges for the index
    def __getEdges(self, ind):
        R = ind[0]
        C = ind[1]
        curNeighbors = copy.deepcopy(self.neighbors)

        if R == 0:
            curNeighbors.pop('topleft', None)
            curNeighbors.pop('top', None)
            curNeighbors.pop('topright', None)
        elif R == self.mapSize[0] - 1:
            curNeighbors.pop('bottomleft', None)
            curNeighbors.pop('bottom', None)
            curNeighbors.pop('bottomright', None)
        if C == 0:
            curNeighbors.pop('topleft', None)
            curNeighbors.pop('left', None)
            curNeighbors.pop('bottomleft', None)
        elif C == self.mapSize[1] - 1:
            curNeighbors.pop('topright', None)
            curNeighbors.pop('right', None)
            curNeighbors.pop('bottomright', None)
        
        edges = np.empty(0, int)

        for key in curNeighbors:
            dif = curNeighbors[key]
            r = R + dif[0]
            c = C + dif[1]

            if self.map[r,c] != 1:
                adjInd = self.__mapInd2AdjInd([r,c])
                edges = np.append(edges, [adjInd], axis=0)

        return edges

    def __createAdjList(self):
        adj = np.empty(0, Node)
        it = np.nditer(self.map, flags = ['multi_index'])

        for i in it:
            if i == 0:
                adjInd = self.__mapInd2AdjInd(it.multi_index)
                curNode = Node(adjInd)
                edges = self.__getEdges(it.multi_index)
                curNode.addConnection(edges)
            
                adj = np.append(adj, [curNode], axis=0)

        return adj