"""
Basic steps:
-Iterate through the pointcloud files of roof segments. Point_source_id can maybe differentiate the roofs, all segments of same roof have same id.
-Find the angle of the plane corresponding to the roof segment.
-Generate an alpha-shape of the roof segment.
-Fit alpha-shape to premade roof segment shapes.
-Visualize the shapes in 3d with the pointcloud.
-(Create LoD2 models)
"""

import numpy as np
import laspy
from alpha_shape import alphaShape
from best_fit_plane import best_fit_plane
from centroid import centroid
from distance import distance, distribution
from convertion import convert_to_ndarray
import matplotlib.pyplot as plt
import pandas as pd
from shapeFitting import fit_to_shape

pointcloud = laspy.read("../sub roof data 1/10477867/10477867_2_7_2.las") #rectangle
#pointcloud = laspy.read("../sub roof data 1/10456495/10456495_1_3_2.las") #triangle
points = pd.DataFrame(pointcloud.xyz, columns=['x', 'y', 'z'])
fit = (best_fit_plane(points))
alpha_points, area, center = alphaShape(points)
fit_to_shape(alpha_points, area, center)

plt.figure()
ax = plt.axes(projection='3d')
#xs,ys,zs = zip(*points)
ax.scatter3D(points.x,points.y,points.z)

xlim = ax.get_xlim()
ylim = ax.get_ylim()
X,Y = np.meshgrid(np.arange(xlim[0], xlim[1]),np.arange(ylim[0], ylim[1]))
Z = np.zeros(X.shape)
for r in range(X.shape[0]):
    for c in range(X.shape[1]):
        Z[r,c] = fit[0] * X[r,c] + fit[1] * Y[r,c] + fit[2]
ax.plot_wireframe(X,Y,Z, color='k')

plt.show()