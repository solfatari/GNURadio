#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/matthew/workspace/GNURadio/python
export PATH=/home/matthew/workspace/GNURadio/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/matthew/workspace/GNURadio/build/swig:$PYTHONPATH
/usr/bin/python /home/matthew/workspace/GNURadio/python/qa_d_theta.py 
