#!/usr/bin/python3

from GraphSearchPlanner import GraphSearchPlanner
from ObstacleField import ObstacleField
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors

size = [20, 20]
density = 0.2

map = ObstacleField(size, density)
planner = GraphSearchPlanner(map)

# Plot graph and obstacle field
fig, ax = plt.subplots()
planner.obsField.showField(ax)
planner.graph.plotGraph(ax)
plt.show()