&#x09;						 ROS2 - Day 2



Workspace



A ROS2 workspace is a directory used to develop and build ROS2 packages. A common workspace name is "ros2\_ws".



* Typical structure:



\- src: contains packages and source code.

\- build: contains build files.

\- install: contains installed package files.

\- log: contains build logs.



* &#x20;Package



A package is an organised unit of ROS2 code. It may contain nodes, configuration files, launch files and dependencies.



* &#x20;Node



A node is an individual executable program that performs a specific task.



Examples:

\- Camera node

\- Object-detection node

\- Motor-control node



* &#x20;Topic



A topic is a named communication channel through which nodes exchange continuous data.



* &#x20;Publisher



A publisher sends messages to a topic.



* &#x20;Subscriber



A subscriber receives messages from a topic.



* &#x20;Message



A message defines the structure of the data exchanged between nodes.



* &#x20;Communication Example



Camera Node → publishes image message → `/camera/image` topic → Object Detection Node subscribes



* &#x20;Service



A service is used for request-and-response communication.



Example:

A client asks a node to reset a sensor, and the service returns whether the reset succeeded.



* &#x20;Topic vs Service



A topic is suitable for continuous data such as camera images or sensor readings.



A service is suitable for a specific request that expects one response.

