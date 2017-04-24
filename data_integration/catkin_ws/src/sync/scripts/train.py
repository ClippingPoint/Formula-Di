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
get_


#for iter in range(msg_count):

###---------------------------------------------
# Export
###---------------------------------------------



