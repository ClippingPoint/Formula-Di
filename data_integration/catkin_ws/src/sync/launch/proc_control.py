#!/usr/bin/env python
"""
import rospy
import subprocess
import signal

child1 = subprocess.Popen(["roslaunch", "sync_raw.launch"])
child2 = subprocess.Popen(["roslaunch", "rosbag_play.launch"])

child1.wait()
child2.send_signal(signal.SIGINT)
"""

import roslaunch

package = "sync"
executable = "listener.py"

launch = roslaunch.scriptapi.ROSLaunc()
launch.start()

process = launch.launch(node)

