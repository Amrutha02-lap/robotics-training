			ROS2 Day 11 - Velocity Commands

## Topic
Publishing Velocity Commands using ROS2

## cmd_vel Topic

The cmd_vel topic is commonly used to send velocity commands to a mobile robot.

In turtlesim, the topic used was:

/turtle1/cmd_vel

## Twist Message

The velocity command uses:

geometry_msgs/msg/Twist

A Twist message contains linear and angular velocity.

Important values used:

linear.x = 1.0
angular.z = 1.0

linear.x controls forward/backward movement.

angular.z controls rotational movement.

## CLI Practice

Checked available topics:

ros2 topic list

Checked the message type:

ros2 topic type /turtle1/cmd_vel

Inspected the Twist message:

ros2 interface show geometry_msgs/msg/Twist

Published velocity commands through the terminal and observed the turtle movement.

## Python ROS2 Node

Created:

velocity_publisher.py

The node publishes Twist messages to:

/turtle1/cmd_vel

The publisher was configured with:

linear.x = 1.0
angular.z = 1.0

The turtle moved continuously in a circular path.

## Communication Flow

velocity_publisher node
        ↓
Twist message
        ↓
/turtle1/cmd_vel
        ↓
turtlesim node
        ↓
Turtle movement

## Learning Outcome

Learned how velocity commands are published through a ROS2 topic using the Twist message.

Practiced robot movement using both ROS2 CLI commands and a Python ROS2 publisher node.
