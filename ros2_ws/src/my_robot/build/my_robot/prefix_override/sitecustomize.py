import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/amrutha/robotics-training/ros2_ws/src/my_robot/install/my_robot'
