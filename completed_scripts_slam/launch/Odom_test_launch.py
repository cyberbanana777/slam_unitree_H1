from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Node 1. teleop_twist_keyboard.
    teleop_twist_keyboard_node = Node(
        package="teleop_twist_keyboard",
        executable="teleop_twist_keyboard"
    )

    # Node 2. Converter from /cmd to /odom. 
    cmd_to_odom_node = Node(
        package="cmd_to_odom_package",
        executable="cmd_to_odom_node"
    )
    
    # Node 3. 
        


    return LaunchDescription([
        teleop_twist_keyboard_node,
        cmd_to_odom_node
    ])

