cmake_minimum_required(VERSION 3.28.0)

project(TP1 VERSION 0.1)


set(CMAKE_CXX_STANDARD_20)

add_executable(TP1
        src/main.cpp
)
target_link_libraries(TP1 glfw GL GLEW)
