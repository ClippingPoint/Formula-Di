"""
    data IO
"""

# Option to use other db?
import pandas as pd
import numpy as np
from collections import defaultdict
import functools
import rospy

# TODO: save lidar point cloud
# TODO: unix time stamp to datetime

class Storage():
    def __init__(self, options=3):
	"""
	Default uses pandas
	"""
	if options == 1:
	    pass
	elif options == 2:
	    pass
	# Raw pickle
	elif options == 3:
	    self.lidar_dict = defaultdict(list)
	    self.camera_dict = defaultdict(list)
	elif options == 0:
	# Naive interpolate
	    self.interp_dict = defaultdict(list)

    def _navie_frame_to_dict(self, image_msg, lidar_msg):
	self.interp_dict["timestamp"].append(image_msg.header.stamp.to_nsec())
	self.interp_dict["image_msg"].append(image_msg)
	self.interp_dict["lidar_msg"].append(lidar_msg)
# Frame by frame
    def _lidar_to_dict(self, msg):
#	print(msg)
# 	rospy.loginfo(msg)
	# _msg = ("timestamp", msg.header.stamp.to_nsec())
	self.lidar_dict["timestamp"].append(msg.header.stamp.to_nsec())
	#self.lidar_dict["timestamp"].append(_msg)
	#_msg = ("lidar_msg", msg)
	self.lidar_dict["lidar_msg"].append(msg)

    def _image_to_dict(self, msg):
	self.camera_dict["timestamp"].append(msg.header.stamp.to_nsec())
	#self.camera_dict["timestamp"].append(_msg)
	# _msg = ("image_msg", msg)
	self.camera_dict["image_msg"].append(msg)

# Offline
    def save_lidar_raw(self, file_path='./lidar_raw.p', file_format='pickle'):
	"""
	Save unsynced data
	TODO: Parameterize file_path
    	"""
	lidar_cols = ["timestamp", "lidar_msg"]
	lidar_df = pd.DataFrame(data=self.lidar_dict, columns=lidar_cols)
        lidar_df.set_index(['timestamp'], inplace=True)
	if file_format == 'pickle':
	    lidar_df.to_pickle(file_path)
	elif file_format == 'hdf5':
	    lidar_df.to_hdf(file_path)
	return lidar_df

    def save_image_raw(self, file_path='./camera_raw.p', file_format='pickle'):
	"""
	Save unsynced timeindex data
	"""
	camera_cols = ["timestamp", "image_msg"]
	camera_df = pd.DataFrame(data=self.camera_dict, columns=camera_cols)
        camera_df.set_index(['timestamp'], inplace=True)

	if file_format == 'pickle':
	    #camera_df.to_pickle(file_path)
	    camera_df.to_pickle(file_path)
	elif file_format == 'hdf5':
	    # camera_df.to_hdf(file_path)
	    camera_df.to_hdf(file_path)
	return camera_df
 
    def save_camera_df_index(self, file_path='./camera_df_index.p', file_format='pickle'):
	"""
	Save time index for cross table interpolation
	"""
	# To index df
	camera_cols = ["timestamp", "image_msg"]
	camera_df = pd.DataFrame(data=self.camera_dict, columns=camera_cols)

  	camera_df['timestamp'] = pd.to_datetime(camera_df['timestamp'])
        camera_df.set_index(['timestamp'], inplace=True)
        camera_df.index.rename('index', inplace=True)

        camera_index_df = pd.DataFrame(index=camera_df.index)
	if file_format == 'pickle':
	    #camera_df.to_pickle(file_path)
	    camera_index_df.to_pickle(file_path)
	elif file_format == 'hdf5':
	    # camera_df.to_hdf(file_path)
	    camera_index_df.to_hdf(file_path)
	return camera_df

    def _naive_save_interp_df(self, file_path='./interp_df_index.p', file_format='pickle'):
	"""
	Interpolate other data based on image message timestamp
	"""
	data_cols = ["timestamp", "image_msg", "lidar_msg"]
	interp_df = pd.DataFrame(data=self.interp_dict, column=data_cols)
	if file_format == 'pickle':
	    #camera_df.to_pickle(file_path)
	    interp_df.to_pickle(file_path)
	elif file_format == 'hdf5':
	    # camera_df.to_hdf(file_path)
	    interp_df.to_hdf(file_path)
	return interp_df

    def _interpolate_to_camera(self, camera_df, other_dfs, filter_cols=[]):
	if not isinstance(other_dfs, list):
	    other_dfs = [other_dfs]
	if not isinstance(camera_df.index, pd.DatetimeIndex):
	    #rospy.logerr("Error: Camera dataframe needs to be indexed by timestamp for interpolation")
	    print("Error, no DatetimeIndex")
	    return pd.DataFrame()
	for o in other_dfs:
	# Convert from unix timestamp
	    o['timestamp'] = pd.to_datetime(o['timestamp'])
	    o.set_index(['timestamp'], inplace=True)
	    o.index.rename('index', inplace=True)
	
	merged = functools.reduce(lambda left, right: pd.merge(left, right, how='outer', 
		left_index=True, right_index=True), [camera_df] + other_dfs)
	merged.interpolate(method='time', inplace=True, limit=100, limit_direction='both')

	filtered = merged.loc[camera_df.index]
	filtered.fillna(0, 0, inplace=True)
	# Convert to unix timestamp
	filtered['timestamp'] = filtered.index.astype('int')
	
	if filter_cols:
	    if not 'timestamp' in filter_cols:
		filter_cols += ['timestamp'] 
	    filtered = filtered[filter_cols]

	return filtered
