				   ROS2 Day 5 Notes

## What is a ROS2 Node?
A ROS2 node is an independent executable program that performs a specific task in a robot. Different nodes communicate with each other to build a complete robotic application.

## Why are ROS2 Nodes used?
- To divide a robot into smaller independent programs.
- Makes the system modular and easier to maintain.
- Enables communication between different parts of the robot.

## Difference between Publisher and Subscriber

Publisher
- Sends data.
- Writes message to a topic.
- Produce Information

Subscriber
- Receives data.
- Reads message from a topic.
- Consume Information

## rclpy
The ROS2 Client Library for Python. It provides the APIs required to create ROS2 nodes, publishers, subscribers, timers, and other ROS2 functionality.

## std_msgs.msg
A package containing standard message types such as:
- String
- Int32
- Float32
- Bool

## colcon build
Builds the selected ROS2 package and prepares it so ROS2 can execute the nodes.

## source install/setup.bash
Loads the built workspace into the current terminal so ROS2 can recognize the packages.

## ros2 run
Runs a specific executable (node) from a ROS2 package.

## Commands Used Today

cd ~/ros2_ws
colcon build --packages-select my_robot
source install/setup.bash
ros2 run my_robot talker
ros2 run my_robot listener
