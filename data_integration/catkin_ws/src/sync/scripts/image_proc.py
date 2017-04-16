from cv_bridge import CvBridge, CvBridgeError
import rospy

# http://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython

"""
Add your image preprocessor here
Such as transformation, cropping and so forth
"""

def image_message_to_cv2(self, image_messages):
    try: 
	cv_image = CvBridge.imgmsg_to_cv2(image_message, desired_encoding="passthrough")
	return cv_image
    except CvBridgeError as e:
	rospy.logerr(e)


