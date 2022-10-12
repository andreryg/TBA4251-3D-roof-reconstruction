import numpy as np
import math

def distance(center, points):
    """
    Calculates the distance between a center and points.
    :param center: A nd point.
    :param points: List of nd points.
    :return: List of distances from center to each point in points.
    """
    distances = []
    for i in points:
        distances.append(np.linalg.norm(i-center))
    return distances

def distribution(distances):
    """
    Creates a distribution from a list.
    :param distances: List of distances.
    :return: 2d List [number of distances left, cutoff]
    """
    dist = []
    for i in range(0, math.ceil(max(distances))+1):
        distances = list(filter(lambda distance: distance > i, distances))
        dist.append([len(distances)])
    return dist
