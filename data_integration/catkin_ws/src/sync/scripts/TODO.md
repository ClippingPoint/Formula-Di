##

Master script/launch file for process control

## Coordinate transformation

Between image plane and velodyne plane


## Hardware

Using VLP-16 Velodyne calibration file instead of 32e?

Paper:

Vehicle Detection from 3D Lidar Using Fully Convolutional Network

In conv1, the point map is down-sampled by 4 horizontally and 2 vertically. This is because for a point map captured by Velo 64E, we have
approximately delta phi = 2 delta theta. i.e. points are denser on horizontal direction


Data Augmentation

For the case of range scans, simply applying these operations results in variable delta theta and delta phi, which violates the geometry property of the lidar device.

To synthesis geometrically correct 3D range scans, we randomly generate a 3D transforma near identity


For round 1, obstacle orientation is not evaluated, so no rotation augmentation needed? Only translation

## Evaluation

lwh_to_box is based on evaluate_tracklets, keep updating it so that it can keep up with newest evaluation toolset

## Understanding

As 04/18/2017, Udacity tracklet labels uses centroid of object/obstacle as original of local reference frame

which is different from KITTI dataset use centroid of bottom surface of tracklet box

# Fix yaw for velodyne data?

[bag_to_kitti code](https://discussions.udacity.com/t/kitti-to-bag-py-code-is-wrong/241269)
