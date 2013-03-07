#!/bin/sh
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/sdr/workspace/GNURadio/python
export PATH=/home/sdr/workspace/GNURadio/build/python:$PATH
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export DYLD_LIBRARY_PATH=$LD_LIBRARY_PATH:$DYLD_LIBRARY_PATH
export PYTHONPATH=/home/sdr/workspace/GNURadio/build/swig:$PYTHONPATH
/usr/bin/python2.7 /home/sdr/workspace/GNURadio/python/qa_d_theta.py 
