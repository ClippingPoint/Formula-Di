## ROS concepts
    Service invocation
Node -----------------> Node
---------> topic ------>
Publication     Subscription

[ROS concepts wiki](http://wiki.ros.org/ROS/Concepts)

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

## Python/C++ in ROS

  Step by step
  
  1. Install and create catkin space
    
    Install from prebuilt package

    ```bash
      sudo apt-get install ros-indigo-catkin
    ```

    [Create a catkin workspace](http://wiki.ros.org/catkin/Tutorials/create_a_workspace)

  2. Create a ROS package

    [Creating ROS Package](http://wiki.ros.org/catkin/Tutorials/CreatingPackage)

  3. [Writing Publisher Subscriber (python)](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)

### TroubleShoot

  * If you encounter package not found error, make sure you compile ROS package using _catkin_make_, after compilation, run devel/setup.bash in your catkin ROS package workspace to set up path env

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

[URDF](http://wiki.ros.org/urdf)

Ideas: Use URDF and Gazebo?

[Static Transform Publisher](http://wiki.ros.org/tf)

### TF/TF2

Coordinate Frames and Transformation

#### TF package to manage transfer matrices between frames

[TF transformations](http://wiki.ros.org/tf/Overview/Transformations)

[How to transform a pose](http://answers.ros.org/question/215656/how-to-transform-a-pose/)

[Tf Using python](http://wiki.ros.org/tf/TfUsingPython)

Sample or transform pose using Quaternion in ROS

[TF Baselink to GPS using position](https://github.com/didi-challenge-team-khodro/data_analysis/blob/master/src/data_discovery/src/tf_baselink_to_gps_using_position.cpp)

### Robot Setup

## ROS + TensorFlow

Test MNIST in ROS
[Tensorflow in ROS](https://github.com/shunchan0677/Tensorflow_in_ROS/blob/master/tensorflow_in_ros_mnist.py)

## ROS bag 

Reading Challenge ROS bag file

[ROS and ROS bags Part2](http://ronny.rest/blog/post_2017_03_30_ros2/)

Time synchronization

[ROS and ROS bag Part3](http://ronny.rest/blog/post_2017_03_30_ros3_and_lidar/)

## (Time) Synchronization

[Sync ROS bag timestamps with ROS system](http://answers.ros.org/question/123256/sync-ros-bag-timestamps-with-ros-system/)

[Message filter Time Synchronizer](http://wiki.ros.org/message_filters#Time_Synchronizer)

## Point Cloud

[How to combine a camera image and a laser point cloud to create a color point cloud](http://answers.ros.org/question/99211/how-to-combine-a-camera-image-and-a-laser-pointcloud-to-create-a-color-pointcloud/)

[Point Clouds and LiDAR module tutorial](http://ronny.rest/tutorials/module/pointclouds_01)

## ROSLaunch

What is [roslaunch](http://wiki.ros.org/roslaunch)

ROSlaunch is a tool for easily launching multiple ROS nodes locally and remotely via SSH, as well as setting parameters on the _Parameter Server_.

[Does a ROS launch start roscore when needed?](http://answers.ros.org/question/217107/does-a-roslaunch-start-roscore-when-needed/)

Yes

# Related Robotics Concepts

Quaterion

# References

[ROS Indigo Cheatsheet](https://w3.cs.jmu.edu/spragunr/CS354_F15/handouts/ROSCheatsheet.pdf)

[Creating and Playing rosbag file (Hokuyo Lidar)](http://yasirkiani.blogspot.com/2015/03/creating-and-playing-rosbag-file.html)

[How to visualize Lidar and Radar data in RViz](https://discussions.udacity.com/t/how-to-visualize-lidar-and-radar-data-in-rviz/232711)

Physical sensor setup:

[Round 1 questions about dataset and evaluation](https://discussions.udacity.com/t/round-1-questions-about-dataset-and-evaluation/231931/8)

Watch it!

Yousof Ebneddin

[Didi Challenge DataSet, transformation issues](https://www.youtube.com/watch?v=5JsO8ifppgA)

Watch it!

[How to visualize the training data for Didi challenge in ROS](https://www.youtube.com/watch?v=RVFpwMAeBOA)

# Hardware List

## Drivers

### Velodyne Lidar

[Velodyne HDL-32E](http://wiki.ros.org/velodyne/Tutorials/Getting%20Started%20with%20the%20HDL-32E)

[Velodyne VLP 16 User manual](http://velodynelidar.com/docs/manuals/VLP-16%20User%20Manual%20and%20Programming%20Guide%2063-9243%20Rev%20A.pdf)

```bash
  sudo apt-get install ros-indigo-velodyne
```

#### Velodyne ROS node

[Introduction of velodyne ros pipeline](http://www.cs.utexas.edu/~piyushk/courses/spr12/slides/Week6b-print.pdf)

[U Texas (Velodyne driver contributor) ROS pkg](https://github.com/austin-robot/utexas-art-ros-pkg)

Run ros nodelet convert recorded bag velodyne_packet to velodyne_points

```bash
  rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

[Velodyne_point_cloud wiki Example 2.1.4](http://wiki.ros.org/velodyne_pointcloud)

Then play rosbag

```bash
  rosbag play -l some.bag
```

Check rostopic list in different bash, we will see ```velodyne_pointcloud``` topic

[How to extract the data from the packets of velodyne hdl 32e](http://answers.ros.org/question/53499/how-to-extract-the-data-from-the-packets-of-velodyne-hdl-32e/)

[Convert velodyne scan to pointcloud2 from a rosbag](http://answers.ros.org/question/191972/convert-velodynescan-to-pointcloud2-from-a-rosbag-file/)

[Questions about velodyne point cloud package](http://answers.ros.org/question/188725/some-questions-about-velodyne_pointcloud-package/)

## ROS package

Software in ROS is organized in packages. A packages might contain ROS nodes, a ROS-independent library, a dataset, configuration files, a third-party piece of software,
or anything else that logically constitute a useful module.

[Wiki catkin package](http://wiki.ros.org/catkin/package.xml)

### Create


TODO:

  * Create complete DockerFile
