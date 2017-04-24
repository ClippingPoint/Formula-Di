import pandas as pd
import parse_tracklet as xml_parser
import numpy as np
import poses_estimator as pe
import generate_tracklet

# TODO: Take Udacity reader code

"""
Utility files for estimating obstacle poses

In training, since in real time, we wouldn't have "ground truth"

Vehicle frame (coordinate system) 

Reference:

https://github.com/udacity/didi-competition/blob/master/tracklets/python/bag_to_kitti.py

get_obstacle_pos 

estimate_obstacle_pos

lwh_to_box is based on lwh_to_box in evaluate_tracklets.py 

XML parser:
www.cvlibs.net/datasets/kitti/downloads/parseTrackletXML.py
"""

def lwh_to_box(l, w, h):
    box = np.array([
        [-l / 2, -l / 2, l / 2, l / 2, -l / 2, -l / 2, l / 2, l / 2],
        [w / 2, -w / 2, -w / 2, w / 2, w / 2, -w / 2, -w / 2, w / 2],
        # FIXME constrain height to range from ground or relative to centroid like l & w?
        [-h / 2, -h / 2, -h / 2, -h / 2, h / 2, h / 2, h / 2, h / 2],
        #[0.0, 0.0, 0.0, 0.0, h, h, h, h]
    ])
    return box

#def corner_pos_in_velo(tracklet_box, trans, yaw=0):
#    """
#    To capture vehicle velodyne reference frame
#    In KITTI dataset, yaw = rotation[2]
#    For round 1 yaw will not be evaluated. 
    
#    Do we need visual yaw reference? I think we do
#    """
#    rot_mat = np.array([[np.cos(yaw), -np.sin(yaw), 0.0],
#			[np.sin(yaw), np.cos(yaw), 0.0],
#			[0.0, 0.0, 1.0]])
    # TODO: calc yaw as seen from the camera (i.e. 0 degree = facing away from cam), as oppposed to 
    # car-centered yaw (i.e. 0 degree = same orientation as car).
    # makes quite a difference for objects in periphery
    # result in [0, 2pi] 
    # x, y, z = translation
    # yaw_visual = (yaw - np.arctan2(y, x)) % (2*np.pi)
#    return (np.dot(rot_mat, tracklet_box) + np.tile(trans, (8, 1)).T)

# TODO: correct get_yaw in tracklet generation function
# http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
def generate_boxes(tracklets):
    for tracklet_idx, tracklet in enumerate(tracklets):
        h, w, l = tracklet.size
        box_vol = h * w * l
        tracklet_box = lwh_to_box(l, w, h)
        # print(tracklet_box)
        frame_idx = tracklet.first_frame
        for trans, rot in zip(tracklet.trans, tracklet.rots):
            # calc 3D bound box in capture vehicle oriented coordinates
            yaw = rot[2]  # rotations besides yaw should be 0
            rot_mat = np.array([
                [np.cos(yaw), -np.sin(yaw), 0.0],
                [np.sin(yaw), np.cos(yaw), 0.0],
                [0.0, 0.0, 1.0]])
	    # corner_pos_in_velo
            oriented_box = np.dot(rot_mat, tracklet_box) + np.tile(trans, (8, 1)).T
            yield frame_idx, tracklet_idx, tracklet.object_type, box_vol, oriented_box
            frame_idx += 1
# http://stackoverflow.com/questions/1984162/purpose-of-pythons-repr
class Obs(object):
    def __init__(self, tracklet_idx, object_type, box_vol, oriented_box):
        self.tracklet_idx = tracklet_idx
        self.object_type = object_type
        self.box_vol = box_vol
        self.oriented_box = oriented_box

    def __repr__(self):
        return str(self.tracklet_idx) + ' ' + str(self.object_type)

# Or maybe tracklet reader? 
class Xml_Reader():
    def __init__(self):
	"""
	Indices: Index range for evaluation
	"""
	return None
    def parse_xml_tracklet(self, xml_path):
	"""
	By default evaluate all frames
	TODO: parameterize frame range later?
	Parameters:
	--------------------
	xml_path: absolute path
	"""
	obs_list = []
	tracklets = xml_parser.parse_xml(xml_path)
#	for i, tracklet in enumerate(tracklets):
#	    print(lwh_to_box)
#	    print(dir(tracklet))
	for frame_idx, tracklet_idx, object_type, box_vol, oriented_box in generate_boxes(tracklets):
	#print(tracklets.size)
	    obs_list.append(Obs(tracklet_idx, object_type, box_vol, oriented_box))
#	    print(obs_list[frame_idx].oriented_box)
	return obs_list
    def is_obs_in_view(self):
	"""
	Return True or false to see if obs present in current view?
	"""
	return NotImplemented

class Xml_Writer():
    def __init__(self):
	"""
	Indices: Index range for evalueation
	create_obs_list -> append_frame_coord_to_rtk_list -> collection = TrackletCollections
	"""
	self.tracklet_collection = TrackletCollection()
	return None
    def add_obs_to_tracklet_collection(self, mdr, cap_front_rtk, cap_rear_rtk, obs_centroid, first_frame=0):
	"""
	Parameters:
	-------------------
	mdr: dict of obstacle dimension information
	cap_front_rtk_interp: list of rtk data synced to image frames
	cap_rear_rtk_interp: list of rtk data synced to image frames
	obs_centroid_interp: list of rtk data synced to image frames
	"""
	assert mdr['object_type'] is not None
	assert mdr['l'] is not None
	assert mdr['w'] is not None
	assert mdr['h'] is not None
	obs_tracklet = Tracklet(object_type=mdr['object_type'], l=mdr['l'], w=mdr['w'], h=mdr['h'], first_frame=0)
	obs_tracklet.poses=estimate_obstacle_poses(
	    cap_front_rtk=cap_front_rtk_interp,
	    cap_rear_rtk=cap_rear_rtk_interp,
	    obs_centroid_interp =obs_centroid_interp
	)
	self.trakclet_collection.append(obs_tracklet)
    def export_tracklet_to_file(self, tracklet_path, prefix='./'):
	"""
	Parameters
	--------------------
	e.g. tracklet_path: 'tracklet_labels.xml'
	"""
	tracklet_path = os.path.join(prefix, tracklet_path)
	collection.write_xml(tracklet_path)
	


if __name__ == "__main__":
    Xml_Reader().parse_xml_tracklet('/root/tracklet_labels.xml')
