import numpy as np
from rotate import rotatePoints
from shapes import rectangle, square, triangle, trapezoid
from distance import distancePointToShape
import matplotlib.pyplot as plt
from tqdm import tqdm

def fit_to_shape(points, area, center):
    """
    Fit points to a best shape and calculate the parameters of the shape. Returns a list of points in the best fitted shape.
    :param points: list of 2d points.
    :param area: float
    :param center: 2d point.
    :return: list
    """

    threshold = 0.2 #Max distance allowed. 
    orig_points = points.copy()
    points = np.array(points)
    x = points[:,0]
    y = points[:,1]
    xy_aligned_bounding_box_area = (np.max(x)-np.min(x))*(np.max(y)-np.min(y))
    rotation = 0
    while(True): #Rotating each roof segment to align to the predefined shapes. 
        temp_points = np.array(rotatePoints(points, center))
        x = temp_points[:,0]
        y = temp_points[:,1]
        temp_area = (np.max(x)-np.min(x))*(np.max(y)-np.min(y))
        if temp_area < xy_aligned_bounding_box_area:
            points = temp_points
            xy_aligned_bounding_box_area = temp_area
            rotation += 1
            continue

        temp_points = np.array(rotatePoints(points, center,-1))
        x = temp_points[:,0]
        y = temp_points[:,1]
        temp_area = (np.max(x)-np.min(x))*(np.max(y)-np.min(y))
        if temp_area < xy_aligned_bounding_box_area:
            points = temp_points
            xy_aligned_bounding_box_area = temp_area
            rotation -= 1
            continue
        break

    """
    to do list:
    remove rotation of shapes.
    add the rest of the shapes and parameter change. When changing parameters a new shape is created for every change. 
    triangles also need to check for mirrored.
    maybe add parallellogram. 
    remember correct constraints: only change when a decrease in distance is found. 
    can maybe remove square and rectangle, trapezoid already covers well. 
    rotate back after best shape is found. 
    """
        

    Square = square(center, area)
    distance = 1000
    temp_dist = distancePointToShape(points, Square)
    if temp_dist < distance:
        distance = temp_dist
        best_fit = Square
    if distance < threshold:
        pass
        #return rotatePoints(best_fit, center, -rotation)
    print(distance)
    
    #TRIANGLE
    g = h = np.sqrt(area*2) 
    Triangle = triangle(center, g, h)
    temp_dist = distancePointToShape(points, Triangle)
    if temp_dist < distance:
        distance = temp_dist
        best_fit = Triangle
    while(True):
        temp_height = h + 1
        g = 2*area/temp_height
        Triangle = triangle(center, g, temp_height)
        temp_dist = distancePointToShape(points, Triangle)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Triangle
            h = temp_height
            continue

        temp_height = h - 1
        g = 2*area/temp_height
        Triangle = triangle(center, g, temp_height)
        temp_dist = distancePointToShape(points, Triangle)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Triangle
            h = temp_height
            continue

        Triangle = rotatePoints(Triangle, center, 90) #Try to flip the triangle incase the initial rotation made it stand on its head. 
        temp_dist = distancePointToShape(points, Triangle)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Triangle
            continue
        break
    if distance < threshold:
        pass
        #return rotatePoints(best_fit, center, -rotation)
    print(distance)

    #RECTANGLE
    b = h = np.sqrt(area)
    Rectangle = rectangle(center, b, h)
    temp_dist = distancePointToShape(points, Rectangle)
    if temp_dist < distance:
        distance = temp_dist
        best_fit = Rectangle
    while(True):
        temp_height = h + 1
        b = area/temp_height
        Rectangle = rectangle(center, b, temp_height)
        temp_dist = distancePointToShape(points, Rectangle)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Rectangle
            h = temp_height
            continue

        temp_height = h - 1
        b = area/temp_height
        Rectangle = rectangle(center, b, temp_height)
        temp_dist = distancePointToShape(points, Rectangle)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Rectangle
            h = temp_height
            continue
        break
    if distance < threshold:
        pass
        #return rotatePoints(best_fit, center, -rotation)
    print(distance)

    #TRAPEZOID
    a = b = h = np.sqrt(area)
    Trapezoiod = trapezoid(center, a, b, h)
    temp_dist = distancePointToShape(points, Trapezoiod)
    if temp_dist < distance:
        distance = temp_dist
        best_fit = Trapezoiod
    while(True):
        temp_height = h + 1
        x = (a+b)/(2*temp_height)
        a = a-x
        b = b-x
        Trapezoiod = trapezoid(center, a, b, temp_height)
        temp_dist = distancePointToShape(points, Trapezoiod)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Trapezoiod
            h = temp_height
            continue

        temp_height = h - 1
        x = (a+b)/(2*temp_height)
        a = a-x
        b = b-x
        Trapezoiod = trapezoid(center, a, b, temp_height)
        temp_dist = distancePointToShape(points, Trapezoiod)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Trapezoiod
            h = temp_height
            continue

        temp_a = a + 1
        temp_b = b - 1
        Trapezoiod = trapezoid(center, temp_a, temp_b, h)
        temp_dist = distancePointToShape(points, Trapezoiod)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Trapezoiod
            a = temp_a
            b = temp_b
            continue

        temp_a = a - 1
        temp_b = b + 1
        Trapezoiod = trapezoid(center, temp_a, temp_b, h)
        temp_dist = distancePointToShape(points, Trapezoiod)
        if temp_dist < distance:
            distance = temp_dist
            best_fit = Trapezoiod
            a = temp_a
            b = temp_b
            continue
        break
    if distance < threshold:
        pass
        #return rotatePoints(best_fit, center, -rotation)
    print(distance)
    
    plt.scatter(*zip(*best_fit))
    plt.scatter(*zip(*points))
    plt.scatter(center[0],center[1])
    plt.show()
