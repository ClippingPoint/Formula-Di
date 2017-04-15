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

class Storage():
    def __init__(self, options=0):
	"""
	Default uses pandas
	"""
	if options == 1:
	    pass
	elif options == 2:
	    pass
	self.lidar_dict = defaultdict(list)
	self.camera_dict = defaultdict(list)
#    def pds_lidar_dict(msg, ):

# Frame by frame
    def _lidar_to_dict(self, msg):
	self.lidar_dict["timestamp"].append(msg.header.stamp.to_nsec())
	self.lidar_dict["lidar_msg"].append(msg)

    def _image_to_dict(self, msg):
	self.camera_dict["timestamp"].append(msg.header.stamp.to_nsec())
	self.camera_dict["image_msg"].append(msg)

# Offline
    def save_lidar_raw(self, file_path='./lidar_raw.p', file_format='pickle'):
	"""
	Save unsynced data
	TODO: Parameterize file_path
    	"""
	lidar_cols = ["timestamp", "lidar_msg"]
	lidar_df = pd.DataFrame(data=self.lidar_dict, columns=lidar_cols)
	if file_format == 'pickle':
	    lidar_df.to_pickle(file_path)
	elif file_format == 'hdf5':
	    lidar_df.to_hdf(file_path)
	return lidar_df

    def save_image_raw(self, file_path='./camera_raw.p', file_format='pickle'):
	"""
	Save unsynced data
	"""
	camera_cols = ["timestamp", "image_msg"]
	camera_df = pd.DataFrame(data=self.camera_dict, columns=camera_cols)
	if file_format == 'pickle':
	    camera_df.to_pickle(file_path)
	elif file_format == 'hdf5':
	    camera_df.to_hdf(file_path)
	return camera_df

    def _interpolate_to_camera(camera_df, other_dfs, filter_cols=[]):
	if not isinstance(other_dfs, list):
	    other_dfs = [other_dfs]
	if not isinstance(camera_df.index, pd.DatetimeIndex):
	    rospy.logerr("Error: Camera dataframe needs to be indexed by timestamp for interpolation")
	    return pd.DataFrame()
	for o in other_dfs:
	# Convert from unix timestamp
	    o['timestamp'] = pd.to_datetime(o['time'])
	    o.set_index(['timestamp'], inplace=True)
	
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
