&#x09;					ROS2 Fundamentals — Day 1



* What is ROS2?



ROS2 stands for Robot Operating System 2. It is a collection of software tools, libraries and communication mechanisms used to build robotic applications.



ROS2 is not a complete operating system like Windows or Ubuntu. It runs on top of an operating system, commonly Ubuntu.



* Why is ROS2 used?



A robot may contain several independent programs for cameras, motors, sensors, navigation and decision-making. ROS2 helps these programs communicate and work together.



\# Node



A node is an individual program that performs one specific task.



Examples:

\- A camera node captures images.

\- A sensor node reads sensor data.

\- A motor-control node controls movement.



\# Topic



A topic is a named communication channel used by ROS2 nodes to exchange data continuously.



Examples:

\- /camera/image

\- /scan



\# Message



A message is the structured data sent through a topic.



Examples include text, velocity values, camera images and sensor readings.



\# Publisher



A publisher is a node that sends messages to a topic.



Example: A camera node publishes images to a camera topic.



\# Subscriber



A subscriber is a node that receives messages from a topic.



Example: An object-detection node subscribes to the camera topic and processes the received images.



\# Communication Example



Camera node → publishes images → camera topic → object-detection node subscribes



\# Today's Understanding



ROS2 divides a robotics system into smaller programs called nodes. Nodes communicate using topics and messages through publishers and subscribers.

