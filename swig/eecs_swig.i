/* -*- c++ -*- */

#define EECS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "eecs_swig_doc.i"

%{
#include "eecs/d_theta.h"
%}


%include "eecs/d_theta.h"
GR_SWIG_BLOCK_MAGIC2(eecs, d_theta);
