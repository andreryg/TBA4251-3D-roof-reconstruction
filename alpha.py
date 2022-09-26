#Implementation of alpha shape

from ast import Del
import numpy as np
from scipy.spatial import Delaunay

def alpha_shape(pointcloud, alpha):
    tri = Delaunay(pointcloud)
    print(tri)