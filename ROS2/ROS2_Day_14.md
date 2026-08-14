			ROS2 Day 14 - ROS Bag Record and Replay

## Topic

ROS2 Bag Record and Replay

## What is ROS Bag?

ROS Bag is used to record ROS2 topic data and replay it later.

This is useful for testing, debugging and working with recorded sensor data without needing the original sensor to be active.

## Practical Work

The simulated LiDAR publisher was running and publishing:

/scan

Message type:

sensor_msgs/msg/LaserScan

The topic data was recorded using:

ros2 bag record /scan

The recording was stopped using Ctrl+C.

The recorded bag information was checked using:

ros2 bag info rosbag2_2026_08_14-18_22_31

The bag contained:

- Topic: /scan
- Type: sensor_msgs/msg/LaserScan
- Messages: 28
- Duration: approximately 27 seconds

## Playback

The original LiDAR publisher was stopped.

The recorded bag was replayed using:

ros2 bag play rosbag2_2026_08_14-18_22_31 --loop

The /scan topic appeared again during playback.

The replayed data was verified using:

ros2 topic echo /scan

The same LaserScan values were successfully received.

## Communication Flow

LiDAR Publisher
      ↓
/scan Topic
      ↓
ros2 bag record
      ↓
Saved Bag

Later:

Saved Bag
      ↓
ros2 bag play
      ↓
/scan Topic
      ↓
ros2 topic echo

## Learning Outcome

Learned how to record ROS2 topic data into a bag file and replay the recorded data later.

Successfully recorded and replayed simulated LiDAR LaserScan messages.
