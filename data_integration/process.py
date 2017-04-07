import data
import lidar_views as lidar_views

## TODO:
## Timing and profile the code

# approach_1 = data.data('./approach_1.bag').read_rosbag()
approach_1 = data.data('./10.bag').read_rosbag()
# approach_1.read_velo_points()
approach_1.read_velo_packets()


# topic, msg, t = approach_1.lidar.next()
topic_packets, msg_packets, t_packets = approach_1.lidar_packets.next()

# One frame
# single_frame = approach_1.lidar_to_pc(msg)
single_frame_packets = approach_1.lidar_packets(msg_packets)

# print(single_frame.shape)
# print(approach_1.lidar_count)

#print(single_frame)

# Create bird_eye_view of the images
im = lidar_views.point_cloud_to_top(single_frame)
lidar_views.save_to_image(im, './out.png')
