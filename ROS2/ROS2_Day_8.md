ROS2 Day 8 - ROS2 Parameters

Topics Learned

- Introduction to ROS2 Parameters
- Creating a parameter inside a ROS2 node
- Reading parameter values
- Changing parameter values while a node is running
- ROS2 node and parameter CLI commands
- Revised Python OOP concepts used in ROS2 nodes


What is a ROS2 Parameter?

A parameter is a configuration value associated with a ROS2 node.

Example:
robot_name = AmruthaBot

Parameters allow us to configure a node without hard-coding every value.


Parameter Node Created

File:
parameter_node.py

Parameter:
robot_name

Default Value:
AmruthaBot


Important Python / ROS2 Concepts

class ParameterNode(Node):
Creates a class that inherits from the ROS2 Node class.

__init__():
Constructor that runs when an object of the class is created.

self:
Refers to the current object.

super().__init__('parameter_node'):
Initializes the parent ROS2 Node class and gives the node its name.

declare_parameter():
Declares a parameter and its default value.

get_parameter():
Reads the current value of a parameter.

rclpy.spin():
Keeps the ROS2 node running.


Commands Practiced

ros2 node list

ros2 param list /parameter_node

ros2 param get /parameter_node robot_name

ros2 param set /parameter_node robot_name RoboBot


Test Result

Initial parameter value:
AmruthaBot

Changed parameter value:
RoboBot

The parameter was successfully changed while the ROS2 node was running.


Difference Between Communication Concepts

Topic:
Continuous data communication using Publisher and Subscriber.

Service:
Request and Response communication using Client and Server.

Parameter:
Configuration value associated with a node.



