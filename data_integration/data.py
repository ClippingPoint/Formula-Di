from rosbag import Bag
import sensor_msgs.point_cloud2 as pc2
import numpy as np

class data:
	"""
	"""
	def __init__(self, file_path):
		"""
		Parameters
		----------
		file_path:
		"""
		self._file_path = file_path 
		self.read_rosbag()
	
	def read_rosbag(self):	
		"""
		Parameers
		---------
		---------
		topics: ROS topic can be found using `rosbag info some.bag`
		eg. /velodyne_points
		"""
		bag = Bag(self._file_path, 'r')
		self._topics = bag.get_type_and_topic_info()[1].keys()

		image_raw = '/image_raw'
		velodyne_points = '/velodyne_points'

		self.lidar = bag.read_messages(topics=[velodyne_points]) 
		self.lidar_count = bag.get_message_count(topic_filters=[velodyne_points])

		self.images = bag.read_messages(topics=[image_raw])
		self.images_count = bag.get_message_count(topic_filters=[image_raw])
		return self
	def lidar_to_pc(self, lidar_msg):
		"""
		Parameters
		----------
		----------
		"""
		return np.array(list(pc2.read_points(lidar_msg)))
		
		
#	def _next(self):

		
