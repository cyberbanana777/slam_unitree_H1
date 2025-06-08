from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    # Step 0. Init LiDAR.
    # Укажите имя пакета и путь к launch-файлу внутри него
    package_name = "livox_ros_driver2"
    launch_file = "msg_MID360_launch.py"
    # Сформируйте полный путь к файлу
    path_to_launch = PathJoinSubstitution([
        FindPackageShare(package_name),
        'launch',  # стандартная папка для launch-файлов
        launch_file
    ])
    # Включите целевой launch-файл
    livox_ros_driver2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([path_to_launch]),
    )


    # Step 1. First converter. 
    livox_to_pointcloud2_node = Node(
            package="livox_to_pointcloud2",
            executable="livox_to_pointcloud2_node"
    )

    
    # Step 2. Second converter. 
    package_name = "pointcloud_to_laserscan"
    launch_file = "sample_pointcloud_to_laserscan_launch.py"
    # Сформируйте полный путь к файлу
    path_to_launch = PathJoinSubstitution([
        FindPackageShare(package_name),
        'launch',  # стандартная папка для launch-файлов
        launch_file
    ])
    # Включите целевой launch-файл
    pointcloud_to_laserscan_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([path_to_launch]),
    )

    return LaunchDescription([
        livox_ros_driver2_launch,
        livox_to_pointcloud2_node,
        pointcloud_to_laserscan_launch,
    ])

