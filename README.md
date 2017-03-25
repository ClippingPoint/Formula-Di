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

#### Troubleshoot

[Rostopic: Error. Unable to communicate with master!](http://answers.ros.org/question/30106/error-unable-to-communicate-with-master/)c

### First ROS bag

Copying files from your host(mac) to docker container

1. Check your container names
```bash
  docker ps -l
```

2. Copy files
```bash
  docker cp ~/some_folder/Didi-Training-Release-1/approach_1.bag  your_container_name:/approach_1.bag
```

<em>Approcha_1.bag</em> size is around 500 MB, which makes it is easier to handle.


