import numpy as np
import math
import shapely

def distancePointToShape(points, shape):
    """
    Finds the average distance between all the points in a list and a shape to determine similarity. 
    """
    poly = shapely.Polygon(shape)
    total_distance = 0
    for i in points:
        total_distance += poly.boundary.distance(shapely.Point(i))
    return total_distance

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
