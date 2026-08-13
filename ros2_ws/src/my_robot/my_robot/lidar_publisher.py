import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan


class LidarPublisher(Node):

    def __init__(self):
        super().__init__('lidar_publisher')

        self.publisher_ = self.create_publisher(
            LaserScan,
            '/scan',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_scan
        )

    def publish_scan(self):

        msg = LaserScan()

        msg.angle_min = -1.57
        msg.angle_max = 1.57
        msg.angle_increment = 0.785

        msg.range_min = 0.1
        msg.range_max = 10.0

        msg.ranges = [1.0, 2.0, 1.5, 3.0, 2.5]

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'Publishing LiDAR ranges: {msg.ranges}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = LidarPublisher()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
