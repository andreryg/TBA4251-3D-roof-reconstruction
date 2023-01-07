import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from skimage.measure import ransac, LineModelND
import math

def ransac_line(points_x, points_y):
    """
    Finds all lines in a 2d pointcloud using the RANSAC model.
    :param points_x: list of x-coordinates
    :param points_y: list of y-coordinates
    :return: line and inliers
    """
    x = np.array(points_x).reshape(-1,1)
    y = np.array(points_y).reshape(-1,1)

    num_of_edges = 0
    lines_x = []
    lines_y = []

    data = np.column_stack([x,y])
    model = LineModelND

    while len(data) > 2 and num_of_edges < 4:
        model_robust, inliers = ransac(data, model, min_samples=2, residual_threshold=0.3, max_trials=1000)
        

        line_x = np.arange(min(x), max(x))
        line_y = model_robust.predict_y(line_x)

        #fix, ax = plt.subplots()
        #ax.plot(data[outliers, 0], data[outliers, 1], '.r', alpha=0.6, label='Outliers')
        #ax.plot(data[inliers, 0], data[inliers, 1], 'b', alpha=0.6, label='Inliers')
        plt.plot(line_x, line_y, '-b')
        temp_df = pd.DataFrame(data[inliers], columns=['x','y'])
        centerx, centery = np.average(temp_df.x), np.average(temp_df.y)
        dist = np.sqrt((temp_df.x-centerx)**2+(temp_df.y-centery)**2)
        print(dist)
        print(len(inliers))
        outliers = inliers == False
        print(outliers)
        data = data[outliers]
        plt.scatter(*zip(*data))
        plt.show()
        num_of_edges += 1
        lines_x.append(line_x)
        lines_y.append(line_y)
    plt.scatter(x,y)
    plt.show()