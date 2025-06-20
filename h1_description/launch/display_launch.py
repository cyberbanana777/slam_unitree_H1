import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    pkg_path = get_package_share_directory('h1_description')
    urdf_file = os.path.join(pkg_path, 'urdf', 'h1_with_hand.urdf')
    rviz_config = os.path.join(pkg_path, 'rviz', 'check_joint.rviz')

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config]
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments=['0.0', '0.0', '0.0', '0.0', '0.0', '0.0', 'odom_frame', 'pelvis']
        )

    ])
