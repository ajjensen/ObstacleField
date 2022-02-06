#!/usr/bin/python3

from GraphSearchPlanner import GraphSearchPlanner
from ObstacleField import ObstacleField
import numpy as np

size = [20, 20]
density = 0.2

map = ObstacleField(size, density)

planner = GraphSearchPlanner(map)
map.showField()