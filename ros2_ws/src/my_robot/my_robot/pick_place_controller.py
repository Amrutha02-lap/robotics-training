import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PickPlaceController(Node):

    def __init__(self):
        super().__init__('pick_place_controller')

        self.subscription = self.create_subscription(
            String,
            'object_detection',
            self.detection_callback,
            10
        )

        self.state = "SEARCHING"

        self.get_logger().info(
            "Pick and Place Controller Started"
        )

    def detection_callback(self, msg):

        self.get_logger().info(
            f"Detection received: {msg.data}"
        )

        if msg.data == "OBJECT DETECTED":
            self.state = "MOVING_TO_OBJECT"

            self.get_logger().info(
                "State changed: SEARCHING -> MOVING_TO_OBJECT"
            )

def main(args=None):
    rclpy.init(args=args)

    node = PickPlaceController()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
