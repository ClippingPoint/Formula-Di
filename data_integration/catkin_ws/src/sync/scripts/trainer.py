import pandas as pd
import numpy as np
from lidar_views import *
from image_proc import *

# TODO: read groud truth

class Trainer:
    def __init__(self, image_msg_df_path, lidar_msg_df_path):
        """
    	Offline trainer
        """
	# Read pickle data
	#self.image_df = image_message_to_cv2(image_msg)
	#self.lidar_df = lidar_msg
	self.image_df = pd.read_pickle(image_msg_df_path)
	self.lidar_df = pd.read_pickle(lidar_msg_df_path)
	self.img_proc = Image_Proc()

  	self.image_df['timestamp'] = pd.to_datetime(self.image_df['timestamp'])
	self.image_df.set_index(['timestamp'], inplace=True)

	self.lidar_df['timestamp'] = pd.to_datetime(self.lidar_df['timestamp'])
	self.lidar_df.set_index(['timestamp'], inplace=True)
	return None
    
    def min_time_diff(self, d_index, pivot):
#http://stackoverflow.com/questions/34929261/get-value-form-pandas-df-column-that-is-closest-to-datetime64
	"""
	return nearest time index of d_index
	"""
	l = list(abs(d_index - pivot))
	return l.index(min(l))
    def get_image_df_by_id(self, frame_id):
	"""
	return converted np cv2 array
	"""
	return self.img_proc.image_message_to_cv2(self.image_df.loc[self.image_df.index[frame_id]]['image_msg'])

    def get_pc_sync_df_by_image_id(self, image_frame_id):
	lidar_frame_id = self.min_time_diff(self.lidar_df.index, self.image_df.index[image_frame_id])
	pc2_msg = self.lidar_df.loc[self.lidar_df.index[lidar_frame_id]]['lidar_msg']
	return pc2_msg_to_np(pc2_msg)
    def sync(self, image_frame_id):
	"""
	Extract synced single frame, lidar, image and other data
	All sync to image_frame_id
	"""	 
	# TODO: remove set_index after rewrite db.py
#	print(self.image_df.ix[0:3])
	#print(pd.Timedelta(milliseconds=120))
	lidar_pc = self.get_pc_sync_df_by_image_id(image_frame_id)
	image_arr = self.get_image_df_by_id(image_frame_id)

	return lidar_pc, image_arr
    def train(self):
	image_frame_id = 10
	NotImplementedError
	
	
image_raw_path = '/root/catkin_ws/camera_raw.p'
lidar_raw_path = '/root/catkin_ws/lidar_raw.p'

Trainer(image_raw_path, lidar_raw_path).preprocessor()
