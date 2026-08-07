		 ROS2 Day 7 - ROS2 Services (Server & Client)

# Topics Learned

- Introduction to ROS2 Services
- Difference between Topics and Services
- Service Server
- Service Client
- Request and Response communication
- Callback function
- Built-in AddTwoInts Service
- Registering executables in setup.py
- Running Service Server and Client


# What is a ROS2 Service?

A ROS2 Service is a communication mechanism based on Request and Response.

A Client sends one request to a Server, and the Server processes the request and sends one response.

Unlike Topics, Services are not continuous communication.

Example:
Client → Add 10 and 20
Server → 30


# Difference between Topic and Service

Topic:
- Publisher → Topic → Subscriber
- Continuous communication
- Used for sensor data, camera images, etc.

Service:
- Client → Server
- One Request → One Response
- Used for calculations or robot commands


# Files Created

- service_server.py
- service_client.py

# Python Modules Used

- rclpy
- rclpy.node.Node
- example_interfaces.srv.AddTwoInts


# Important Functions

create_service()
- Creates a Service Server.

create_client()
- Creates a Service Client.

wait_for_service()
- Waits until the server becomes available.

call_async()
- Sends a request asynchronously.

spin()
- Keeps the node running.

spin_until_future_complete()
- Waits until the client receives the response.


# Workflow

Client
↓

Request

↓

Service Server

↓

Callback Function

↓

Response

↓

Client receives the result


# Commands Used

cd ~/robotics-training/ros2_ws

colcon build

source install/setup.bash

ros2 run my_robot service_server

ros2 run my_robot service_client


## Output

Server:

Request: 10 + 20

Client:

Result:30
