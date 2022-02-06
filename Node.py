#!/usr/bin/python3
import numpy as np

class Node:
    # A Node object has two important parts:
    #
    #   id              -   this is what identifies the node itself
    #   connections     -   a dictionary whose keys are the id of the connected nodes
    #                       and the values are the weight of the edges

    def __init__(self, id, weightedEdges = False):
        self.id = id
        self.edges = {}

    def addConnection(self, nextNodeID, weight = 1):
        if np.isscalar(nextNodeID):
            self.edges[nextNodeID] = weight

        else:
            for i in nextNodeID:
                self.edges[i] = weight