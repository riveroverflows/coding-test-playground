cmake_minimum_required(VERSION 3.20)
project(coding-test-playground CXX)

# 프로그래머스 C++ 컴파일 환경: Clang++ 10.0, C++17
# clang++ -std=c++17 -O2 -Wno-unused-result
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
add_compile_options(-O2 -Wno-unused-result)

# 각 .cpp 파일을 독립 실행파일로 빌드 (CLion에서 개별 Run/Debug 가능)
file(GLOB_RECURSE CPP_SOURCES
    "${CMAKE_SOURCE_DIR}/leetcode/*.cpp"
    "${CMAKE_SOURCE_DIR}/boj/*.cpp"
    "${CMAKE_SOURCE_DIR}/programmers/*.cpp"
    "${CMAKE_SOURCE_DIR}/code-up/*.cpp"
    "${CMAKE_SOURCE_DIR}/book-codingtest-python/*.cpp"
)

foreach(source ${CPP_SOURCES})
    file(RELATIVE_PATH rel_path "${CMAKE_SOURCE_DIR}" "${source}")
    string(REPLACE "/" "_" target_name "${rel_path}")
    string(REPLACE ".cpp" "" target_name "${target_name}")
    add_executable(${target_name} ${source})
    set_target_properties(${target_name} PROPERTIES SUFFIX ".out")
endforeach()