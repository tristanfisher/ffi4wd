cmake_minimum_required(VERSION 3.2)
project(cpp)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -I/usr/local/Cellar/python3/3.4.3/Frameworks/Python.framework/Versions/3.4/include/python3.4m -framework Python")

set(SOURCE_FILES main.cpp)
add_executable(cpp ${SOURCE_FILES})