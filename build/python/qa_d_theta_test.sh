#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/chris/workspace/GNURadio/gr-eecs/python
export PATH=/home/chris/workspace/GNURadio/gr-eecs/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/chris/workspace/GNURadio/gr-eecs/build/swig:$PYTHONPATH
/usr/bin/python /home/chris/workspace/GNURadio/gr-eecs/python/qa_d_theta.py 
