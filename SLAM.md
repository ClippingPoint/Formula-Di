## Rigid body dynamics

Global vs Local reference frame

[References Frames](http://www.kwon3d.com/theory/transform/refrm.html)

[Quaternion from global space to local space](http://math.stackexchange.com/questions/1690239/quaternion-from-global-space-to-local-space)

[Conversion gps longitude latitude to (x,y) of local reference frame?](http://robotics.stackexchange.com/questions/10450/conversion-gps-longitude-latitude-to-x-y-of-local-reference-frame/10451)

  * Localization

  * Transform (Translation and Rotation)

### Rotation

#### Quaternions

[Understanding quaternions](https://www.3dgep.com/understanding-quaternions/)

```c
  p = [0, x, y, z]
```
  After rotation

  p_prime = q p q_inverse

#### Axis angle and Rodrigues Formula

[Axis Angle representation](https://en.wikipedia.org/wiki/Axis%E2%80%93angle_representation)

#### Euler Angles

Mostly for human readable purpose, seldomly used in actual calculation.

Issue: Singularity, Gimbal lock

### [ROS/TF](http://wiki.ros.org/tf)

tf is a package that lets the user keep track of multiple coordinate frames over time

[Quaternions orientation representation](http://answers.ros.org/question/9772/quaternions-orientation-representation/)

[Transform Configuration](http://wiki.ros.org/navigation/Tutorials/RobotSetup/TF#Transform_Configuration)

[Applying rotations to coordinate frames using TF](http://answers.ros.org/question/87726/applying-rotations-to-coordinate-frames-using-tf/)

[ROS SLAM Mapping](http://wiki.ros.org/slam_gmapping/Tutorials/MappingFromLoggedData)

## Kalman Filter, EKF and more

[An explanation of the Kalman Filter](http://math.stackexchange.com/questions/840662/an-explanation-of-the-kalman-filter)

[Question about Q matrix noise process covariance in Kalman filter](http://dsp.stackexchange.com/questions/21796/question-about-q-matrix-noise-process-covariance-in-kalman-filter)

# References 

[Youtube SLAM tutorials](https://www.youtube.com/watch?v=B2qzYCeT9oQ&index=1&list=PLpUPoM7Rgzi_7YWn14Va2FODh7LzADBSm)

ROS Hector SLAM
[F1/10 ROS SLAM Installation](http://f1tenth.org/lab_instructions/W3_T1_Using%20the%20Hector%20SLAM.pdf)

Odometry, EKF, state estimation
[SLAM for Dummies](https://ocw.mit.edu/courses/aeronautics-and-astronautics/16-412j-cognitive-robotics-spring-2005/projects/1aslam_blas_repo.pdf)
