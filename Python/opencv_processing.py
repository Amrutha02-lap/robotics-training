import cv2

image = cv2.imread("test_images.jpeg")

if image is None:
    print("Image could not be loaded.")

else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred, 50, 150)

    cv2.imwrite("blurred_image.jpg", blurred)
    cv2.imwrite("edge_image.jpg", edges)

    print("Blurred image saved.")
    print("Edge detected image saved.")
