#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2008, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
#
# Revision $Id$

## Simple talker demo that listens to std_msgs/Strings published 
## to the 'velodyne_points' topic
import sys
import numpy as np

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud2
from sensor_msgs.msg import Image
import sensor_msgs.point_cloud2 as pc2

from ros_proc import *
from db import *

# start_time = time.time()
# end_time = time.time()

# TODO: Record last a few frames of data then extroploate?
# TODO: Teach/train mode vs real time testing predictio mode?
class Listener:
    def __init__(self, mode):
	"""
	When actual training, listener relies on bag files stops playing
	Then starts training
	"""
	self.velo_sub = rospy.Subscriber('/velodyne_points', PointCloud2, self.lidar_callback)
    	self.image_sub = rospy.Subscriber('/image_raw', Image, self.image_callback)
	self._verbose = False
#	self._last_lidar_frame = None
#	self._last_timestamp = None
    	self.storage = Storage()
	if mode == 'train':
	    self.action = self._train_hook
	elif mode == 'predict':
	    self.action = self._predict_hook
#	self.yes

    def lidar_callback(self, lidar_msg):
    # TODO: get message count
    # print(lidar_msg.header)
#	point_cloud = np.array(list(pc2.read_points(lidar_msg)))
	if self._verbose:
	    rospy.loginfo(point_cloud)
	self.storage._lidar_to_dict(lidar_msg)

#	self.action(lidar_msg)

    def image_callback(self, image_msg):
	if self._verbose:
	    rospy.loginfo(image_msg)
	self.storage._image_to_dict(image_msg)

#	self.action(image_msg)

    def _train_hook(self, msg):
	NotImplementedError

    def _predict_hook():
	NotImplementedError

    def on_shutdown(self):
	# TODO:save numpy/dict to db or file?
	# Use with roslaunch?
	rospy.loginfo("I AM shutting down!!")
	# Synchronize then save to pickle file
	#self.storage.lidar_dict
	self.storage.save_lidar_raw()
	self.storage.save_image_raw()


def main(args):
    # TODO: parameterize mode, compatiable to command line
    listener = Listener(mode='train')
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)
    rospy.on_shutdown(listener.on_shutdown)
    try: 
    	# spin() simply keeps python from exiting until this node is stopped
	rospy.spin()
    except KeyboardInterrupt:
	rospy.loginfo("Shutting down")


main(sys.argv)
