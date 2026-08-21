		 ROS2 Day 21 - OpenCV Object Detection Publisher

## Today's Task
Integrated basic OpenCV object detection with a ROS2 publisher.

## Work Done
- Created `object_detection_publisher.py`.
- Created a ROS2 node named `object_detection_publisher`.
- Created the `/object_detection` topic using String messages.
- Used a timer to perform detection every 2 seconds.
- Loaded an image using OpenCV.
- Converted the image to grayscale.
- Applied Gaussian Blur to reduce noise.
- Used Canny edge detection.
- Used contours and bounding rectangles for basic object detection.
- Published the detection result through ROS2.
- Verified the topic using `ros2 topic echo /object_detection`.

## Output
The node successfully published:

`OBJECT DETECTED`

on the `/object_detection` topic.

## Concepts Learned
- ROS2 Node
- Publisher and Topic
- String messages
- ROS2 Timer
- OpenCV with ROS2
- Grayscale
- Gaussian Blur
- Canny Edge Detection
- Contours
