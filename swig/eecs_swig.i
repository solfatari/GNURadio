/* -*- c++ -*- */

#define EECS_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "eecs_swig_doc.i"

%{
#include "eecs/d_theta.h"
#include "eecs/phase_shifter.h"
#include "eecs/rev_phase_shifter.h"
#include "eecs/x_corr.h"
%}


%include "eecs/d_theta.h"
GR_SWIG_BLOCK_MAGIC2(eecs, d_theta);
%include "eecs/phase_shifter.h"
GR_SWIG_BLOCK_MAGIC2(eecs, phase_shifter);
%include "eecs/rev_phase_shifter.h"
GR_SWIG_BLOCK_MAGIC2(eecs, rev_phase_shifter);
%include "eecs/x_corr.h"
GR_SWIG_BLOCK_MAGIC2(eecs, x_corr);
