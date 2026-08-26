				  Day 24 Report

## Task
Video Feed Object Detection using OpenCV

## Work Completed
Today I completed the video-feed object detection part of the Week 3 task.

I first tested the laptop camera devices. Since the camera device was detected but frame capture was not working correctly, I used a video feed instead.

The video was processed frame by frame using OpenCV. Each frame was converted to grayscale, Gaussian Blur was applied, Canny Edge Detection was performed, and contours were detected.

Bounding boxes were drawn around larger detected regions and the processed video was displayed successfully.

## Result
Video Feed → OpenCV Processing → Contour Detection → Bounding Boxes
