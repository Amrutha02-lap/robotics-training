import cv2

image = cv2.imread("test_images.jpeg")

if image is None:
    print("Image could not be loaded.")

else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred, 50, 150)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        if w > 20 and h > 20:
            cv2.rectangle(
                image,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

    cv2.imwrite("detected_objects.jpg", image)

    print("Objects detected:", len(contours))
    print("Detected image saved.")
