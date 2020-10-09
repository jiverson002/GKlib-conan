cmake_minimum_required(VERSION 2.8.12)
project(PackageTest C)

include(${CMAKE_BINARY_DIR}/conan_paths.cmake)

find_package(GKlib CONFIG REQUIRED)

add_executable(example example.c)
target_link_libraries(example GKlib::GKlib)

# CTest is a testing tool that can be used to test your project.
# enable_testing()
# add_test(NAME example
#          WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/bin
#          COMMAND example)
