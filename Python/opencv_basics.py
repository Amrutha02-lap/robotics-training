import cv2

print("OpenCV version:", cv2.__version__)

image_path = "test_images.jpeg"

image = cv2.imread(image_path)

if image is None:
    print("Image could not be loaded.")
else:
    print("Image loaded successfully.")
    print("Image shape:", image.shape)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imwrite("gray_image.jpg", gray)

    print("Grayscale image saved successfully.")

    resized = cv2.resize(image, (100, 100))

    cv2.imwrite("resized_image.jpg", resized)

    print("Resized image saved successfully.")
