		 ROS2 Day 13 - Camera and LiDAR Sensor Basics

## Topic

Introduction to Camera and LiDAR sensors in ROS2.

## Camera

A camera provides visual information about the robot's environment.

ROS2 commonly represents uncompressed camera images using:

sensor_msgs/msg/Image

Important fields include:

- height - image height
- width - image width
- encoding - pixel encoding format
- step - size of each image row in bytes
- data - actual image data
- header - timestamp and frame information

The interface was inspected using:

ros2 interface show sensor_msgs/msg/Image


## LiDAR

LiDAR stands for Light Detection and Ranging.

It measures distances between the sensor and surrounding objects using laser measurements.

ROS2 commonly represents a 2D LiDAR scan using:

sensor_msgs/msg/LaserScan

Important fields include:

- angle_min - starting angle of scan
- angle_max - ending angle of scan
- angle_increment - angle between measurements
- range_min - minimum valid distance
- range_max - maximum valid distance
- ranges - measured distance values
- intensities - intensity information


## LiDAR Publisher Practical

Created a Python ROS2 node:

lidar_publisher.py

The node publishes LaserScan messages to:

/scan

Sample simulated distance values:

[1.0, 2.0, 1.5, 3.0, 2.5]

The publisher was successfully executed and the data was verified using:

ros2 topic echo /scan


## Communication Flow

LiDAR Publisher Node
        ↓
LaserScan Message
        ↓
/scan Topic
        ↓
Subscriber / Robot System


## Sense - Decide - Act

A basic robot system can be understood as:

Sensors
   ↓
Sense Environment
   ↓
Process / Decide
   ↓
Movement Command
   ↓
Robot Action

Camera and LiDAR can provide sensor information, while velocity commands such as Twist can be used to control robot movement.


## Learning Outcome

Learned the basic purpose of Camera and LiDAR sensors in robotics.

Inspected Image and LaserScan ROS2 message structures and created a simple ROS2 publisher that publishes simulated LiDAR distance data through the /scan topic.
