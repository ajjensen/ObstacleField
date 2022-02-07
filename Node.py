#!/usr/bin/python3
import numpy as np

class Node:
    # A Node object has three important parts:
    #
    #   id      -   tuple which identifies the node, and corresponds to index in the map
    #   edges   -   a dictionary whose keys are the id (indices as tuple) of the connected nodes
    #               and the values are the weight of the edges
    #   state   -   indicates if the node has been searched

    states = ['Unvisited', 'Dead', 'Alive']

    def __init__(self, id, weightedEdges = False):
        self.id = id
        self.edges = {}
        self.state = self.states[0]
        self.cost = 0

    def addEdge(self, nextNode, weight = 1):
        if isinstance(nextNode, Node):
            if (not nextNode.id in self.edges):
                self.edges[nextNode.id] = weight
        elif (not nextNode in self.edges):
            self.edges[nextNode] = weight

    def getEdges(self):
        pass

    def setState_Dead(self):
        self.state = self.states[1]

    def setState_Unvisited(self):
        self.state = self.states[0]

    def setState_Alive(self):
        self.state = self.states[2]

    def isUnvisited(self):
        if self.state == 'Unvisited':
            return True
        else:
            return False

    def isDead(self):
        if self.state == 'Dead':
            return True
        else:
            return False

    def isAlive(self):
        if self.state == 'Alive':
            return True
        else:
            return False