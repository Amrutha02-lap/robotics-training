		 Day 20 - Object Detection and System Response

## Topics Practiced
- OpenCV image processing
- Contour-based object detection
- Bounding box detection
- Boolean decision logic
- Simple system response

## Processing Flow
Image
→ Grayscale
→ Gaussian Blur
→ Canny Edge Detection
→ Find Contours
→ Filter Contours
→ Detect Object Region
→ Trigger Response
→ Save Output Image

## Important Concepts

### object_detected
A Boolean variable used to store whether a valid object region was detected.

### cv2.boundingRect()
Returns the x-position, y-position, width and height of a contour.

### Detection Condition
Contours with width and height greater than 20 pixels were considered valid regions.

### System Response
When a valid region was detected, the program generated a simple response message.

## Learning Outcome
Learned how image processing and contour detection can be combined with Python decision logic to trigger a simple response when an object region is detected.
