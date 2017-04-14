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

To /odom format?

```bash
  rosrun nodelet nodelet standalone velodyne_pointcloud/TransformNodelet
```

[Processing velodyne data for dataset-2](https://discussions.udacity.com/t/processing-velodyne-data-for-dataset-2/237084/3)

[Velodyne_point_cloud wiki Example 2.1.4](http://wiki.ros.org/velodyne_pointcloud)

Then play rosbag

```bash
  rosbag play -l some.bag
```

Check rostopic list in different bash, we will see ```velodyne_pointcloud``` topic

[How to extract the data from the packets of velodyne hdl 32e](http://answers.ros.org/question/53499/how-to-extract-the-data-from-the-packets-of-velodyne-hdl-32e/)

[Convert velodyne scan to pointcloud2 from a rosbag](http://answers.ros.org/question/191972/convert-velodynescan-to-pointcloud2-from-a-rosbag-file/)

[Questions about velodyne point cloud package](http://answers.ros.org/question/188725/some-questions-about-velodyne_pointcloud-package/)

[Conversion from sensor message point cloud 2 to pcl point cloud](http://answers.ros.org/question/136916/conversion-from-sensor_msgspointcloud2-to-pclpointcloudt/)

## ROS package

Software in ROS is organized in packages. A packages might contain ROS nodes, a ROS-independent library, a dataset, configuration files, a third-party piece of software,
or anything else that logically constitute a useful module.

[Wiki catkin package](http://wiki.ros.org/catkin/package.xml)

1. Create catkin workspace

[Create a catkin workspace](http://wiki.ros.org/cn/catkin/Tutorials/create_a_workspace)

Optional: Creating a ROS package

[Creating Package](http://wiki.ros.org/ROS/Tutorials/CreatingPackage)

Then build

[Writing a Python Writing Publisher Subscriber node](http://wiki.ros.org/ROS/Tutorials/WritingPublisherSubscriber%28python%29)


TODO:

  * Create complete DockerFile



### Building Lidar Package from ros-examples ###

How to install the requirements and compile the [ros-examples lidar package](https://github.com/mjshiggins/ros-examples) provided by Udacity.  These instructions assume the ROS distribution is Indigo.

Requirements:  [PCL Library](http://pointclouds.org)
and [catkin](http://wiki.ros.org/catkin)

If catkin is not already installed:  ```sudo apt-get install ros-indigo-catkin```
If needed install the dependencies:  ```sudo apt-get install cmake python-catkin-pkg python-empy python-nose python-setuptools libgtest-dev build-essential```

Now install PCL:  ```sudo add-apt-repository ppa:v-launchpad-jochen-sprickerhof-de/pcl
sudo apt-get update
sudo apt-get install libpcl-all```

If downloaded already, do so now for [mjshiggins/ros-examples](https://github.com/mjshiggins/ros-examples).

There is an errant ```CMakeLists.txt``` file that seems to interfere with the catkin build.  Delete it before building:  ```rm ros-examples/src/CMakeLists.txt```.
Now go into the directory:  ```cd ros-examples```
Make from there:  ```catkin_make```
Note:  typically you would need to run ```catkin_create_pkg package_name node_name``` but this seems to have been done already and the ```CMakeLists.txt``` and ```package.xml``` are already in ```ros-examples/src/lidar/```.

Before running the node it needs to be added to bash:  ```source ros-examples/devel/setup.bash```.  
Now it should run:  ```rosrun lidar lidar_node```

Try playing the bag file and see if it is placing images in the ```/images``` directory:  ```rosbag play -l name-of-file.bag```.


### Using ROS python script with velodyne packets

After resolveing ROS dependencies mentioned in previous section, configuring catkin_ws, copy _catkin_ws_ under _data\_integration.

A new cpp/python node _sync_ is created based on Udacity/ros-example. Package.xml and CMakeLists.txt are modified to map new node name: sync 

Play ros bag

```bash
  rosbag play -l some.bag --clock # running under system clock?
```

Convert velodyne packets to velodyne point cloud

```bash
  rosrun nodelet nodelet standalone velodyne_pointcloud/CloudNodelet
```

Use with template HDL32e coming with package:

```bash
  rosrun velodyne_pointcloud cloud_node _calibration:=32db.yaml
```

```32db.yaml``` file located under 

```bash
  /opt/ros/indigo/share/velodyne_pointcloud/params
```

References:

[Velodyne calibration](http://answers.ros.org/question/89756/velodyne-calibration/)

[Velodyne point cloud yaml file does not work](http://answers.ros.org/question/229102/velodyne-point-cloud-node-doesnt-work/)


Please see Velodyne ROS node section for velodyne_packets to velodyne_points conversion details.

Run python version

```bash
  rosrun sync listener.py
```

Run cpp version

```bash
  rosrun sync sync_node
```
