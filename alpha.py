#Implementation of alpha shape

import numpy as np
from scipy.spatial import Delaunay
from best_fit_plane import best_fit_plane
import matplotlib.pyplot as plt
import alphashape
from descartes import PolygonPatch
import math

from convertion import convert_to_2darray, convert_to_ndarray

def alpha_shape(points, alpha):
    """
    Converts a Dataframe of points to alpha shape. For simplicity all points are treadet as 2d points. 
    :param points: pandas dataframe with x and y column.
    :param alpha: alpha parameter between 0 and 1 used to create tighter fitting shape.
    :return: list of points in alpha shape
    """
    
    points_flat = tuple(zip(points.x, points.y))
    alpha_shape = alphashape.alphashape(points_flat, alpha)

    return alpha_shape
    heights = []
    for i in points:
        heights.append(i[2])
    print(sorted(heights))
    
    fig, ax = plt.subplots()
    ax.scatter(*zip(*points_flat))
    ax.add_patch(PolygonPatch(alpha_shape, alpha=0.4))
    

    def angle_between_vec(vec1, vec2):
        return np.rad2deg(np.arccos(np.clip(np.inner(vec1, vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)), -1.0, 1.0)))

    x,y = alpha_shape.exterior.coords.xy
    x_avg = sum(x)/len(x)
    y_avg = sum(y)/len(y)
    ax.scatter(x_avg,y_avg,color="b")
    plt.show()
    
    tot_angle = 0
    for i in range(0,len(x)-2):
        tot_angle += angle_between_vec([x[i+1]-x[i],y[i+1]-y[i]], [x[i+2]-x[i+1],y[i+2]-y[i+1]])
        print(tot_angle)
    print(tot_angle)

    """
    a = points[10]
    b = points[11]
    c = points[21]
    ab = b-a
    ac = c-a
    cross = np.cross(ab,ac)
    print(cross)
    """
    fit = best_fit_plane(points)
    plt.figure()
    ax = plt.axes(projection='3d')
    xs,ys,zs = zip(*points)
    ax.scatter3D(xs,ys,zs)

    xlim = ax.get_xlim()
    ylim = ax.get_ylim()
    X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),np.arange(ylim[0], ylim[1]))
    Z = np.zeros(X.shape)
    for r in range(X.shape[0]):
        for c in range(X.shape[1]):
            Z[r,c] = fit[0] * X[r,c] + fit[1] * Y[r,c] + fit[2]
    ax.plot_wireframe(X,Y,Z, color='k')

    plt.show()
    
    


def add_edge(edges, i, j):
    return None