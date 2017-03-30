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
