#!/usr/bin/python3
from ObstacleField import ObstacleField
import matplotlib as plt
import numpy as np
from Graph import Graph

class GraphSearchPlanner:

    def __init__(self, obsFieldIn = ObstacleField()):
        self.obsField = obsFieldIn
        self.graph = Graph(self.obsField.field)
