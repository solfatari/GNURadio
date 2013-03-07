#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/sdr/workspace/GNURadio/lib
export PATH=/home/sdr/workspace/GNURadio/build/lib:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-eecs 
