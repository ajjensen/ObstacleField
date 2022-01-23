#!/usr/bin/python3
import numpy as np
from random import choice

class Tetromino:
    'Tetromino objects resemble tetris blocks'

    blocks = {'T' : np.array([[1, 1, 1],[0, 1, 0]]), \
        'S' : np.array([[0, 1, 1], [1, 1, 0]]), \
        'Z' : np.array([[1, 1, 0], [0, 1, 1]]), \
        'J' : np.array([[0, 1], [0, 1], [1, 1]]), \
        'L' : np.array([[1, 0], [1, 0], [1, 1]]), \
        'I' : np.array([[1], [1], [1], [1]]), \
        'O' : np.array([[1, 1],[1, 1]])}


    def __init__(self):
        return None

    def getRandom(self):
        result = choice(list(self.blocks.keys()))

        return self.blocks.get(result)

    
