#import rospy
import sensor_msgs.point_cloud2 as pc2
import numpy as np

"""
Add your lidar point cloud preprocessor here

Such as filtering, cropping, intensity or more?

All processing methods should be done in Velodyne coordinates
"""

class Lidar_Proc():
    def __init__(self):
	NotImplementedError
	return
    def method_1(self):
	NotImplementedError


def lidar_to_pc2(lidar_msg):
    """
    Parameters:
    ------------------
    ------------------
    """
    return np.array(list(pc2.read_points(lidar_msg)))
