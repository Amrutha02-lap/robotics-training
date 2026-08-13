import os
from glob import glob
from setuptools import find_packages, setup

from setuptools import find_packages, setup

package_name = 'my_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
       (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='amrutha',
    maintainer_email='amruthasprasad01@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
		'hello_node = my_robot.hello_node:main',
                'talker = my_robot.talker:main',
        	'listener = my_robot.listener:main',
		'service_server = my_robot.service_server:main',
		'service_client = my_robot.service_client:main',
                'parameter_node = my_robot.parameter_node:main',
                'velocity_publisher = my_robot.velocity_publisher:main',
                'lidar_publisher = my_robot.lidar_publisher:main',
 ],
    },
)
