cmake_minimum_required(VERSION 3.8)
project(hbot_description)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

message(STATUS ${CMAKE_SOURCE_DIR}/urdf)
install(CODE "
    execute_process(
    COMMAND bash -c \"xacro hbot.urdf.xacro > hbot.urdf && gz sdf -p hbot.urdf > hbot.sdf\"
    WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/urdf
    )"
  DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY launch rviz urdf
  DESTINATION share/${PROJECT_NAME}
)
ament_package()
