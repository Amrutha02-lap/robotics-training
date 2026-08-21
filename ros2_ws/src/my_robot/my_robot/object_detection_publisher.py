import cv2
import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class ObjectDetectionPublisher(Node):

    def __init__(self):
        super().__init__('object_detection_publisher')

        self.publisher_ = self.create_publisher(
            String,
            'object_detection',
            10
        )

        self.timer = self.create_timer(
            2.0,
            self.detect_and_publish
        )

    def detect_and_publish(self):

        image = cv2.imread(
            '/home/amrutha/robotics-training/Python/test_images.jpeg'
        )

        if image is None:
            self.get_logger().error("Image could not be loaded")
            return

        gray = cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

        blurred = cv2.GaussianBlur(
            gray,
            (5, 5),
            0
        )

        edges = cv2.Canny(
            blurred,
            50,
            150
        )

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
                break

        msg = String()

        if object_detected:
            msg.data = "OBJECT DETECTED"
        else:
            msg.data = "NO OBJECT DETECTED"

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Published: {msg.data}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = ObjectDetectionPublisher()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
