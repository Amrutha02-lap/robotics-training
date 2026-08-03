				    ROS2 Day 4

## Objective
Install ROS2 Humble on Ubuntu and create the first ROS2 Python node.

## Tasks Completed

### 1. Installed ROS2 Humble
- Updated Ubuntu packages.
- Added ROS2 repository.
- Installed ROS2 Humble Desktop.
- Configured the environment using:
  source /opt/ros/humble/setup.bash

### 2. Verified Installation
Commands used:
- ros2
- ros2 topic list

Verified that ROS2 was installed successfully.

### 3. Created ROS2 Workspace

Commands:

mkdir -p ~/ros2_ws/src
cd ~/ros2_ws

### 4. Created Python Package

Package Name:
my_robot

Command used:

ros2 pkg create --build-type ament_python my_robot

### 5. Created First ROS2 Node

File:
hello_node.py

The node prints:

Hello! My first ROS2 node is running.

### 6. Build the Package

Command:

colcon build

### 7. Source the Workspace

Command:

source install/setup.bash

### 8. Run the Node

Command:

ros2 run my_robot hello_node

Output:

Hello! My first ROS2 node is running.

## Challenges Faced

- Repository setup errors.
- colcon command not found
- Package executable not found.
- Fixed setup.py entry point issues.
- Successfully resolved all errors.
