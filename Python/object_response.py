import cv2

image = cv2.imread("test_images.jpeg")

if image is None:
    print("The image could not be loaded")

else:
    print("The image loaded successfully")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    object_detected = False

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        if w > 20 and h > 20:
            object_detected = True

            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    if object_detected:
        print("Object detected!")
        print("System response: Object found in camera image.")
    else:
        print("No object detected.")

    cv2.imwrite("object_response.jpg", image)
    print("Output image saved.")
