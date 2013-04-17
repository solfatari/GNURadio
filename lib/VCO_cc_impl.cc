/* -*- c++ -*- */
/* 
 * Copyright 2013 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gr_io_signature.h>
#include "VCO_cc_impl.h"
#include <math.h>

namespace gr {
  namespace eecs {

    VCO_cc::sptr
    VCO_cc::make(float sampRate)
    {
      return gnuradio::get_initial_sptr (new VCO_cc_impl(sampRate));
    }

    /*
     * The private constructor
     */
    VCO_cc_impl::VCO_cc_impl(float sampRate)
      : gr_sync_block("VCO_cc",
		      gr_make_io_signature(1, 1, sizeof (float)),
		      gr_make_io_signature(2, 2, sizeof (float))),
		      p_sampRate(sampRate)
    { d_vcos.set_phase(M_PI/2);}

    /*
     * Our virtual destructor.
     */
    VCO_cc_impl::~VCO_cc_impl()
    {
    }

    int
    VCO_cc_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in = (const float *) input_items[0];
        float *outr = (float *) output_items[0];
        float *outi = (float *) output_items[1];
		
	//	float (*cos_out)[noutput_items];
	//		cos_out = (float*)malloc(noutput_items*sizeof(float));
	//	float (*sin_out)[noutput_items];
	//		sin_out = (float*)malloc(noutput_items*sizeof(float));
	//	gr_complex (*comp)[noutput_items];
	//		comp = (gr_complex*)malloc(noutput_items*sizeof(gr_complex));
	//
 //      d_vcoc.cos(cos_out, in, noutput_items, 1/p_sampRate, 1);
 //      d_vcos.cos(sin_out, in, noutput_items, 1/p_sampRate, 1);
       
       d_vcoc.cos(outr, in, noutput_items, 1/p_sampRate, 1);
       d_vcos.cos(outi, in, noutput_items, 1/p_sampRate, 1);
 
    
        return noutput_items;
    }
    
	void VCO_cc_impl::set_sampRate(float sampRate)
	{	p_sampRate = sampRate;	}
	
  } /* namespace eecs */
} /* namespace gr */

