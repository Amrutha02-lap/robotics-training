import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class VelocityPublisher(Node):

    def __init__(self):
        super().__init__('velocity_publisher')

        self.publisher_ = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_velocity)

    def publish_velocity(self):
        msg = Twist()

        msg.linear.x = 1.0
        msg.angular.z = 1.0

        self.publisher_.publish(msg)

        self.get_logger().info(
            'Publishing velocity: linear=1.0 angular=1.0'
        )


def main(args=None):
    rclpy.init(args=args)

    node = VelocityPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
