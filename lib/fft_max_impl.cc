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
#include "fft_max_impl.h"

namespace gr {
  namespace eecs {

    fft_max::sptr
    fft_max::make(int window)
    {
      return gnuradio::get_initial_sptr (new fft_max_impl(window));
    }

    /*
     * The private constructor
     */
    fft_max_impl::fft_max_impl(int window)
      : gr_sync_block("fft_max",
		      gr_make_io_signature(2, 2, window*sizeof(gr_complex)),
		      gr_make_io_signature(2, 2, sizeof(float))),
		      p_window(window)
    {}

    /*
     * Our virtual destructor.
     */
    fft_max_impl::~fft_max_impl()
    {
    }

    int
    fft_max_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in1 = (const gr_complex*) input_items[0];
        const gr_complex *in2 = (const gr_complex *) input_items[1];
        float *out1 = (float *) output_items[0];
        float *out2 = (float *) output_items[1];
		
		float mag1[p_window], mag2[p_window];
		
		for (int i = 0; i < p_window; i++){
			mag1[i] = floor(real(in1[i]));
		//	mag2[i] = floor(abs(in2[i])*abs(in2[i]));
		}
        int o1[2] = {0,0};
        max(mag1, o1);
				
		for (int i = 0; i < noutput_items; i++){
			out1[i] = o1[0];
			out2[i] = o1[1];
		}
        return noutput_items;
    }

	void fft_max_impl::max(float in[], int out[]){
		float max_val = 0;
		int zero_cross = 0;
		
		for (int i = 0; i < p_window; i++){	
			if (in[i] > max_val){
				max_val = in[i];
				out[0] = i;
		}}
		int j = out[0]+1;
		while (zero_cross != 0){
			if (in[j] == 0 || in[j] < 0)
				zero_cross = j;
			j++;
			if (j == p_window)
				j = 0;
		}
		max_val = 0;
		if (zero_cross < out[0]){
		for (int i = zero_cross; i < out[0]; i++){
			if (in[i] > max_val){
				max_val = in[i];
				out[1] = i;
			}}}
		else{
			for (int i = zero_cross; i < p_window; i++){
			if (in[i] > max_val){
				max_val = in[i];
				out[1] = i;
			}}}
		}
	//}
	
	void fft_max_impl::set_window(int window)
		{p_window = window;}	

  } /* namespace eecs */
} /* namespace gr */

