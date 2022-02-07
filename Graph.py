#!/usr/bin/python3
import numpy as np
from Node import Node
import copy
import matplotlib.pyplot as plt
from matplotlib import colors

class Graph:
    # 
    # This is a graph object which is defined by an adjacency list
    # 
    #   map         -   Array that represents the obstacle field. Empty = 0; Occupied = 1
    #   mapSize     -   Shape of the map object
    #   adj         -   Dictionary of node objects. Key is tuple from map indices, value is Node object
    #   neighbors   -   A dictionary containing the difference in indices for a cell and 
    #                   its neighboring cells
    # 

    neighbors = {'bottomright' : [1, 1], \
        'right' : [0, 1], \
        'bottom' : [1, 0], \
        'topright' : [-1, 1], \
        'bottomleft' : [1, -1], \
        'top' : [-1, 0], \
        'left': [0, -1], \
        'topleft' : [-1, -1]}

    def __init__(self, mapIn = np.zeros((128, 128), np.int8)):
        self.map = mapIn
        self.mapSize = np.shape(mapIn)
        self.adj = {}
        self.__createAdjList()

    # Add a node to the graph
    def addNode(self, srcNodeInd, newNodeInd):
        if not srcNodeInd in self.adj:
            srcNode = Node(srcNodeInd)
            self.adj[srcNode.id] = srcNode
        if not newNodeInd in self.adj:
            newNode = Node(newNodeInd)
            self.adj[newNode.id] = newNode

        self.adj[srcNodeInd].addEdge(newNodeInd)
        self.adj[newNodeInd].addEdge(srcNodeInd)

    # set the map of the graph if not already set in constructor
    def setMap(self, mapIn):
        self.map = mapIn

    # TODO: update to work with new Node object and adjacency list. plot the graph
    def plotGraph(self, ax):

        for key in self.adj:
            curNode = self.adj[key]

            for edge in curNode.edges:
                curEdge = edge

                ax.plot([curNode.id[0], curEdge[0]], [curNode.id[1], curEdge[1]], '.-', markersize=1.5, color="black", linewidth=1)
                # plt.pause(0.01)
        return ax

    # Get all edges for the index
    def __getEdges(self, curNode):
        R = curNode[0]
        C = curNode[1]
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

        for key in curNeighbors:
            dif = curNeighbors[key]
            r = R + dif[0]
            c = C + dif[1]

            if (self.map[r,c] == 0):
                self.addNode((R,C), (r,c))

    # OBSOLETE: given indices (size 2) on the map, return a corresponding index in the adjacency list (size 1) 
    def __mapInd2AdjInd(self, mapInd):
        r = mapInd[0]
        c = mapInd[1]

        adjInd = r * self.mapSize[1] + c
        return adjInd
    
    # OBSOLETE
    def __adjInd2MapInd(self, adjInd):
        r = int(adjInd / self.mapSize[1])
        c = adjInd % self.mapSize[1]
        mapInd = np.array([r,c])
        return mapInd
    
    # Creates the adjacency list for the entire graph
    def __createAdjList(self):

        it = np.nditer(self.map, flags = ['multi_index'])

        for i in it:
            if i == 0:
                self.__getEdges(it.multi_index)