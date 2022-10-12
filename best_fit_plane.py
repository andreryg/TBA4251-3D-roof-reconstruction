import numpy as np

def best_fit_plane(points):
    """
    Solve best fit plane for a set of points. Based on the plane equation: ax+by+c=z => Ax=B.
    :param points: Pandas DataFrame of 3d points.
    :return: values of a,b and c corresponding to best fit plane in a list.  
    """
    A = np.matrix(list(zip(points.x, points.y, np.ones(len(points.index)))))
    B = np.matrix(points.z).T

    best_fit = (A.T * A).I * A.T * B
    return best_fit