import launch
from launch.substitutions import LaunchConfiguration, Command
import launch_ros
import os

def generate_launch_description():
  pkg_share = launch_ros.substitutions.FindPackageShare(package='hbot_description').find('hbot_description')
  default_model_path = os.path.join(pkg_share, 'urdf', 'hbot.urdf')
  default_rviz_config_path = os.path.join(pkg_share, 'rviz', 'hbot.rviz')

  print('default_model_path : {}'.format(default_model_path))

  robot_state_publisher_node = launch_ros.actions.Node(
    package='robot_state_publisher',
    executable='robot_state_publisher',
    name='robot_state_publisher',
    parameters=[{'robot_description': Command(['xacro', ' ', LaunchConfiguration('model')])}]
  )
  # joint_state_publisher_node = launch_ros.actions.Node(
  #   package='joint_state_publisher',
  #   executable='joint_state_publisher',
  #   name='joint_state_publisher',
  #   condition=launch.conditions.UnlessCondition(LaunchConfiguration('gui'))
  # )
  rviz_node = launch_ros.actions.Node(
    package='rviz2',
    executable='rviz2',
    name='rviz2',
    output='screen',
    arguments=['-d', LaunchConfiguration('rvizconfig')],
    condition=launch.conditions.IfCondition(LaunchConfiguration('rviz'))
  )
  return launch.LaunchDescription([
    launch.actions.DeclareLaunchArgument(name='model', default_value=default_model_path,
                                          description='Absolute path to robot urdf file'),
    launch.actions.DeclareLaunchArgument(name='rvizconfig', default_value=default_rviz_config_path,
                                          description='Absolute path to rviz config file'),
    launch.actions.DeclareLaunchArgument(name='rviz', default_value='false',
                                          description='Open RViz?'),
    # joint_state_publisher_node,
    robot_state_publisher_node,
    rviz_node
  ])