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
#include <cmath>
#include <complex>
#include "xcorr_vec_impl.h"

namespace gr {
  namespace eecs {

    xcorr_vec::sptr
    xcorr_vec::make(int window)
    {
      return gnuradio::get_initial_sptr (new xcorr_vec_impl(window));
    }

    xcorr_vec_impl::xcorr_vec_impl(int window)
      : gr_sync_block("xcorr_vec",
		      gr_make_io_signature(2, 2, window*sizeof (gr_complex)),
		      gr_make_io_signature(2, 2, window*sizeof (gr_complex))),
		      p_window(window)
    {}

    xcorr_vec_impl::~xcorr_vec_impl(){}

    int
    xcorr_vec_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        size_t block_size = input_signature()->sizeof_stream_item (0);
        const gr_complex *r1 = (const gr_complex *) input_items[0];
        const gr_complex *r2 = (const gr_complex *) input_items[1];
        gr_complex *out1 = (gr_complex *) output_items[0];
		gr_complex *out2 = (gr_complex *) output_items[1];

		gr_complex xcor[2*p_window-1];
		int offset;
        xcorr(r1, r2, xcor);
		offset =findTheta(xcor);
		
		for(int i = 0; i <noutput_items; i++){
			if (offset < 0 || offset== 0){		// Neg theta offset
				memcpy(out1, r1, noutput_items*block_size);
				for (int j = 0; j < p_window-offset; j++)
					memcpy(&out2[j], &r2[j+offset], sizeof(gr_complex));
		//		for (int j = p_window-offset; j < p_window; j++)
		//			memcpy(&out2[j], &r1[j], sizeof(gr_complex));
			for (int i = 0; i < offset;i++)		//copy what we need for the next one
				memcpy(&saved[i], &r2[p_window-offset+i], sizeof(gr_complex));
			}			
		}
	
        return noutput_items;
    }

	void xcorr_vec_impl::xcorr(const gr_complex* ir1, const gr_complex* r2, gr_complex xout[])
	{
		gr_complex r1[2*p_window-1];
		for (int i = 0; i < p_window-1; i++)
			r1[i] = conj(ir1[i]);
		for(int i = 0; i < p_window-1; i++){							
			xout[i] = 0;												
			for (int j = 0; j < i; j++)								
				xout[i] = xout[i]+ r1[i-j]*r2[p_window-j];					
		}	
		for(int i = -1; i < p_window-2; i++){							
			xout[p_window+i-1] = 0;										
			for(int j = 0; j < (p_window-i-1); j++){					
			  xout[p_window+i-1] = xout[p_window+i-1] + r1[i+j]*r2[j];  		
			}}
	}
	
	int xcorr_vec_impl::findTheta(gr_complex sig[]){
		float max_val = 0;
		int max_index = 0;
		
		for (int i = 0; i < 2*p_window-1; i++){	
			if (real(sig[i]) > max_val){
				max_val = real(sig[i]);
				max_index = i;
		}}
		if (max_index > p_window)
			return -1*(p_window-1 - max_index);
		else 					
			return -1*(p_window-1 - max_index);
	}
	
	void xcorr_vec_impl::set_window(int window)
	{	p_window = window;}
  } /* namespace eecs */
} /* namespace gr */

