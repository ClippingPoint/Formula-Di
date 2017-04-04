import data
import lidar_views as lidar_views

## TODO:
## Timing and profile the code

approach_1 = data.data('./approach_1.bag').read_rosbag()

topic, msg, t = approach_1.lidar.next()

# One frame
single_frame = approach_1.lidar_to_pc(msg)

# Create bird_eye_view of the images
im = lidar_views.point_cloud_to_top(single_frame)
lidar_views.save_to_image(im, './out.png')
