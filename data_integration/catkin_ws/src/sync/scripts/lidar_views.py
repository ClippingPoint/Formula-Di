# Avoid namespace collision
from PIL import Image as PILImage
import numpy as np
import sys
import sensor_msgs.point_cloud2 as pc2

"""
To image plane coordinates, mostly for debugging.

Required feature: 1. velopoint_cloud coordinate to display image coordinates
"""

def pc2_msg_to_np(lidar_msg):
	return np.array(list(pc2.read_points(lidar_msg)))

def scale_to_255(a, min_, max_, dtype=np.uint8):
	"""
	double or float?
	"""
	return (((a - min_) / float(max_ - min_)) * 255).astype(dtype)

def point_cloud_to_top(points, res=0.1, side_range=(-10., 10.), fwd_range=(-10., 10.), height_range=(-2, 2),):
	l_and = lambda *x: np.logical_and.reduce(x)
	l_or = lambda *x: np.logical_or.reduce(x)
	"""
	Create an 2D birds eye view of (lidar) point cloud data
	http://ronny.rest/tutorials/module/pointclouds_01/point_cloud_birdseye/
	Parameters:
	-----------
	points: (Nx1 numpy array)
	x,y,z_range: (float, float) tuple
	res: (float) Resolution (pixel per metre) to use. Each output pixel
	will represent an square region res x res in size
	postive x: vehicle forward
	postive y: vehicle left
	postive z: vehilce up
	TODO: intensity filter
	-----------
	retur:
	-----------
	"""
	# EXTRACT THE POINTS FOR EACH AXIS
    	x_points = points[:, 0]
	y_points = points[:, 1]
    	z_points = points[:, 2]

    # FILTER - To return only indices of points within desired cube
    # Three filters for: Front-to-back, side-to-side, and height ranges
    # Note left side is positive y axis in LIDAR coordinates
#    	f_filt = np.logical_and((x_points > fwd_range[0]), (x_points < fwd_range[1]))
	f_filt = l_and((x_points > fwd_range[0]), (x_points < fwd_range[1]))
#    	s_filt = np.logical_and((y_points > -side_range[1]), (y_points < -side_range[0]))
    	s_filt = l_and((y_points > -side_range[1]), (y_points < -side_range[0]))
    	filtered = l_and(f_filt, s_filt)
    	indices = np.argwhere(filtered).flatten()

    # KEEPERS
    	x_points = x_points[indices]
    	y_points = y_points[indices]
    	z_points = z_points[indices]

    # CONVERT TO PIXEL POSITION VALUES - Based on resolution
    	x_img = (-y_points / res).astype(np.int32)  # x axis is -y in LIDAR
    	y_img = (-x_points / res).astype(np.int32)  # y axis is -x in LIDAR

    # SHIFT PIXELS TO HAVE MINIMUM BE (0,0)
    # floor & ceil used to prevent anything being rounded to below 0 after shift
    	x_img -= int(np.floor(side_range[0] / res))
    	y_img += int(np.ceil(fwd_range[1] / res))

    # CLIP HEIGHT VALUES - to between min and max heights
    	pixel_values = np.clip(a=z_points,
                           a_min=height_range[0],
                           a_max=height_range[1])


    # RESCALE THE HEIGHT VALUES - to be between the range 0-255
    	pixel_values = scale_to_255(pixel_values,
                                min_=height_range[0],
                                max_=height_range[1])

    # INITIALIZE EMPTY ARRAY - of the dimensions we want
    	x_max = 1 + int((side_range[1] - side_range[0]) / res)
    	y_max = 1 + int((fwd_range[1] - fwd_range[0]) / res)
    	im = np.zeros([y_max, x_max], dtype=np.uint8)

    # FILL PIXEL VALUES IN IMAGE ARRAY
    	im[y_img, x_img] = pixel_values

    	return im
# im2 = Image.framearray()
def point_cloud_to_2d_front_view(points,
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
        h_res: (float)
            horizontal resolution of the lidar sensor used.
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

    # PROJECT INTO IMAGE COORDINATES
    x_img = np.arctan2(-y_lidar, x_lidar)/ h_res_rad
    y_img = np.arctan2(z_lidar, d_lidar)/ v_res_rad

    # SHIFT COORDINATES TO MAKE 0,0 THE MINIMUM
    x_min = -360.0 / h_res / 2  # Theoretical min x value based on sensor specs
    x_img -= x_min              # Shift
    x_max = 360.0 / h_res       # Theoretical max x value after shifting

    y_min = v_fov[0] / v_res    # theoretical min y value based on sensor specs
    y_img -= y_min              # Shift
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

    im = np.zeros([y_max, x_max], dtype=np.uint8)
    # FILL PIXEL VALUES IN IMAGE ARRAY
    im[y_img, x_img] = pixel_values

    return im

# ==============================================================================
#                                                        POINT_CLOUD_TO_PANORAMA
# ==============================================================================
def point_cloud_to_panorama(points,
                            v_res=0.42,
                            h_res = 0.35,
                            v_fov = (-24.9, 2.0),
                            d_range = (0,100),
                            y_fudge=3
                            ):
    """ Takes point cloud data as input and creates a 360 degree panoramic
        image, returned as a numpy array.

    Args:
        points: (np array)
            The numpy array containing the point cloud. .
            The shape should be at least Nx3 (allowing for more columns)
            - Where N is the number of points, and
            - each point is specified by at least 3 values (x, y, z)
        v_res: (float)
            vertical angular resolution in degrees. This will influence the
            height of the output image.
        h_res: (float)
            horizontal angular resolution in degrees. This will influence
            the width of the output image.
        v_fov: (tuple of two floats)
            Field of view in degrees (-min_negative_angle, max_positive_angle)
        d_range: (tuple of two floats) (default = (0,100))
            Used for clipping distance values to be within a min and max range.
        y_fudge: (float)
            A hacky fudge factor to use if the theoretical calculations of
            vertical image height do not match the actual data.
    Returns:
        A numpy array representing a 360 degree panoramic image of the point
        cloud.
    """
    # Projecting to 2D
    x_points = points[:, 0]
    y_points = points[:, 1]
    z_points = points[:, 2]
    r_points = points[:, 3]
    d_points = np.sqrt(x_points ** 2 + y_points ** 2)  # map distance relative to origin
    #d_points = np.sqrt(x_points**2 + y_points**2 + z_points**2) # abs distance

    # We use map distance, because otherwise it would not project onto a cylinder,
    # instead, it would map onto a segment of slice of a sphere.

    # RESOLUTION AND FIELD OF VIEW SETTINGS
    v_fov_total = -v_fov[0] + v_fov[1]

    # CONVERT TO RADIANS
    v_res_rad = v_res * (np.pi / 180)
    h_res_rad = h_res * (np.pi / 180)

    # MAPPING TO CYLINDER
    x_img = np.arctan2(y_points, x_points) / h_res_rad
    y_img = -(np.arctan2(z_points, d_points) / v_res_rad)

    # THEORETICAL MAX HEIGHT FOR IMAGE
    d_plane = (v_fov_total/v_res) / (v_fov_total* (np.pi / 180))
    h_below = d_plane * np.tan(-v_fov[0]* (np.pi / 180))
    h_above = d_plane * np.tan(v_fov[1] * (np.pi / 180))
    y_max = int(np.ceil(h_below+h_above + y_fudge))

    # SHIFT COORDINATES TO MAKE 0,0 THE MINIMUM
    x_min = -360.0 / h_res / 2
    x_img = np.trunc(-x_img - x_min).astype(np.int32)
    x_max = int(np.ceil(360.0 / h_res))

    y_min = -((v_fov[1] / v_res) + y_fudge)
    y_img = np.trunc(y_img - y_min).astype(np.int32)

    # CLIP DISTANCES
    d_points = np.clip(d_points, a_min=d_range[0], a_max=d_range[1])

    # CONVERT TO IMAGE ARRAY
    img = np.zeros([y_max + 1, x_max + 1], dtype=np.uint8)
    img[y_img, x_img] = scale_to_255(d_points, min=d_range[0], max=d_range[1])

    return img

def save_to_image(im_array, output_image_path):
	PILImage.fromarray(im_array).save(output_image_path)
