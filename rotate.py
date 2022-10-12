import math
import numpy as np

def rotate(points):
    """
    Rotates a set of points on any 3d plane to the xy plane.
    """
    
    
    angle = 0

    def rot_matrix(axis, angle):
        if axis == "x":
            return np.matrix([[1, 0, 0], [0, math.cos(angle), -math.sin(angle)], [0, math.sin(angle), math.cos(angle)]])
        elif axis == "y":
            return  np.matrix([[math.cos(angle), 0, math.sin(angle)], [0, 1, 0], [-math.sin(angle), 0, math.cos(angle)]])
        elif axis == "z":
            return np.matrix([[math.cos(angle), -math.sin(angle), 0], [math.sin(angle), math.cos(angle), 0], [0, 0, 1]])
