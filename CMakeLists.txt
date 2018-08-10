cmake_minimum_required(VERSION 2.8)

include_directories(glad lodepng)

add_executable(main glad/egl.c glad/gl.c lodepng/lodepng.cpp egl_example.cpp)
target_link_libraries(main dl pthread)