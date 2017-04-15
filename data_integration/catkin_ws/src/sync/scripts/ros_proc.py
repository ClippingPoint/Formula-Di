from cv_bridge import CvBridge, CvBridgeError
import numpy as np

#import numpy as np
"""
   ROS raw info preprocessor
"""

# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

class Image_proc:
    """
	Add your image preprocessor here
	Such as transformation, cropping and so forth
    """
    def __init__(self):
	self.images = []

    def image_converter(self, image_messages):
	for i, image_message in enumerate(image_messages):
    	    try: 
	    	cv_image = bridge.imgmsg_to_cv2(image_message, desired_encoding="passthrough")
		return cv_image
	    except CvBridgeError as e:
	    	rospy.logerr(e)
    def push_image(self, image):
	self.images.append(image)

class Point_cloud_proc:
    def __init__(self):
	self.filtered = []
	self.XYZI = []

    def push_point_cloud_filtered(self, filtered):
	self.filtered.append(filtered)

    def push_point_cloud_XYZI(self, xyzi):
	self.XYZI.append(xyzi)
    
    def get_point_cloud_XYZI(self, point_cloud):
	return point_cloud[:, 0:3]

    def filter_point_cloud(self, point_cloud, fwd_range=(-20, 20.), side_range=(-20., 20.), height_range=(-10., 10.)):
        l_and = lambda *x: np.logical_and.reduce(x)
        l_or = lambda *x: np.logical_or.reduce(x)
	"""
	   data filtering under velodyne coordinates
	   Positives: Forward, left, up
	"""
	x_points = point_cloud[:, 0]
	y_points = point_cloud[:, 1]
	z_points = point_cloud[:, 2]

    # FILTER - To return only indices of points within desired cube
    # Three filters for: Front-to-back, side-to-side, and height ranges
    # Note left side is positive y axis in LIDAR coordinates
        f_filt = l_and((x_points > fwd_range[0]), (x_points < fwd_range[1]))
        s_filt = l_and((y_points > side_range[0]), (y_points < side_range[1]))
	
        # filtered = l_and(f_filt, l_and(s_filt, h_filt))
        filtered = l_and(f_filt, s_filt)
        indices = np.argwhere(filtered).flatten()

    # KEEPERS
        x_points = x_points[indices]
        y_points = y_points[indices]
        z_points = z_points[indices]

	h_filt = l_and((z_points > height_range[0], (z_points < height_range[1])))
	indices = np.argwhere(h_filt).flatten()
	
        x_points = x_points[indices]
        y_points = y_points[indices]
        z_points = z_points[indices]

	return np.hstack((x_points, y_points, z_points))
