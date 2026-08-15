		ROS2 Day 15 - Gazebo Simulation Basics

## Topic
Introduction to Gazebo Simulation with ROS2

## What is Gazebo?
Gazebo is a 3D simulation environment used to simulate robots, objects, sensors and physics without requiring physical robot hardware.

## Today's Practical

### 1. Installed Gazebo for ROS2 Humble
Installed the Gazebo ROS packages and verified the installation.

Gazebo version:
- Gazebo 11.10.2

### 2. Launched Gazebo

Command:

ros2 launch gazebo_ros gazebo.launch.py

This started the Gazebo simulation environment through ROS2.

### 3. Checked Spawn Service

Command:

ros2 service list | grep spawn

Output:

/spawn_entity

The `/spawn_entity` service is used to add an entity or model into the Gazebo simulation.

### 4. Created a Simple URDF Model

Created:

simple_box.urdf

URDF stands for Unified Robot Description Format.

It is an XML-based format used to describe robot/model properties such as:
- Links
- Geometry
- Collision properties
- Inertial properties

For today's practice, a simple box model was created.

### 5. Spawned the Model in Gazebo

Used `spawn_entity.py` to load the URDF model into Gazebo.

The model was successfully spawned as:

simple_box

### 6. Checked Simulation Time

Verified the `/clock` topic:

ros2 topic echo /clock

The `/clock` topic continuously published the Gazebo simulation time.

## Basic Flow

URDF Model
    ↓
ROS2 gazebo_ros
    ↓
/spawn_entity
    ↓
Gazebo Simulation
    ↓
3D Model

## Learning Outcome

Today I learned the basic integration between ROS2 and Gazebo.

I understood how a URDF model can describe an object and how ROS2 can spawn that model into a Gazebo simulation environment.
