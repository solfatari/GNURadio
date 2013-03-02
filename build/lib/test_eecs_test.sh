#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/chris/workspace/GNURadio/gr-eecs/lib
export PATH=/home/chris/workspace/GNURadio/gr-eecs/build/lib:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-eecs 
