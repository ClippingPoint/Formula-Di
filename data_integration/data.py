from rosbag import Bag
import sensor_msgs.point_cloud2 as pc2
import numpy as np



class data:
	"""
	TODO: using defaultdict(list)? to reduce duplicated list
		Feature: Filter topic lists
		Feature: Seperate obstacle prefix across differnt obstacles
		There is only one obstacle for challenge1
		e.g. /obs1, /obs2/, ...
	"""
	def __init__(self, file_path):
		"""
		Parameters
		----------
		file_path:
		"""
		self._file_path = file_path 
		self.read_rosbag()
		self.filter_topics = ['/image_raw',
				'/velodyne_points',
				'/obs1/gps/fix']
	
	def read_rosbag(self):	
		"""
		Parameers
		---------
		---------
		topics: ROS topic can be found using `rosbag info some.bag`
		eg. /velodyne_points
		"""
		self._bag = Bag(self._file_path, 'r')
		self._topics = self._bag.get_type_and_topic_info()[1].keys()
		return self
	
	def read_images(self):
		image_raw = '/image_raw'

		self.images = self._bag.read_messages(topics=[image_raw])
		self.images_count = self._bag.get_message_count(topic_filters=[image_raw])
		return self

	def read_velo_points(self):
		velodyne_points = '/velodyne_points'
		self.lidar = self._bag.read_messages(topics=[velodyne_points]) 
		self.lidar_count = self._bag.get_message_count(topic_filters=[velodyne_points])
		return self
	
	def read_obs_gps(self):
		"""
		For challenge_1 only one obstacle detection is required
		"""
		obs1_gps_fix = '/obs1/gps/fix'
		self.obs_gps_fix = self._bag.read_messages(topics=[obs1_gps_fix])		
		self.obs_gps_fix_count = self._bag.read_message_count(topic_filters=[obs1_gps_fix])
	
		obs1_gps_rtkfix = '/obs1/gps/rtkfix'
		self.obs_gps_rtkfix = self._bag.read_messages(topics=[obs1_gps_rtkfix])
		self.obs_gps_rtkfix_count = self._bag.read_message_count(topic_filters=[obs1_gps_rtkfix])

		obs1_gps_time = '/obs1/gps/time'
		self.obs_gps_time = self._bag.read_messages(topics=[obs1_gps_time])
		self.obs_gps_time_count = self._bag.read_messages_count(topics=[obs1_gps_time])
		return self
	
	def read_gps(self):
		"""
		Capture vehicle?
		"""
		gps_fix = '/gps/fix'
		self.gps_fix = self._bag.read_messages(topics=[gps_fix])		
		self.gps_fix_count = self._bag.read_message_count(topic_filters=[gps_fix])
	
		gps_rtkfix = '/gps/rtkfix'
		self.gps_rtkfix = self._bag.read_messages(topics=[gps_rtkfix])
		self.gps_rtkfix_count = self._bag.read_message_count(topic_filters=[gps_rtkfix])

		gps_time = '/gps/time'
		self.gps_time = self._bag.read_messages(topics=[gps_time])
		self.gps_time_count = self._bag.read_messages_count(topics=[gps_time])
		return self
	
	def read_radar(self):
		"""
		"""
		radar_points = '/radar/points'
		self.radar_points = self._bag.read_messages(topics=[radar_points]) 
		self.radar_points_count = self._bag.get_message_count(topic_filters=[radar_points])
	
		radar_range = '/radar/range'
		self.radar_range = self._bag.read_messages(topics=[radar_range]) 
		self.radar_range_count = self._bag.get_message_count(topic_filters=[radar_range])

		radar_track = '/radar/track'
		self.radar_track = self._bag.read_messages(topics=[radar_track])
		self.radar_track_count = self._bag.get_message_count(radar_track)
		return self

	def read_velo_packets(self):
		"""
		"""
		velodyne_packets = '/velodyne_packets'
		self.lidar_packets = self._bag.read_messages(topics=[velodyne_packets])
		self.lidar_packets_count = self._bag.get_message_count(velodyne_packets)
		return self

	def lidar_to_pc(self, lidar_msg):
		"""
		Parameters
		----------
		----------
		"""
		return np.array(list(pc2.read_points(lidar_msg)))
		
		
#	def _next(self):

		
