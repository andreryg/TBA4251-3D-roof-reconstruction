import math

def rotatePoints(points, center, deg=1):
    """
    https://gist.github.com/somada141/d81a05f172bb2df26a2c
    Rotates a list of points around a center deg degrees.  
    :param points: 2d list of points.
    :param center: 2d point.
    :param deg: integer.
    :return: list of 2d points
    """

    angle = math.radians(deg)
    rotatedPoints = []
    for point in points:
        temp_point = point[0]-center[0], point[1]-center[1]
        temp_point = (temp_point[0]*math.cos(angle) - temp_point[1]*math.sin(angle), temp_point[0]*math.sin(angle) + temp_point[1]*math.cos(angle))
        temp_point = temp_point[0]+center[0], temp_point[1]+center[1]
        rotatedPoints.append(temp_point)
    return rotatedPoints