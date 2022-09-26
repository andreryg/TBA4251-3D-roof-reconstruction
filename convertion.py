import numpy as np

def convert_to_ndarray(pointcloud):
    points = np.zeros((len(pointcloud)-1,3))

    for i in range(0, len(pointcloud)-1):
        points[i] = [pointcloud.x[i], pointcloud.y[i], pointcloud.z[i]]
    
    return points