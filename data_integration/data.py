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
		bag = Bag(self._file_path, 'r')
		self._topics = bag.get_type_and_topic_info()[1].keys()
	
	def read_images():
		image_raw = '/image_raw'

		self.images = bag.read_messages(topics=[image_raw])
		self.images_count = bag.get_message_count(topic_filters=[image_raw])
		return self

	def read_velo():
		velodyne_points = '/velodyne_points'
		self.lidar = bag.read_messages(topics=[velodyne_points]) 
		self.lidar_count = bag.get_message_count(topic_filters=[velodyne_points])
		return self
	
	def read_obs_gps():
		"""
		For challenge_1 only one obstacle detection is required
		"""
		obs1_gps_fix = '/obs1/gps/fix'
		self.obs_gps_fix = bag.read_messages(topics=[obs1_gps_fix])		
		self.obs_gps_fix_count = bag.read_message_count(topic_filters=[obs1_gps_fix])
	
		obs1_gps_rtkfix = '/obs1/gps/rtkfix'
		self.obs_gps_rtkfix = bag.read_messages(topics=[obs1_gps_rtkfix])
		self.obs_gps_rtkfix_count = bag.read_message_count(topic_filters=[obs1_gps_rtkfix])

		obs1_gps_time = '/obs1/gps/time'
		self.obs_gps_time = bag.read_messages(topics=[obs1_gps_time])
		self.obs_gps_time_count = bag.read_messages_count(topics=[obs1_gps_time])
		return self
	
	def read_gps():
		"""
		Capture vehicle?
		"""
		gps_fix = '/gps/fix'
		self.gps_fix = bag.read_messages(topics=[gps_fix])		
		self.gps_fix_count = bag.read_message_count(topic_filters=[gps_fix])
	
		gps_rtkfix = '/gps/rtkfix'
		self.gps_rtkfix = bag.read_messages(topics=[gps_rtkfix])
		self.gps_rtkfix_count = bag.read_message_count(topic_filters=[gps_rtkfix])

		gps_time = '/gps/time'
		self.gps_time = bag.read_messages(topics=[gps_time])
		self.gps_time_count = bag.read_messages_count(topics=[gps_time])
		return self
	
	def read_radar():
		"""
		"""
		radar_points = '/radar/points'
		self.radar_points = bag.read_messages(topics=[radar_points]) 
		self.radar_points_count = bag.get_message_count(topic_filters=[radar_points])
	
		radar_range = '/radar/range'
		self.radar_range = bag.read_messages(topics=[radar_range]) 
		self.radar_range_count = bag.get_message_count(topic_filters=[radar_range])

		radar_track = '/radar/track'
		self.radar_track = bag.read_messages(topics=[radar_track])
		self.radar_track_count = bag.get_message_count(radar_track)
		return self

	def lidar_to_pc(self, lidar_msg):
		"""
		Parameters
		----------
		----------
		"""
		return np.array(list(pc2.read_points(lidar_msg)))
		
		
#	def _next(self):

		
