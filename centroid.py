import numpy as np

def centroid(points):
    """
    Finds centroid of nd points in a 2d array
    :param points: 2d array
    :return: list with x,y,z coordinate of centroid.
    """
    
    return np.average(points, axis=0)