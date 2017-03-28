## First ROS bag

What is [ROS bag](http://wiki.ros.org/Bags)?

Copying <em>Didi Challenge</em> .bag files from your host(mac) to docker container


  Check your container names
```bash
  docker ps -l
```

  Copy files
```bash
  docker cp ~/some_folder/Didi-Training-Release-1/approach_1.bag  your_container_name:/approach_1.bag
```

<em>Approcha_1.bag</em> size is around 500 MB, which makes it is easier to handle.

  "Play"

```bash
  rosbag info approach_1.bag
```

![Bag Info](https://bytebucket.org/Khanhh/formual-di/raw/bafb977b72fb1d15d32ca91c48dd149916556d51/setup/baginfo.png?token=0629ae6ebfec8672e7ad7c9505a57022b751c00f)

```bash
  rosbag play approach_1.bag
```

Hit space to stop then open another docker terminal running ros:indigo in order to check current broadcasting topics

```bash
  rostopic list
```

![Bag topic list](https://bytebucket.org/Khanhh/formual-di/raw/80b773c13c8866dc41abcd798b31f0e10fede9cb/setup/bag_topic_list.png?token=648419427493c8e31fedde4d7c749a13b4aa4d8f)

### Visualization

 * Install ros indigo rviz

```bash
  sudo apt-get install ros-indigo-rviz
```

## RViz

[Sample RViz plugin for visualizing Didi Data](https://github.com/jokla/didi_challenge_ros)

## Core ROS concepts and Components

[BaseLink and Robot Setup](http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF)

[Static Transform Publisher](http://wiki.ros.org/tf)

### TF/TF2

Coordinate Frames and Transformation

### Robot Setup

## ROS + TensorFlow

Test MNIST in ROS
[Tensorflow in ROS](https://github.com/shunchan0677/Tensorflow_in_ROS/blob/master/tensorflow_in_ros_mnist.py)

# Related Robotics Concepts

Quaterion

# References

[ROS Indigo Cheatsheet](https://w3.cs.jmu.edu/spragunr/CS354_F15/handouts/ROSCheatsheet.pdf)

[Creating and Playing rosbag file (Hokuyo Lidar)](http://yasirkiani.blogspot.com/2015/03/creating-and-playing-rosbag-file.html)

# Hardware List

Velodyne Lidar




