		 ROS2 Day 22 - Object Detection Subscriber

## Today's Task
Created a ROS2 subscriber for the object detection topic.

## Work Done
- Created `object_detection_subscriber.py`.
- Subscribed to the `/object_detection` topic.
- Used `std_msgs/String` for communication.
- Ran the existing object detection publisher.
- Received the published detection result in the subscriber.
- Verified Publisher-Subscriber communication successfully.

## Result
Publisher:
`Published: OBJECT DETECTED`

Subscriber:
`Received: OBJECT DETECTED`

## Concept Learned
A ROS2 publisher sends messages to a topic, and a subscriber listens to the same topic and receives those messages.
