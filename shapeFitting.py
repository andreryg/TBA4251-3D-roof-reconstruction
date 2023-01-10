import numpy as np
from rotate import rotatePoints
from shapes import rectangle, square, triangle, iso_trapezium, parallelogram, trapezium
from distance import distancePointToShape
import matplotlib.pyplot as plt

def fit_to_shape(points, area, center):
    """
    Fit points to a best shape and calculate the parameters of the shape. Returns a list of points in the best fitted shape.
    :param points: list of 2d points.
    :param area: float
    :param center: 2d point.
    :return: list
    """

    threshold = 0.15 #Optimal max distance allowed. 
    orig_points = points.copy()
    points = np.array(points)
    x = points[:,0]
    y = points[:,1]
    xy_aligned_bounding_box_area = (np.max(x)-np.min(x))*(np.max(y)-np.min(y))
    for i in range(359): #Rotating each roof segment to align to the predefined shapes. 
        temp_points = np.array(rotatePoints(orig_points, center, i))
        x = temp_points[:,0]
        y = temp_points[:,1]
        temp_area = (np.max(x)-np.min(x))*(np.max(y)-np.min(y))
        
        if temp_area < xy_aligned_bounding_box_area:
            points = temp_points
            xy_aligned_bounding_box_area = temp_area
            rotation = i

    old_center = center.copy()
    x = points[:,0]
    y = points[:,1]
    
    center = [(np.max(x)+np.min(x))/2, (np.max(y)+np.min(y))/2]

    Square = square(center, area)
    distance = 1000
    temp_dist = distancePointToShape(points, Square)
    if temp_dist < distance:
        distance = temp_dist
        best_fit = Square
    if distance < threshold:
        return rotatePoints(best_fit, old_center, -rotation)
  
    
    #TRIANGLE
    temp_distance = 1000
    g = h = np.sqrt(area*2) 
    Triangle = triangle(center, g, h)
    temp_dist = distancePointToShape(points, Triangle)
    if temp_dist < temp_distance:
        temp_distance = temp_dist
        best_tri = Triangle
    while(True):
        temp_height = h - 0.5
        g = 2*area/temp_height
        Triangle = triangle(center, g, temp_height)
        temp_dist = distancePointToShape(points, Triangle)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_tri = Triangle
            h = temp_height
            continue

        temp_height = h + 0.5
        g = 2*area/temp_height
        Triangle = triangle(center, g, temp_height)
        temp_dist = distancePointToShape(points, Triangle)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_tri = Triangle
            h = temp_height
            continue

        Triangle = rotatePoints(Triangle, center, 180) #Try to flip the triangle incase the initial rotation made it stand on its head. 
        temp_dist = distancePointToShape(points, Triangle)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_tri = Triangle
            continue
        break
    if temp_distance < distance:
        distance = temp_distance
        best_fit = best_tri
    if distance < threshold:
        return rotatePoints(best_fit, old_center, -rotation)


    #RECTANGLE
    temp_distance = 1000
    b = h = np.sqrt(area)
    Rectangle = rectangle(center, b, h)
    temp_dist = distancePointToShape(points, Rectangle)
    if temp_dist < temp_distance:
        temp_distance = temp_dist
        best_rect = Rectangle
    while(True):
        temp_height = h + 0.5
        b = area/temp_height
        Rectangle = rectangle(center, b, temp_height)
        temp_dist = distancePointToShape(points, Rectangle)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_rect = Rectangle
            h = temp_height
            continue

        temp_height = h - 0.5
        b = area/temp_height
        Rectangle = rectangle(center, b, temp_height)
        temp_dist = distancePointToShape(points, Rectangle)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_rect = Rectangle
            h = temp_height
            continue
        break
    if temp_distance < distance:
        distance = temp_distance
        best_fit = best_rect
    if distance < threshold:
        return rotatePoints(best_fit, old_center, -rotation)
 

    #ISOSCELES TRAPEZIUM
    temp_distance = 1000
    a = b = h = np.sqrt(area)
    Iso_trapezium = iso_trapezium(center, a, b, h)
    temp_dist = distancePointToShape(points, Iso_trapezium)
    if temp_dist < temp_distance:
        temp_distance = temp_dist
        best_isotrap = Iso_trapezium

    angles = np.arange(0,360, 10).tolist()
    while(True):
        for i in angles:
            temp_a = a + 0.5
            temp_b = b - 0.5
            Iso_trapezium = iso_trapezium(center, temp_a, temp_b, h)
            Iso_trapezium = rotatePoints(Iso_trapezium, center, i)
            temp_dist = distancePointToShape(points, Iso_trapezium)
            if temp_dist < temp_distance:
                temp_distance = temp_dist
                best_isotrap = Iso_trapezium
                a = temp_a
                b = temp_b
                continue

            temp_a = a - 0.5
            temp_b = b + 0.5
            Iso_trapezium = iso_trapezium(center, temp_a, temp_b, h)
            Iso_trapezium = rotatePoints(Iso_trapezium, center, i)
            temp_dist = distancePointToShape(points, Iso_trapezium)
            if temp_dist < temp_distance:
                temp_distance = temp_dist
                best_isotrap = Iso_trapezium
                a = temp_a
                b = temp_b
                continue
            
            temp_height = h + 0.9
            x = (a+b)/(2*temp_height)
            temp_a = a-x
            temp_b = b-x
            Iso_trapezium = iso_trapezium(center, temp_a, temp_b, temp_height)
            Iso_trapezium = rotatePoints(Iso_trapezium, center, i)
            temp_dist = distancePointToShape(points, Iso_trapezium)
            if temp_dist < temp_distance:
                temp_distance = temp_dist
                best_isotrap = Iso_trapezium
                h = temp_height
                a = temp_a
                b = temp_b
                continue

            temp_height = h - 0.9
            x = (a+b)/(2*temp_height)
            temp_a = a+x
            temp_b = b+x
            Iso_trapezium = iso_trapezium(center, temp_a, temp_b, temp_height)
            Iso_trapezium = rotatePoints(Iso_trapezium, center, i)
            temp_dist = distancePointToShape(points, Iso_trapezium)
            if temp_dist < temp_distance:
                temp_distance = temp_dist
                best_isotrap = Iso_trapezium
                h = temp_height
                a = temp_a
                b = temp_b
                continue
        break
 
    if temp_distance < distance:
        distance = temp_distance
        best_fit = best_isotrap
    if distance < threshold:
        return rotatePoints(best_fit, old_center, -rotation)


    #PARALLELOGRAM
    temp_distance
    offset = 0
    g = h = np.sqrt(area)
    Parallelogram = parallelogram(center, g, h, offset)
    temp_dist = distancePointToShape(points, Parallelogram)
    if temp_dist < temp_distance:
        temp_distance = temp_dist
        best_para = Parallelogram
    while(True):
        temp_g = g + 1
        h = area/temp_g
        Parallelogram = parallelogram(center, temp_g, h, offset)
        temp_dist = distancePointToShape(points, Parallelogram)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_para = Parallelogram
            g = temp_g
            continue

        temp_g = g - 1
        h = area/temp_g
        Parallelogram = parallelogram(center, temp_g, h, offset)
        temp_dist = distancePointToShape(points, Parallelogram)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_para = Parallelogram
            g = temp_g
            continue

        temp_offset = offset + 1
        Parallelogram = parallelogram(center, g, h, offset)
        temp_dist = distancePointToShape(points, Parallelogram)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_para = Parallelogram
            offset = temp_offset
            continue

        temp_offset = offset - 1
        Parallelogram = parallelogram(center, g, h, offset)
        temp_dist = distancePointToShape(points, Parallelogram)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_para = Parallelogram
            offset = temp_offset
            continue
        break
    if temp_distance < distance:
        distance = temp_distance
        best_fit = best_para
    if distance < threshold:
        return rotatePoints(best_fit, old_center, -rotation)


    #TRAPEZIUM
    temp_distance = 1000
    offset = 0
    trap_rotation = 0
    w = h = np.sqrt(area)
    Trapezium = trapezium(center, w, h, offset)
    temp_dist = distancePointToShape(points, Parallelogram)
    if temp_dist < temp_distance:
        temp_distance = temp_dist
        best_trap = Trapezium
        
    w = area/h
    temp_distance = 1000
    for i in [0, 90, 180, 270]:
        temp_offset = offset + 0.5
        Trapezium = trapezium(center, w, h, temp_offset)
        Trapezium = rotatePoints(Trapezium, center, i)
        temp_dist = distancePointToShape(points, Trapezium)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            trap_rotation = i
        
        temp_offset = offset - 0.5
        Trapezium = trapezium(center, w, h, temp_offset)
        Trapezium = rotatePoints(Trapezium, center, i)
        temp_dist = distancePointToShape(points, Trapezium)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            trap_rotation = i

    while(True):
        temp_height = h + 0.5
        w = area/temp_height
        Trapezium = trapezium(center, w, temp_height, offset)
        Trapezium = rotatePoints(Trapezium, center, trap_rotation)
        temp_dist = distancePointToShape(points, Trapezium)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_trap = Trapezium
            h = temp_height
            continue

        temp_height = h - 0.5
        w = area/temp_height
        Trapezium = trapezium(center, w, temp_height, offset)
        Trapezium = rotatePoints(Trapezium, center, trap_rotation)
        temp_dist = distancePointToShape(points, Trapezium)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_trap = Trapezium
            h = temp_height
            continue

        temp_offset = offset + 0.5
        Trapezium = trapezium(center, w, h, temp_offset)
        Trapezium = rotatePoints(Trapezium, center, trap_rotation)
        temp_dist = distancePointToShape(points, Trapezium)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_trap = Trapezium
            offset = temp_offset
            continue

        temp_offset = offset - 0.5
        Trapezium = trapezium(center, w, h, temp_offset)
        Trapezium = rotatePoints(Trapezium, center, trap_rotation)
        temp_dist = distancePointToShape(points, Trapezium)
        if temp_dist < temp_distance:
            temp_distance = temp_dist
            best_trap = Trapezium
            offset = temp_offset
            continue
        break
    if temp_distance < distance:
        distance = temp_distance
        best_fit = best_trap
    
    return rotatePoints(best_fit, old_center, -rotation)
    

    plt.scatter(*zip(*best_fit))
    plt.scatter(*zip(*points))
    plt.scatter(old_center[0],old_center[1])
    plt.show()
