# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.8

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/sdr/workspace/GNURadio

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/sdr/workspace/GNURadio/build

# Include any dependencies generated for this target.
include lib/CMakeFiles/test-eecs.dir/depend.make

# Include the progress variables for this target.
include lib/CMakeFiles/test-eecs.dir/progress.make

# Include the compile flags for this target's objects.
include lib/CMakeFiles/test-eecs.dir/flags.make

lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o: lib/CMakeFiles/test-eecs.dir/flags.make
lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o: ../lib/test_eecs.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sdr/workspace/GNURadio/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o"
	cd /home/sdr/workspace/GNURadio/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/test-eecs.dir/test_eecs.cc.o -c /home/sdr/workspace/GNURadio/lib/test_eecs.cc

lib/CMakeFiles/test-eecs.dir/test_eecs.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-eecs.dir/test_eecs.cc.i"
	cd /home/sdr/workspace/GNURadio/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/sdr/workspace/GNURadio/lib/test_eecs.cc > CMakeFiles/test-eecs.dir/test_eecs.cc.i

lib/CMakeFiles/test-eecs.dir/test_eecs.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-eecs.dir/test_eecs.cc.s"
	cd /home/sdr/workspace/GNURadio/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/sdr/workspace/GNURadio/lib/test_eecs.cc -o CMakeFiles/test-eecs.dir/test_eecs.cc.s

lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.requires:
.PHONY : lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.requires

lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.provides: lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-eecs.dir/build.make lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.provides

lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.provides.build: lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o
.PHONY : lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.provides.build

lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o: lib/CMakeFiles/test-eecs.dir/flags.make
lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o: ../lib/qa_eecs.cc
	$(CMAKE_COMMAND) -E cmake_progress_report /home/sdr/workspace/GNURadio/build/CMakeFiles $(CMAKE_PROGRESS_2)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o"
	cd /home/sdr/workspace/GNURadio/build/lib && /usr/bin/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/test-eecs.dir/qa_eecs.cc.o -c /home/sdr/workspace/GNURadio/lib/qa_eecs.cc

lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/test-eecs.dir/qa_eecs.cc.i"
	cd /home/sdr/workspace/GNURadio/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /home/sdr/workspace/GNURadio/lib/qa_eecs.cc > CMakeFiles/test-eecs.dir/qa_eecs.cc.i

lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/test-eecs.dir/qa_eecs.cc.s"
	cd /home/sdr/workspace/GNURadio/build/lib && /usr/bin/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /home/sdr/workspace/GNURadio/lib/qa_eecs.cc -o CMakeFiles/test-eecs.dir/qa_eecs.cc.s

lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.requires:
.PHONY : lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.requires

lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.provides: lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.requires
	$(MAKE) -f lib/CMakeFiles/test-eecs.dir/build.make lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.provides.build
.PHONY : lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.provides

lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.provides.build: lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o
.PHONY : lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.provides.build

# Object files for target test-eecs
test__eecs_OBJECTS = \
"CMakeFiles/test-eecs.dir/test_eecs.cc.o" \
"CMakeFiles/test-eecs.dir/qa_eecs.cc.o"

# External object files for target test-eecs
test__eecs_EXTERNAL_OBJECTS =

lib/test-eecs: lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o
lib/test-eecs: lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o
lib/test-eecs: /usr/local/lib/libgnuradio-core.so
lib/test-eecs: /usr/lib64/libboost_filesystem-mt.so
lib/test-eecs: /usr/lib64/libboost_system-mt.so
lib/test-eecs: /usr/lib/libcppunit.so
lib/test-eecs: lib/libgnuradio-eecs.so
lib/test-eecs: /usr/lib64/libboost_filesystem-mt.so
lib/test-eecs: /usr/lib64/libboost_system-mt.so
lib/test-eecs: /usr/local/lib/libgruel.so
lib/test-eecs: /usr/local/lib/libgnuradio-core.so
lib/test-eecs: lib/CMakeFiles/test-eecs.dir/build.make
lib/test-eecs: lib/CMakeFiles/test-eecs.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable test-eecs"
	cd /home/sdr/workspace/GNURadio/build/lib && $(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/test-eecs.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
lib/CMakeFiles/test-eecs.dir/build: lib/test-eecs
.PHONY : lib/CMakeFiles/test-eecs.dir/build

lib/CMakeFiles/test-eecs.dir/requires: lib/CMakeFiles/test-eecs.dir/test_eecs.cc.o.requires
lib/CMakeFiles/test-eecs.dir/requires: lib/CMakeFiles/test-eecs.dir/qa_eecs.cc.o.requires
.PHONY : lib/CMakeFiles/test-eecs.dir/requires

lib/CMakeFiles/test-eecs.dir/clean:
	cd /home/sdr/workspace/GNURadio/build/lib && $(CMAKE_COMMAND) -P CMakeFiles/test-eecs.dir/cmake_clean.cmake
.PHONY : lib/CMakeFiles/test-eecs.dir/clean

lib/CMakeFiles/test-eecs.dir/depend:
	cd /home/sdr/workspace/GNURadio/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/sdr/workspace/GNURadio /home/sdr/workspace/GNURadio/lib /home/sdr/workspace/GNURadio/build /home/sdr/workspace/GNURadio/build/lib /home/sdr/workspace/GNURadio/build/lib/CMakeFiles/test-eecs.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : lib/CMakeFiles/test-eecs.dir/depend

