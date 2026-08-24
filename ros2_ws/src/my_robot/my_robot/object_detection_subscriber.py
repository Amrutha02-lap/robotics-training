import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class ObjectDetectionSubscriber(Node):

    def __init__(self):
        super().__init__('object_detection_subscriber')

        self.subscription = self.create_subscription(
            String,
            'object_detection',
            self.listener_callback,
            10
        )

        self.cmd_vel_publisher = self.create_publisher(
            Twist,
            'cmd_vel',
             10
        )

    def listener_callback(self, msg):

        self.get_logger().info(
            f'Received: {msg.data}'
        )

        velocity = Twist()

        if msg.data == "OBJECT DETECTED":
            velocity.linear.x = 0.0
            velocity.angular.z = 0.0
            self.get_logger().info("Robot Action: STOP")

        else:
            velocity.linear.x = 0.2
            velocity.angular.z = 0.0
            self.get_logger().info("Robot Action: CONTINUE")

        self.cmd_vel_publisher.publish(velocity)


def main(args=None):
    rclpy.init(args=args)

    node = ObjectDetectionSubscriber()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
