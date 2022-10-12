from pdb import lasti2lineno
import numpy as np
import laspy
import open3d as o3d

from alpha import alpha_shape
from best_fit_plane import best_fit_plane
from convertion import convert_to_ndarray
#from liblas import file

las = laspy.read("../sub roof data 1/10456495/10456495_1_3_1.las")
las2 = laspy.read("../sub roof data 1/10456495/10456495_1_3_2.las")
las3 = laspy.read("../sub roof data 1/10456495/10456495_1_3_3.las")
las4 = laspy.read("../sub roof data 1/10456495/10456495_1_3_4.las")
las5 = laspy.read("../sub roof data 1/10478413/10478413_2_7_1.las")
las6 = laspy.read("../sub roof data 1/10478413/10478413_2_7_2.las")
las7 = laspy.read("../sub roof data 1/10478413/10478413_2_7_3.las")
las8 = laspy.read("../sub roof data 1/10478413/10478413_2_7_4.las")
print(list(las.point_format.dimension_names))
#print(las7.point_source_id)
#print(las8.point_source_id)
#print(las3.point_source_id)
alpha_shape(las6, 2)


"""
point_data = np.stack([las.x, las.y, las.z], axis=0).transpose((1,0))
point_data2 = np.stack([las2.x, las2.y, las2.z], axis=0).transpose((1,0))
point_data3 = np.stack([las3.x, las3.y, las3.z], axis=0).transpose((1,0))
point_data4 = np.stack([las4.x, las4.y, las4.z], axis=0).transpose((1,0))
point_data5 = np.stack([las5.x, las5.y, las5.z], axis=0).transpose((1,0))
point_data6 = np.stack([las6.x, las6.y, las6.z], axis=0).transpose((1,0))
point_data7 = np.stack([las7.x, las7.y, las7.z], axis=0).transpose((1,0))
point_data8 = np.stack([las8.x, las8.y, las8.z], axis=0).transpose((1,0))
point_data = np.concatenate((point_data5, point_data6, point_data7, point_data8), axis=0)

geom = o3d.geometry.PointCloud()
geom.points = o3d.utility.Vector3dVector(point_data)
o3d.visualization.draw_geometries([geom])
"""
