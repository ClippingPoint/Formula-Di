##
## Based on paper 
## Multi-View 3D Object Detection Network for Autonomous Driving

import numpy as np
from collections import defaultdict

def scale_to_(num_):
	def scale_to_num(a, min_, max_, dtype=np.uint8):
		return (((a - min_) / float(max_ - min_)) * num_).astype(dtype)
	return scale_to_num
#The point cloud is devided equally into M slices. A height map is computed for each slice
##---------------------------------------------------------------------------------------
## Define "forward" transformation Point Cloud to 2D view
##---------------------------------------------------------------------------------------
def point_cloud_to_front_view(points,
                           v_res,
                           h_res,
                           v_fov,
                           val="depth",
                           y_fudge=0.0
                           ):
    """ Takes points in 3D space from LIDAR data and projects them to a 2D
        "front view" image, and saves that image.
	http://ronny.rest/blog/post_2017_03_25_lidar_to_2d/

    Args:
        points: (np array)
            The numpy array containing the lidar points.
            The shape should be Nx4
            - Where N is the number of points, and
            - each point is specified by 4 values (x, y, z, reflectance)
        v_res: (float)
            vertical resolution of the lidar sensor used.
	    for HDL_32E use 1.33
        h_res: (float)
            horizontal resolution of the lidar sensor used.
	    for HDL_32E use 1
        v_fov: (tuple of two floats)
            (minimum_negative_angle, max_positive_angle)
        val: (str)
            What value to use to encode the points that get plotted.
            One of {"depth", "height", "reflectance"}
	Not Used:
        cmap: (str)
            Color map to use to color code the `val` values.
            NOTE: Must be a value accepted by matplotlib's scatter function
            Examples: "jet", "gray"
	Not Used:
        saveto: (str or None)
            If a string is provided, it saves the image as this filename.
            If None, then it just shows the image.
        y_fudge: (float)
            A hacky fudge factor to use if the theoretical calculations of
            vertical range do not match the actual data.

            For a Velodyne HDL 64E, set this value to 5.
    """

    # DUMMY PROOFING
    assert len(v_fov) ==2, "v_fov must be list/tuple of length 2"
    assert v_fov[0] <= 0, "first element in v_fov must be 0 or negative"
    assert val in {"depth", "height", "reflectance"}, \
        'val must be one of {"depth", "height", "reflectance"}'

    x_lidar = points[:, 0]
    y_lidar = points[:, 1]
    z_lidar = points[:, 2]
    r_lidar = points[:, 3] # Reflectance
    # Distance relative to origin when looked from top
    d_lidar = np.sqrt(x_lidar ** 2 + y_lidar ** 2)
    # Absolute distance relative to origin
    # d_lidar = np.sqrt(x_lidar ** 2 + y_lidar ** 2, z_lidar ** 2)

    v_fov_total = -v_fov[0] + v_fov[1]

    # Convert to Radians
    v_res_rad = v_res * (np.pi/180)
    h_res_rad = h_res * (np.pi/180)

    # PROJECT INTO FRONT VIEW
    # FRONT VIEW Coordinate(RU) x-pos R, y-pos U 
    x_front = np.floor(np.arctan2(y_lidar, x_lidar)/ h_res_rad)
    y_front = np.floor(np.arctan2(z_lidar, d_lidar)/ v_res_rad)


    # SHIFT COORDINATES TO MAKE 0,0 THE MINIMUM
    x_max = 360.0 / h_res       # Theoretical max x value after shifting

    y_max = v_fov_total / v_res # Theoretical max x value after shifting

    y_max += y_fudge            # Fudge factor if the calculations based on
                                # spec sheet do not match the range of
                                # angles collected by in the data.

    # WHAT DATA TO USE TO ENCODE THE VALUE FOR EACH PIXEL
    if val == "reflectance":
        pixel_values = r_lidar
    elif val == "height":
        pixel_values = z_lidar
    else:
        pixel_values = -d_lidar

    front = np.zeros([y_max, x_max], dtype=np.uint8)
    # FILL PIXEL VALUES IN FRONT ARRAY
    front[y_front, x_front] = pixel_values

    return front

# For generating sliced height map 
# Maybe we can do this calculation on the fly to save some bandwidth?
def get_top_sliced_height_maps(top_, y_top_, x_top_, height_, num_channel, height_range_):
    	"""
	Parameters:
        ------------------------------------------------
	top: np.zeros array with y_top, x_top dimension
        num_channel: Number of bins e.g. 14
	Assume uniform distribution over height
	height_range_: LiDAR height information
        """
	height_total = height_range_[1] - height_range_[0]
	bin_width = height_total./num_channel
	height_slices_map = defaultdict(np.array)	
	# PLACEHOLDERS
	x_points = points[:, 0]
	y_points = points[:, 1]
    	z_points = points[:, 2]
	r_points = points[:, 3]

    # FILTER - To return only indices of points within desired cube
    # Three filters for: Front-to-back, side-to-side, and height ranges
    # Note left side is positive y axis in LIDAR coordinates
	f_filt = l_and((x_points > fwd_range[0]), (x_points < fwd_range[1]))
    	s_filt = l_and((y_points > side_range[0]), (y_points < side_range[1]))
    	filtered = l_and(f_filt, s_filt)
    	indices = np.argwhere(filtered).flatten()

    # KEEPERS
    	x_points = x_points[indices]
    	y_points = y_points[indices]
    	z_points = z_points[indices]
    # Keep reflectance/intensity information
	r_points = r_points[indices]

    # CONVERT TO TOP VIEW Velodyne coordinates FL 
    	y_top = (y_points / res).astype(np.int32)  # x axis is -y in LIDAR
    	x_top = (x_points / res).astype(np.int32)  # y axis is -x in LIDAR

    # CLIP HEIGHT VALUES - to between min and max heights
    	clipped_height = np.clip(a=z_points,
                           a_min=height_range[0],
                           a_max=height_range[1])

    # INITIALIZE EMPTY ARRAY - of the dimensions we want
    	x_max = 1 + int((side_range[1] - side_range[0]) / res)
    	y_max = 1 + int((fwd_range[1] - fwd_range[0]) / res)
    	top = np.zeros([y_max, x_max], dtype=np.uint8)

    # FILL PIXEL VALUES IN IMAGE ARRAY
    # pixel_value is height channel
    	# top[y_top, x_top] = clipped_height
	if not has_reflectance:
	    r_points = None 
	    
	return top, y_top, x_top, clipped_height, r_points 

##---------------------------------------------------------------------------------------
## Define "Backward" transformation Point Cloud to 2D view
##---------------------------------------------------------------------------------------
if __name__ == "__main__":
	return
