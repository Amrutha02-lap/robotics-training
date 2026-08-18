			 Day 18 - OpenCV Image Processing

## Topics Practiced
- Basic image processing using OpenCV
- Grayscale image conversion
- Gaussian Blur
- Canny Edge Detection
- Saving processed images

## Functions Used

### cv2.cvtColor()
Used to convert the original color image into grayscale.

### cv2.GaussianBlur()
Used to reduce image noise and smooth the image before edge detection.

Syntax used:
cv2.GaussianBlur(gray, (5, 5), 0)

- gray: input grayscale image
- (5, 5): kernel size
- 0: lets OpenCV determine the Gaussian sigma

### cv2.Canny()
Used to detect edges or boundaries in an image.

Syntax used:
cv2.Canny(blurred, 50, 150)

- blurred: input image
- 50: lower threshold
- 150: upper threshold

## Processing Flow

Original Image
→ Grayscale
→ Gaussian Blur
→ Canny Edge Detection
→ Save Processed Images

## Learning Outcome
Understood why image smoothing is performed before edge detection and practiced basic OpenCV image-processing functions.
