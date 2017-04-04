[Deep Learning for Laser Based Odometry Estimation](http://juxi.net/workshop/deep-learning-rss-2016/papers/Nicolai%20-%20Deep%20Learning%20Lidar%20Odometry.pdf)


Traditional Odometry:

Wheel based dead reckoning: diverging estimate of a robot`s position

IMU, three accelerometers and gyroscopes: Noisy estimates, wheel slippage

One solution:  scan-matching often uses a technique knowns as Iterative Closest Point (ICP) to iteratively minimize the difference between two clouds
of points, in this case two consecutively laser scans. The estimated transformation is used to estimate the motion of the robotic base.

ICP: Expensive, sensitive to large differences in the initial point distributions. 

Improvement: Zhang and Singh 

  Two loops

 *Lidar odometry and mapping in real-time. In Robotics: Science and Systems Conference

 *[Low-drift and real-time lidar odometry and mapping. Autonomous Robots](http://www.frc.ri.cmu.edu/~jizhang03/Publications/AURO_2017_2.pdf)

Another solution: Visual odometry

  Konda and Memisevic:

  _reduce high dimensional point cloud data to a depth image that we can pass into a CNN to perform motion estimation._

  regression vs soft-max

Problem Formulation

A. Voxel 3D Convolution

B. Image Based 2D Convolution
  
  Modify our point cloud into a 2D projection of the environment; that is a panoramic depth image. "We do this by binning the raw VLP-16 scans into pixel representations"



[Vehicle Detection Based on LiDAR and Camera Fusion](http://www6.in.tum.de/Main/Publications/Zhang2014b.pdf)

## Object Detection

### CV

[How to do Object Detection with OpenCV](https://www.youtube.com/watch?v=OnWIYI6-4Ss)
