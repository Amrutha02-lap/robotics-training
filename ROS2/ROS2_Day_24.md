	 ROS2 Day 24 - Video Feed Object Detection using OpenCV

## Objective
Complete the Week 3 perception pipeline by detecting objects from a video feed using OpenCV.

## Work Completed
- Tested available camera devices in Ubuntu.
- Verified that `/dev/video0` and `/dev/video1` were available.
- Tested OpenCV camera access.
- Encountered camera frame capture issues.
- Switched to a video feed as allowed in the training task.
- Loaded a video using OpenCV.
- Processed the video frame by frame.
- Converted each frame to grayscale.
- Applied Gaussian Blur to reduce noise.
- Used Canny Edge Detection.
- Detected contours from each frame.
- Drew green bounding boxes around larger detected regions.
- Displayed the processed video successfully.

## Processing Flow

Video Feed
→ Read Frame
→ Grayscale
→ Gaussian Blur
→ Canny Edge Detection
→ Find Contours
→ Bounding Boxes
→ Display Detection Result

## Result
The video feed was processed successfully and detected regions were highlighted using green bounding boxes.

## Learning Outcome
Understood how the image-processing steps previously used on a single image can be applied continuously to video frames for basic object detection.
