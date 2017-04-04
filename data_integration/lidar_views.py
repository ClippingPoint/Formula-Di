from PIL import Image
import numpy as np
import sys

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

def save_to_image(im_array, output_image_path):
	Image.fromarray(im_array).save(output_image_path)
