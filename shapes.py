import numpy as np

def rectangle(center, b, h):
    """
    Define a rectangle based on its geographical center and height and width. Returns a list of all the corner points. 
    :param center: 2d coordinate.
    :param b: float
    :param h: float
    :return: list of 2d points.
    """

    point1 = [center[0]-b/2, center[1]-h/2]
    point2 = [center[0]+b/2, center[1]-h/2]
    point3 = [center[0]+b/2, center[1]+h/2]
    point4 = [center[0]-b/2, center[1]+h/2]
    return [point1, point2, point3, point4]

def square(center, area):
    """
    Define a square based on its geographical center and the area. Returns a list of all the corner points. 
    :param center: 2d coordinate.
    :param area: float
    :return: list of 2d points.
    """

    s = np.sqrt(area)
    point1 = [center[0]-s/2, center[1]-s/2]
    point2 = [center[0]+s/2, center[1]-s/2]
    point3 = [center[0]+s/2, center[1]+s/2]
    point4 = [center[0]-s/2, center[1]+s/2]
    return [point1, point2, point3, point4]

def triangle(center, g, h):
    """
    Define a triangle based on its geographical center and its height and ground witdh. Returns a list of all the corner points.
    :param center: 2d coordinate
    :param g: float
    :param h: float
    :return: list of 2d points.
    """

    point1 = [center[0]-g/2, center[1]-h/2]
    point2 = [center[0]+g/2, center[1]-h/2]
    point3 = [center[0], center[1]+h/2]
    return [point1, point2, point3]

def trapezoid(center, a, b, h):
    """
    Define a trapezoid based on its geographical center and height and bases a and b. Returns a list of all the corner points. 
    :param center: 2d coordinate.
    :param a: float
    :param b: float
    :param h: float
    :return: list of 2d points.
    """

    point1 = [center[0]-b/2, center[1]-h/2]
    point2 = [center[0]+b/2, center[1]-h/2]
    point3 = [center[0]+a/2, center[1]+h/2]
    point4 = [center[0]-a/2, center[1]+h/2]
    return [point1, point2, point3, point4]