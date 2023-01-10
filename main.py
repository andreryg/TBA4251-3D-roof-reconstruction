import numpy as np
import laspy
from alpha_shape import alphaShape
from best_fit_plane import best_fit_plane
import matplotlib.pyplot as plt
import pandas as pd
from shapeFitting import fit_to_shape
from folderIteration import folder_iteration

from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

#pointcloud = laspy.read("../sub roof data 1/10477867/10477867_2_7_1.las") #rectangle
#pointcloud = laspy.read("../sub roof data 1/10456495/10456495_1_3_2.las") #triangle
#pointcloud = laspy.read("../sub roof data 1/10527457/10527457_2_7_4.las") #Trapezium
#pointcloud = laspy.read("../sub roof data 1/182452858/182452858_1_6_3.las") #Parallelogram
roof_paths = folder_iteration() #Generating lists with all the names of the roof segment point cloud files. 

for i in roof_paths:
    shapes = []
    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)
    pointss = pd.DataFrame(columns=['x','y','z'])
    for j in i:
        try:
            pointcloud = laspy.read(j) #Reading point cloud
            points = pd.DataFrame(pointcloud.xyz, columns=['x', 'y', 'z']) #Converting points in point cloud to dataframe
            pointss = pd.concat([pointss, points]) #Combining dataframes with others of the same roof.
            fit = (best_fit_plane(points)) #Finding the a,b,c values of the best fitted plane to the points.
            alpha_points, area, center = alphaShape(points) #Finding the alpha shape. 
            shape = fit_to_shape(alpha_points, area, center) #Finding which shape fits the best to the alpha shape. 
            shape = [list(coord) for coord in shape]
            for i in shape:
                i.append(float((-fit[0] * i[0] - fit[1] * i[1] - fit[3])/fit[2]))

            ax.add_collection3d(Poly3DCollection([shape], color='red', edgecolor='black'))
        except AttributeError:
            print("Bad polygon shape")

    z_value = np.min(pointss.z)
    z = np.empty(len(pointss.index))
    z.fill(z_value-5)
    ax.scatter3D(pointss.x,pointss.y,z,c='gray')
    ax.set_xlim3d(np.min(points.x)-10, np.max(points.x)+10)
    ax.set_ylim3d(np.min(points.y)-10, np.max(points.y)+10)
    ax.set_zlim3d(np.min(points.z)-10, np.max(points.z)+10)
    ax.set_box_aspect([1,1,1])
    plt.show()
