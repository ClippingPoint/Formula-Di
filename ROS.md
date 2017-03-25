## First ROS bag

What is [ROS bag](http://wiki.ros.org/Bags)

Copying <em>Didi Challenge</em> .bag files from your host(mac) to docker container

1. Check your container names
```bash
  docker ps -l
```

2. Copy files
```bash
  docker cp ~/some_folder/Didi-Training-Release-1/approach_1.bag  your_container_name:/approach_1.bag
```

<em>Approcha_1.bag</em> size is around 500 MB, which makes it is easier to handle.


# References

[ROS Indigo Cheatsheet](https://w3.cs.jmu.edu/spragunr/CS354_F15/handouts/ROSCheatsheet.pdf)


