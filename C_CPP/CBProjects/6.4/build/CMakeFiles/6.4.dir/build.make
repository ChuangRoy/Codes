# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.22

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake.exe

# The command to remove a file.
RM = /usr/bin/cmake.exe -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/s0415/Codes/C_CPP/CBProjects/6.4

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/s0415/Codes/C_CPP/CBProjects/6.4/build

# Include any dependencies generated for this target.
include CMakeFiles/6.4.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/6.4.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/6.4.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/6.4.dir/flags.make

CMakeFiles/6.4.dir/main.cpp.o: CMakeFiles/6.4.dir/flags.make
CMakeFiles/6.4.dir/main.cpp.o: ../main.cpp
CMakeFiles/6.4.dir/main.cpp.o: CMakeFiles/6.4.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/s0415/Codes/C_CPP/CBProjects/6.4/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/6.4.dir/main.cpp.o"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/6.4.dir/main.cpp.o -MF CMakeFiles/6.4.dir/main.cpp.o.d -o CMakeFiles/6.4.dir/main.cpp.o -c /home/s0415/Codes/C_CPP/CBProjects/6.4/main.cpp

CMakeFiles/6.4.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/6.4.dir/main.cpp.i"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/s0415/Codes/C_CPP/CBProjects/6.4/main.cpp > CMakeFiles/6.4.dir/main.cpp.i

CMakeFiles/6.4.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/6.4.dir/main.cpp.s"
	/usr/bin/c++.exe $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/s0415/Codes/C_CPP/CBProjects/6.4/main.cpp -o CMakeFiles/6.4.dir/main.cpp.s

# Object files for target 6.4
6_4_OBJECTS = \
"CMakeFiles/6.4.dir/main.cpp.o"

# External object files for target 6.4
6_4_EXTERNAL_OBJECTS =

6.4.exe: CMakeFiles/6.4.dir/main.cpp.o
6.4.exe: CMakeFiles/6.4.dir/build.make
6.4.exe: CMakeFiles/6.4.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/s0415/Codes/C_CPP/CBProjects/6.4/build/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable 6.4.exe"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/6.4.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/6.4.dir/build: 6.4.exe
.PHONY : CMakeFiles/6.4.dir/build

CMakeFiles/6.4.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/6.4.dir/cmake_clean.cmake
.PHONY : CMakeFiles/6.4.dir/clean

CMakeFiles/6.4.dir/depend:
	cd /home/s0415/Codes/C_CPP/CBProjects/6.4/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/s0415/Codes/C_CPP/CBProjects/6.4 /home/s0415/Codes/C_CPP/CBProjects/6.4 /home/s0415/Codes/C_CPP/CBProjects/6.4/build /home/s0415/Codes/C_CPP/CBProjects/6.4/build /home/s0415/Codes/C_CPP/CBProjects/6.4/build/CMakeFiles/6.4.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/6.4.dir/depend
