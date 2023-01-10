import numpy as np
from scipy.spatial import ConvexHull, convex_hull_plot_2d
import matplotlib.pyplot as plt
import alphashape

def alphaShape(points, alpha=0.2):
    """
    Converts a Dataframe of points to alpha shape. For simplicity all points are treated as 2d points. 
    :param points: pandas dataframe with x and y column.
    :param alpha: alpha parameter between 0 and 1 used to create tighter fitting shape.
    :return: list of points in alpha shape, area of alpha shape and the pointclouds geographical center
    """

    #print(points)
    points_flat = list(zip(points.x, points.y))
    alpha_shape = alphashape.alphashape(points_flat,alpha)
    xx, yy = alpha_shape.exterior.coords.xy
    alpha_points = list(zip(xx,yy))
    alpha_points = [list(item) for item in alpha_points]
    area = alpha_shape.area
    bounds = alpha_shape.bounds
    center = [(bounds[2]+bounds[0])/2, (bounds[3]+bounds[1])/2]

    return alpha_points, area, center
