cmake_minimum_required(VERSION 3.10)

project(CMake_Test)

add_executable(CMake_Test main.cpp)

set(CMAKE_C_COMPILER gcc)
set(CMAKE_CXX_COMPILER g++)

set(CMAKE_BUILD_TYPE "Debug")