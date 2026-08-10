				ROS2 Day 10 - Launch Files

## Topic
ROS2 Launch Files

## What is a Launch File?

A launch file is used to start and configure multiple ROS2 nodes using a single command.

Previously, the talker and listener nodes were started separately.

Using a launch file, both nodes can be started together.

## Practical Work

Created:
my_robot_launch.py

The launch file starts:
- talker node
- listener node

Command:

ros2 launch my_robot my_robot_launch.py

## Learning Outcome

Learned how ROS2 launch files can be used to start multiple nodes together instead of running each node separately.
