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
#include "xcor_inversion_cc_impl.h"
#include <cmath>
#include <complex>

namespace gr {
  namespace eecs {

    xcor_inversion_cc::sptr
    xcor_inversion_cc::make(int nSamples)
    {
      return gnuradio::get_initial_sptr (new xcor_inversion_cc_impl(nSamples));
    }

    xcor_inversion_cc_impl::xcor_inversion_cc_impl(int nSamples)
      : gr_sync_block("xcor_inversion_cc",
		      gr_make_io_signature(2, 2, sizeof (gr_complex)),
		      gr_make_io_signature(2, 2, sizeof (gr_complex))),
		      p_nSamples(nSamples)
    {
	set_history(p_nSamples);
	}

    xcor_inversion_cc_impl::~xcor_inversion_cc_impl()
    {
    }

    int
    xcor_inversion_cc_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *Sat1 = (const gr_complex *) input_items[0];
        const gr_complex *Sat2 = (const gr_complex *) input_items[1];
		gr_complex *out1 = (gr_complex *) output_items[0];
		gr_complex *out2 = (gr_complex *) output_items[1];
        Sat1 += p_nSamples; Sat2 += p_nSamples;
        
		int offset = 0;
		bool invert;
        offset = xcorr(Sat1, Sat2, invert);
		     
        for(int i = 0; i <noutput_items; i++){
			if (invert){
				out1[i] = Sat1[i]*gr_complex(cos(M_PI), sin(0));
				out2[i] = Sat2[i-offset];
			}
			else{
				out1[i] = Sat1[i];
				out2[i] = Sat2[i-offset];
			}
		}  
        return noutput_items;
    }

	int xcor_inversion_cc_impl::xcorr(const gr_complex* ir1, const gr_complex* r2, bool iflag)
	{
		gr_complex r1[2*p_nSamples-1];
		gr_complex xout[2*p_nSamples-1];
		gr_complex xout_inv[2*p_nSamples-1];
		float max_val = 0;	float max_val_inv = 0;
		int max_index = 0; 	int max_index_inv = 0;
		
		// complex conjugate
		for (int i = 0; i < p_nSamples-1; i++){
			r1[i] = conj(ir1[i]);}
		//cross correlate	
		for(int i = 0; i < p_nSamples-1; i++){							
			xout[i] 	= 0;
			xout_inv[i] = 0;												
			for (int j = 0; j < i; j++){								
				xout[i] 	= xout[i]+ 		r1[i-j]*r2[p_nSamples-j];
				xout_inv[i] = xout_inv[i]+ 	r1[i-j]*r2[p_nSamples-j]*gr_complex(cos(M_PI), sin(0));					
		}}	
		for(int i = -1; i < p_nSamples-2; i++){							
			xout[p_nSamples+i-1] = 0;
			xout_inv[p_nSamples+i-1] = 0;										
			for(int j = 0; j < (p_nSamples-i-1); j++){					
			  xout[p_nSamples+i-1] 		= xout[p_nSamples+i-1] 		+ r1[i+j]*r2[j];
			  xout_inv[p_nSamples+i-1] 	= xout_inv[p_nSamples+i-1] 	+ r1[i+j]*r2[j]*gr_complex(cos(M_PI), sin(0));   		
					}}
	
		// Find the sample Shift
		for (int i = 0; i < 2*p_nSamples-1; i++){	
			if (real(xout[i]) > max_val){
				max_val = real(xout[i]);
				max_index = i;
			}
			if (real(xout_inv[i]) > max_val_inv){
				max_val_inv = real(xout_inv[i]);
				max_index_inv = i;
			}
		}
		// pass the highest correlator
		if (max_val_inv > max_val){
			max_index = max_index_inv;
			iflag = 1;
		}
		// Return Shift	
		if (max_index > p_nSamples/* || max_index == p_nSamples*/)//theta pos
			return -1*(p_nSamples-1 - max_index);
		else 								//theta neg
			return -1*(p_nSamples-1 - max_index);
	}

	int xcor_inversion_cc_impl::findTheta(gr_complex sig[]){
		float max_val = 0;
		int max_index = 0;
		
		for (int i = 0; i < 2*p_nSamples-1; i++){	
			if (real(sig[i]) > max_val){
				max_val = real(sig[i]);
				max_index = i;
		}}
		if (max_index > p_nSamples/* || max_index == p_nSamples*/)//theta pos
			return -1*(p_nSamples-1 - max_index);
		else 								//theta neg
			return -1*(p_nSamples-1 - max_index);
	}
	
	void xcor_inversion_cc_impl::set_nSamples(int nSamples)
	{	p_nSamples = nSamples;}
  } /* namespace eecs */
} /* namespace gr */

