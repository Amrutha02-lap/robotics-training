import rclpy
from rclpy.node import Node


class ParameterNode(Node):

    def __init__(self):
        super().__init__('parameter_node')

        self.declare_parameter('robot_name', 'AmruthaBot')

        robot_name = self.get_parameter('robot_name').value

        self.get_logger().info(f'Robot name: {robot_name}')


def main(args=None):
    rclpy.init(args=args)

    node = ParameterNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
