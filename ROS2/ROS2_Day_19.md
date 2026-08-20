		  Day 19 - Basic Object Detection Using OpenCV

## Topics Practiced
- Basic object detection using OpenCV
- Contour detection
- Bounding rectangles
- Filtering small contours

## Processing Flow
Image
→ Grayscale
→ Gaussian Blur
→ Canny Edge Detection
→ Find Contours
→ Filter Small Contours
→ Draw Bounding Boxes
→ Save Output

## Functions Used

### cv2.findContours()
Used to find connected boundaries or contours from the edge-detected image.

### cv2.boundingRect()
Used to get the x-position, y-position, width, and height of a contour.

### cv2.rectangle()
Used to draw a rectangle around the detected region.

## Learning Outcome
Understood how basic image processing can be extended to locate object regions using contours and bounding boxes.
