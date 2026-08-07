				     Day 7 Report

## Today's Activities

- Learned the concept of ROS2 Services.
- Understood the difference between Topics and Services.
- Created a Service Server (service_server.py).
- Created a Service Client (service_client.py).
- Registered both executables in setup.py.
- Built the package using colcon build.
- Sourced the ROS2 workspace.
- Successfully executed the Service Server and Client.
- Verified request-response communication using the AddTwoInts service.
- Prepared Day 7 notes and documentation.

## Commands Used

cd ~/robotics-training/ros2_ws

colcon build

source install/setup.bash

ros2 run my_robot service_server

ros2 run my_robot service_client

## Output

Server Output:

Request: 10 + 20

Client Output:

Result: 30

## Challenges Faced

- The service executables were initially not found because setup.py was not registered and rebuilt.
- Restored talker.py and listener.py into the robotics-training workspace.
- Rebuilt the package to register the new service nodes successfully.

## Learning Outcome

Today I learned how ROS2 Services work using the Client-Server model. I understood the request-response communication mechanism, created both Service Server and Service Client nodes, registered them in setup.py, and successfully tested the communication using the AddTwoInts service.
