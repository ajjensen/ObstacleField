#!/usr/bin/python3

from GraphSearchPlanner import GraphSearchPlanner
from ObstacleField import ObstacleField
import numpy as np
import matplotlib.pyplot as plt

size = [64, 64]
densities = [0.0, 0.25, 0.5, 0.75]
successBFS = False
successDFS = False
successDIJ = False
iterationsBFS = {}
iterationsDFS = {}
iterationsDIJ = {}

for d in densities:
    map = ObstacleField(size, d)
    planner = GraphSearchPlanner(map)
    temp = str(d)
    d_str = temp.replace(".", "")

    figBFS, axBFS = plt.subplots()
    planner.obsFieldObj.showField(axBFS)
    while successBFS == False:
        successBFS = planner.planBreadthFirst(True, axBFS)
    plt.show()
    filename_BFS = "BFS_" + d_str
    plt.savefig(filename_BFS)
    iterationsBFS[d] = planner.BreadthFirstSol.numIterations

    figDFS, axDFS = plt.subplots()
    planner.obsFieldObj.showField(axDFS)
    while successDFS == False:
        successDFS = planner.planDepthFirst(True, axDFS)
    plt.show()
    filename_DFS = "DFS_" + d_str
    plt.savefig(filename_DFS)
    iterationsDFS[d] = planner.DepthFirstSol.numIterations

    figDIJ, axDIJ = plt.subplots()
    planner.obsFieldObj.showField(axDIJ)
    while successDIJ == False:
        successDIJ = planner.planDijkstra(True, axDIJ)
    plt.show()
    filename_DIJ = "DIJ_" + d_str
    plt.savefig(filename_DIJ)
    iterationsDIJ[d] = planner.DijkstraSol.numIterations

print("BFS number of iterations: ", iterationsBFS)
print("DFS number of iterations: ", iterationsDFS)
print("DIJ number of iterations: ", iterationsDIJ)



# TODO:
#   - generate plots
#   - compile data