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
#include "eecs/xcor2.h"
#include "eecs/max_energy.h"
#include "eecs/xcorr_vec.h"
#include "eecs/max_vec.h"
#include "eecs/fft_max.h"
#include "eecs/fft_shift.h"
%}


%include "eecs/d_theta.h"
GR_SWIG_BLOCK_MAGIC2(eecs, d_theta);
%include "eecs/phase_shifter.h"
GR_SWIG_BLOCK_MAGIC2(eecs, phase_shifter);
%include "eecs/rev_phase_shifter.h"
GR_SWIG_BLOCK_MAGIC2(eecs, rev_phase_shifter);
%include "eecs/x_corr.h"
GR_SWIG_BLOCK_MAGIC2(eecs, x_corr);

%include "eecs/xcor2.h"
GR_SWIG_BLOCK_MAGIC2(eecs, xcor2);

%include "eecs/max_energy.h"
GR_SWIG_BLOCK_MAGIC2(eecs, max_energy);
%include "eecs/xcorr_vec.h"
GR_SWIG_BLOCK_MAGIC2(eecs, xcorr_vec);
%include "eecs/max_vec.h"
GR_SWIG_BLOCK_MAGIC2(eecs, max_vec);
%include "eecs/fft_max.h"
GR_SWIG_BLOCK_MAGIC2(eecs, fft_max);
%include "eecs/fft_shift.h"
GR_SWIG_BLOCK_MAGIC2(eecs, fft_shift);
