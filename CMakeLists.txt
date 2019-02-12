cmake_minimum_required(VERSION 2.8)
find_package(OpenGL)

include_directories(glad lodepng)

add_executable(main glad/egl.c glad/gl.c lodepng/lodepng.cpp egl_example.cpp)
add_executable(query_devices glad/egl.c glad/gl.c lodepng/lodepng.cpp query_devices.cpp)
add_executable(test_device glad/egl.c glad/gl.c lodepng/lodepng.cpp test_device.cpp)

target_link_libraries(main dl pthread EGL ${OPENGL_LIBRARIES})
target_link_libraries(query_devices dl pthread EGL ${OPENGL_LIBRARIES})
target_link_libraries(test_device dl pthread EGL ${OPENGL_LIBRARIES})