import numpy as np
from scipy.optimize import leastsq


def best_fit_plane(points):
    """
    https://stackoverflow.com/a/12301583
    Solve best fit plane for a set of points. Based on the plane equation: ax+by+cz+d=0
    :param points: Pandas DataFrame of 3d points.
    :return: values of a,b and c corresponding to best fit plane in a list.  
    """
    
    XYZ = np.array([list(points.x), list(points.y), list(points.z)])
    p0 = [0.506645455682, -0.185724560275, -1.43998120646, 1.37626378129]

    def f_min(X,p):
        plane_xyz = p[0:3]
        distance = (plane_xyz*X.T).sum(axis=1) + p[3]
        return distance / np.linalg.norm(plane_xyz)

    def residuals(params, signal, X):
        return f_min(X, params)

    sol = leastsq(residuals, p0, args=(None, XYZ))[0]
    
    return sol

