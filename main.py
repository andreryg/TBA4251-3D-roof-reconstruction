"""
Basic steps:
-Iterate through the pointcloud files of roof segments. Point_source_id can maybe differentiate the roofs, all segments of same roof have same id.
-Find the angle of the plane corresponding to the roof segment.
-Generate an alpha-shape of the roof segment.
-Fit alpha-shape to premade roof segment shapes.
-Visualize the shapes in 3d with the pointcloud.
-(Create LoD2 models)
"""