import numpy as np

def convert_to_ndarray(pointcloud):
    points = np.zeros((len(pointcloud.x)-1,3))

    for i in range(0, len(pointcloud.x)-1):
        points[i] = [pointcloud.x[i], pointcloud.y[i], pointcloud.z[i]]
    
    return points

def convert_to_2darray(points):
    points2d = np.zeros((len(points)-1,2))

    for i in range(0, len(points)-1):
        points2d[i] = [points[i][0], points[i][1]]

    return points2d