# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

# Starter Kit

## Env setup

### Docker on Mac

[Download docker for mac](https://docs.docker.com/docker-for-mac/install/#download-docker-for-mac)

[Get started with Docker for Mac](https://docs.docker.com/docker-for-mac/)

#### Docker + Ros

[Docker and ROS](http://wiki.ros.org/docker/Tutorials/Docker)

[Sample Docker installation script](https://github.com/uts-magic-lab/ros-docker)

```bash
 docker pull ros:indigo-robot
```

 * To initiate a docker terminal on mac

![Quick terminal image](https://bytebucket.org/Khanhh/formual-di/raw/b0db6609321d1ee69eb048f605d7edaffd5d7f97/setup/quick_terminal.png?token=a1d19639db0b9794c452ba953e293e8f3810e77f)

 * Check installation and environment setup

```bash
  echo $ROS_PACAKGE_PATH
```

  * Get into certain container (in docker teriminal)

```bash
  docker exec -it <mycontainer> bash
```

[How to continue a docker which is exited](http://stackoverflow.com/questions/21928691/how-to-continue-a-docker-which-is-exited)

#### Troubleshoot

[Rostopic: Error. Unable to communicate with master!](http://answers.ros.org/question/30106/error-unable-to-communicate-with-master/)c

#

## Data integration

Files under /scripts are created to easily execute admin tasks such as docker operations

Examples:

```bash
  ./docker_cp <docker_container_name>:/root/base_line ~/my_local_ws
```

```bash
  ./exec_bash <docker_container_name>
```

### Lidar data integration

  After point_cloud conversion, Velodyne point cloud pc2 has below format for each data point, see ```data_integration/process.py single_frame``` for example

  [Velodyne PC2](https://bytebucket.org/Khanhh/formual-di/raw/e509144cd56e51306b20cfe9f585b135621a1fc9/setup/velodyne_pc2.png?token=4dec74e58b529ab4ac355845b99e9e2a598caabe)

  data pack format [X, Y, Z, Intensity, Ring_number]


References: 

Data format:

[Velodyne pointcloud point types](https://github.com/ros-drivers/velodyne/blob/master/velodyne_pointcloud/include/velodyne_pointcloud/point_types.h)

[Organizing point cloud from HDL-32e](http://answers.ros.org/question/59743/organizing-point-cloud-from-hdl-32e/)

[Accessing layers in velodyne point cloud](http://answers.ros.org/question/132811/accessing-layers-in-velodyne-point-cloud/)

[Velodyne ROS driver ring sequence](https://github.com/ros-drivers/velodyne/blob/master/velodyne_driver/include/velodyne_driver/ring_sequence.h)
