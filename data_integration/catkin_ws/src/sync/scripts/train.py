###---------------------------------------------
# Import
###---------------------------------------------
from tracklet_io import *
from image_proc import *
from syncer import *
from lidar_mapping import *
# from collections import defaultdict

xml_path = '/root/tracklet_labels.xml'
gt_obs_list = Xml_Reader().parse_xml_tracklet(xml_path)

# d = defaultdict(list)
# d[xml_path].append(obs_list)
image_raw_path = '/root/catkin_ws/camera_raw.p'
lidar_raw_path = '/root/catkin_ws/lidar_raw.p'

# Contains all images
syncer = Syncer(image_raw_path, lidar_raw_path)
msg_count = syncer.get_lidar_message_count()
#print(msg_count)

lidar_pc, image_arr = syncer.sync_to_lidar_frame(10)

print(lidar_pc.shape)
print(image_arr.shape)

#for iter in range(msg_count):
###---------------------------------------------
# Seems there are different physical parameters are used according to 
# http://ronny.rest/blog/post_2017_03_25_lidar_to_2d/ 
# 20Hz?
###---------------------------------------------
front_depth = point_cloud_to_front_view(
			lidar_pc, 
			v_res=1.33, 
			h_res=1, 
			v_fov=(-24.0, 2.0),
			val="depth",
			y_fudge=3.0)

front_r = point_cloud_to_front_view(
			lidar_pc, 
			v_res=1.33, 
			h_res=1, 
			v_fov=(-24.0, 2.0),
			val="reflectance",
			y_fudge=3.0)

front_height = point_cloud_to_front_view(
			lidar_pc, 
			v_res=1.33, 
			h_res=1, 
			v_fov=(-24.0, 2.0),
			val="height",
			y_fudge=3.0)

top_pc, y_top, x_top, c_height, r = point_cloud_to_top(lidar_pc,
			    res=0.1,
			    side_range=(-10.0, 10.0),
			    fwd_range=(-10., 10.),
			    height_range=(-2, 2),
			    has_reflectance=True)



height_sliced_map = get_top_sliced_height_maps(
				top_pc,
				y_top,
				x_top,
				c_height,
				num_channel=14,
				height_range=(-2, 2))
				

density_map = get_density_map(top_pc, y_top, x_top, c_height)
reflectance_map = get_reflectance_map(top_pc, y_top, x_top, r)
###---------------------------------------------
# Export
###---------------------------------------------

