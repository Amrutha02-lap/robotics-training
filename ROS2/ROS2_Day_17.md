		Day 17 - Computer Vision and OpenCV Basics

## Topics Practiced
- Introduction to Computer Vision
- Introduction to OpenCV
- Verified OpenCV installation
- Loaded an image using OpenCV
- Checked image dimensions
- Converted a color image to grayscale
- Resized an image
- Saved processed images

## Commands Used

Check OpenCV version:
python3 -c "import cv2; print(cv2.__version__)"

Run the Python program:
python3 opencv_basics.py

## OpenCV Functions Used

- cv2.imread() - Reads an image from a file.
- image.shape - Gives image height, width, and number of channels.
- cv2.cvtColor() - Converts an image from one color format to another.
- cv2.imwrite() - Saves an image to a file.
- cv2.resize() - Changes the dimensions of an image.

## Result

Successfully loaded a 160 x 160 color image, converted it to grayscale,
resized it to 100 x 100 pixels, and saved the processed images.
