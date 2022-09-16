from pdb import lasti2lineno
import numpy as np
import laspy
import open3d as o3d
#from liblas import file

las = laspy.read("../sub roof data 1/10456495/10456495_1_3_1.las")
las2 = laspy.read("../sub roof data 1/10456495/10456495_1_3_2.las")
las3 = laspy.read("../sub roof data 1/10456495/10456495_1_3_3.las")
las4 = laspy.read("../sub roof data 1/10456495/10456495_1_3_4.las")
print(list(las.point_format.dimension_names))

point_data = np.stack([las.X, las.Y, las.Z], axis=0).transpose((1,0))
point_data2 = np.stack([las2.X, las2.Y, las2.Z], axis=0).transpose((1,0))
point_data3 = np.stack([las3.X, las3.Y, las3.Z], axis=0).transpose((1,0))
point_data4 = np.stack([las4.X, las4.Y, las4.Z], axis=0).transpose((1,0))
point_data = np.concatenate((point_data, point_data2, point_data3, point_data4), axis=0)

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])
