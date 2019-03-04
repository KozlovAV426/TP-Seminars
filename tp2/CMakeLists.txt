cmake_minimum_required(VERSION 2.8)
								
project(final)				

set(SOURCE_EXE C/main.cpp A/index.cpp)			

include_directories("${PROJECT_SOURCE_DIR}")

EXECUTE_PROCESS(COMMAND python "${PROJECT_SOURCE_DIR}/A/preparing.py"
WORKING_DIRECTORY "${PROJECT_SOURCE_DIR}/A")

add_executable(main ${SOURCE_EXE})	

add_subdirectory(B)				

target_link_libraries(main lib)	
