						 ROS2 - Day 2



Workspace



A ROS2 workspace is a directory used to develop and build ROS2 packages. A common workspace name is "ros2\_ws".



* Typical structure:



- src: contains packages and source code.

- build: contains build files.

- install: contains installed package files.

- log: contains build logs.



* Package



A package is an organised unit of ROS2 code. It may contain nodes, configuration files, launch files and dependencies.




* Service



A service is used for request-and-response communication.



Example:

A client asks a node to reset a sensor, and the service returns whether the reset succeeded.



* Topic vs Service



A topic is suitable for continuous data such as camera images or sensor readings.



A service is suitable for a specific request that expects one response.

