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
#include "xcor2_impl.h"
#include <cmath>
#include <complex>

namespace gr {
  namespace eecs {

    xcor2::sptr
    xcor2::make(float sampRate,
				int nSamples)
    {
      return gnuradio::get_initial_sptr (new xcor2_impl(sampRate,
													    nSamples));
    }

    xcor2_impl::xcor2_impl(float sampRate,
							int nSamples)
      : gr_sync_block("xcor2",
		      gr_make_io_signature(2, 2, sizeof (gr_complex)),
		      gr_make_io_signature(2, 2, sizeof (gr_complex))),
		      p_sampRate(sampRate), p_nSamples(nSamples)
    {
	set_history(p_nSamples);
	}

    xcor2_impl::~xcor2_impl()
    {
    }

    int
    xcor2_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *Sat1 = (const gr_complex *) input_items[0];
        const gr_complex *Sat2 = (const gr_complex *) input_items[1];
		gr_complex *out1 = (gr_complex *) output_items[0];
		gr_complex *out2 = (gr_complex *) output_items[1];
        
        Sat1 += p_nSamples; Sat2 += p_nSamples;
        
        gr_complex xcor[2*p_nSamples];
		int offset;
        xcorr(Sat1, Sat2, xcor);
		offset =findTheta(xcor);
        
        for(int i = 0; i <noutput_items; i++){
			out1[i] = Sat1[i];
			out2[i] = Sat2[i-offset];
		}  
       
        return noutput_items;
    }

	void xcor2_impl::xcorr(const gr_complex* r1, const gr_complex* r2, gr_complex xout[])
	{
		//gr_complex r1;
		//	r1 = gnuradio.gr.conjugate_cc(ir1);
		
		for(int i = 0; i < p_nSamples-1; i++){							
			xout[i] = 0;												
			for (int j = 0; j <= i; j++){								
				xout[i] = xout[i]+ r1[i-j]*r2[p_nSamples-j];					
		}}	
		for(int i = 0; i < p_nSamples-2; i++){							
			xout[p_nSamples+i] = 0;										
			for(int j = 0; j < (p_nSamples-1-i); j++){					
			  xout[p_nSamples+i] += r1[p_nSamples-1 +i]*r2[j];  		
					}}
	}

	int xcor2_impl::findTheta(gr_complex sig[]){
		float max_val = 0;
		int max_index = 0;
		
		for (int i = 0; i < 2*p_nSamples-1; i++){							//for i = 1:len
			if (abs(sig[i]) > max_val){
				max_val = abs(sig[i]);
				max_index = i;
		}}
		if (max_index < p_nSamples)
			return -1*(p_nSamples - max_index);
		else
			return (max_index - p_nSamples);
	}
	
	void xcor2_impl::set_sampRate(float sampRate)
	{	p_sampRate = sampRate;	}
	void xcor2_impl::set_nSamples(int nSamples)
	{	p_nSamples = nSamples;}
  } /* namespace eecs */
} /* namespace gr */

