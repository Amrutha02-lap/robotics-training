			 ROS2 Day 12 - Keyboard Teleoperation

## Topic
Keyboard Control using Turtlesim

## Teleoperation

Teleoperation (teleop) means manually controlling a robot from a remote input device such as a keyboard.

## Practical Work

Started turtlesim:

ros2 run turtlesim turtlesim_node

Started keyboard teleoperation:

ros2 run turtlesim turtle_teleop_key

Used the arrow keys to control the turtle.

## Monitoring Velocity Commands

Used:

ros2 topic echo /turtle1/cmd_vel

This displayed the Twist messages generated while using the keyboard.

## Communication Flow

Keyboard Input
      ↓
turtle_teleop_key Node
      ↓
Twist Message
      ↓
/turtle1/cmd_vel Topic
      ↓
turtlesim_node
      ↓
Turtle Movement

## Observation

Forward movement produced a positive linear.x value.

Left and right rotation change the angular.z value.

## Learning Outcome

Learned how keyboard teleoperation can be used to manually control a robot and observed the velocity commands being published through the /turtle1/cmd_vel topic.
