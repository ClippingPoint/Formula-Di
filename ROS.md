## First ROS bag

What is [ROS bag](http://wiki.ros.org/Bags)?

Copying _Didi Challenge_ .bag files from your host(mac) to docker container


  Check your container names
```bash
  docker ps -l
```

  Copy files
```bash
  docker cp ~/some_folder/Didi-Training-Release-1/approach_1.bag  your_container_name:/approach_1.bag
```

_Approcha_1.bag_ size is around 500 MB, which makes it is easier to handle.

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


Example: Visualize Velodyne data

 Display -> PointCloud2 -> Topic -> /velodyne_points

  Topic names can be found from 

  ```bash
    rosbag play -l <your_bagfile>
  ```

  In new terminal, go to dataset folder

  ```bash
    rosbag play -l 5mph.bag # -l stands for loop. it will play it in loop
  ```

### Find data structure
  
  ```bash
    rostopic type <topic_name> | rosmsg show
    rostopic type /image_raw | rosmsg show
    rostopic echo -c /image_raw
  ```

  Other useful command

  rqt_graph

  rqt_bag


### Catkin

Dependencies: CMAKE, GCC/build-essential

~~Catkin is required by Velodyne driver~~

### Visualization

 * Install ros indigo rviz

```bash
  sudo apt-get install ros-indigo-rviz
```

## RViz

[Sample RViz plugin for visualizing Didi Data](https://github.com/jokla/didi_challenge_ros)

[Udacity ROS launch file plug-in for visualizing ROS bag data](https://github.com/udacity/self-driving-car/tree/master/datasets/udacity_launch)

## Core ROS concepts and Components

[BaseLink and Robot Setup](http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF)


"Baselink" robot (Udacity Lincoln MKZ) setup, can be used to contrust TF?

[Udacity MKZ URDF mesh](https://bitbucket.org/DataspeedInc/dbw_mkz_ros/src/0ee2d85ecbe101dca33316ed0855089e2c668707/dbw_mkz_description/urdf/mkz.urdf.xacro?at=default&fileviewer=file-view-default)

Ideas: Use URDF and Gazebo?

[Static Transform Publisher](http://wiki.ros.org/tf)

### TF/TF2

Coordinate Frames and Transformation

#### TF package to manage transfer matrices between frames

[TF transformations](http://wiki.ros.org/tf/Overview/Transformations)

[How to transform a pose](http://answers.ros.org/question/215656/how-to-transform-a-pose/)

[Tf Using python](http://wiki.ros.org/tf/TfUsingPython)

### Robot Setup

## ROS + TensorFlow

Test MNIST in ROS
[Tensorflow in ROS](https://github.com/shunchan0677/Tensorflow_in_ROS/blob/master/tensorflow_in_ros_mnist.py)

# Related Robotics Concepts

Quaterion

# References

[ROS Indigo Cheatsheet](https://w3.cs.jmu.edu/spragunr/CS354_F15/handouts/ROSCheatsheet.pdf)

[Creating and Playing rosbag file (Hokuyo Lidar)](http://yasirkiani.blogspot.com/2015/03/creating-and-playing-rosbag-file.html)

[How to visualize Lidar and Radar data in RViz](https://discussions.udacity.com/t/how-to-visualize-lidar-and-radar-data-in-rviz/232711)

Physical sensor setup:

[Round 1 questions about dataset and evaluation](https://discussions.udacity.com/t/round-1-questions-about-dataset-and-evaluation/231931/8)

# Hardware List

## Drivers

### Velodyne Lidar

[Velodyne HDL-32E](http://wiki.ros.org/velodyne/Tutorials/Getting%20Started%20with%20the%20HDL-32E)

```bash
  sudo apt-get install ros-indigo-velodyne
```

TODO:

  * Create complete DockerFile
