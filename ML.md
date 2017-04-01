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
