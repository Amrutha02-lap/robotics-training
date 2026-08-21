				   Day 21 Report

## Work Completed

Today I integrated basic OpenCV image processing with ROS2.

I created an object detection publisher node that reads an image using OpenCV, converts it to grayscale, applies Gaussian Blur and Canny edge detection, and uses contours for basic object detection.

The detection result is published as a String message on the `/object_detection` ROS2 topic every 2 seconds.

I verified the communication using:

`ros2 topic echo /object_detection`

The topic successfully displayed:

`OBJECT DETECTED`

## Result

Successfully integrated basic OpenCV object detection with a ROS2 publisher.
