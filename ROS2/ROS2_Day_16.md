		 ROS2 Day 16 - Mobile Robot Control in Gazebo

## Topic
URDF Mobile Robot and Velocity Control in Gazebo

## Today's Practical

### 1. Created a Mobile Robot URDF

Created `mobile_robot.urdf` containing:

- `base_link` - main robot body
- `left_wheel` - left wheel
- `right_wheel` - right wheel
- Continuous joints connecting the wheels to the robot body

The URDF was validated using:

check_urdf mobile_robot.urdf

The XML was successfully parsed and the robot structure was verified.

### 2. Differential Drive

Added the Gazebo differential-drive plugin to the robot.

Differential drive allows a robot to move using the speeds of its left and right wheels.

### 3. Spawned Robot in Gazebo

The mobile robot was successfully spawned into the Gazebo simulation using `spawn_entity.py`.

### 4. Velocity Control

The differential-drive plugin subscribed to the `/cmd_vel` topic.

The `/cmd_vel` topic uses:

geometry_msgs/msg/Twist

Important values:

- `linear.x` - forward/backward velocity
- `angular.z` - rotational velocity

A velocity command was published and the robot successfully moved forward in Gazebo.

### 5. Odometry

The differential-drive plugin publishes robot movement information through:

/odom

Odometry provides information about the robot's estimated position, orientation and velocity.

## Control Flow

ROS2 velocity command
        ↓
/cmd_vel
        ↓
Twist message
        ↓
Differential-drive plugin
        ↓
Wheel movement
        ↓
Robot moves in Gazebo
        ↓
/odom feedback

## Learning Outcome

Today I learned how a simple mobile robot can be described using URDF and controlled inside Gazebo using ROS2 velocity commands.

I also understood the basic relationship between `/cmd_vel`, `Twist`, differential-drive control and `/odom`.
