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
#include "xcorr_impl.h"
#include <cmath>
#include <complex>

namespace gr {
  namespace eecs {

    xcorr::sptr
    xcorr::make(float freq, 
				float sampRate,
				int nSamples)
    {
      return gnuradio::get_initial_sptr (new xcorr_impl(freq, 
													    sampRate,
													    nSamples));
    }

    /*
     * The private constructor
     */
    xcorr_impl::xcorr_impl( float freq, 
							float sampRate,
							int nSamples)
      : gr_block("xcorr",
		      gr_make_io_signature(4, 4, sizeof (gr_complex)),
		      gr_make_io_signature(4, 4, sizeof (gr_complex))),
		      p_freq(freq), p_sampRate(sampRate), p_nSamples(nSamples)
    {
		set_history(512);
	}

    /*
     * Our virtual destructor.
     */
    xcorr_impl::~xcorr_impl()
    {
    }

    void
    xcorr_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
    {
      ninput_items_required[0] = 512;
    }

    int
    xcorr_impl::general_work (int noutput_items,
                       gr_vector_int &ninput_items,
                       gr_vector_const_void_star &input_items,
                       gr_vector_void_star &output_items)
    {
        const gr_complex *Sat1 = (const gr_complex *) input_items[0];
        const gr_complex *Sat2 = (const gr_complex *) input_items[1];
        const gr_complex *Sat3 = (const gr_complex *) input_items[2];
        const gr_complex *Sat4 = (const gr_complex *) input_items[3];
		gr_complex *out1 = (gr_complex *) output_items[0];
		gr_complex *out2 = (gr_complex *) output_items[1];
		gr_complex *out3 = (gr_complex *) output_items[2];
		gr_complex *out4 = (gr_complex *) output_items[3];
		
		gr_complex *(*xcor);
		xcor = (gr_complex**)malloc(3*sizeof(gr_complex *));
		for (int i =0; i<3; i++){
			xcor[i] = (gr_complex*)malloc((2*512-1)*sizeof(gr_complex));
		}

		float (*theta);
			theta = (float*)malloc(4*sizeof(float));
			
		x_corr(Sat1, Sat2, xcor[0]);
		
		for(int i = 0; i <noutput_items; i++){
			out1[i] = Sat1[i]*gr_complex(cos(theta[0]), sin(theta[0]));
			out2[i] = Sat2[i]*gr_complex(cos(theta[1]), sin(theta[1]));
			out3[i] = Sat3[i]*gr_complex(cos(theta[2]), sin(theta[2]));
			out4[i] = Sat4[i]*gr_complex(cos(theta[3]), sin(theta[3]));
			
		}     
        
        
        
        consume_each (noutput_items);
        // Tell runtime system how many output items we produced.
        return noutput_items;
    }
    
	void xcorr_impl::x_corr(const gr_complex* r1, const gr_complex* r2, gr_complex* xout)
	{
		for(int i = 0; i < p_nSamples-1; i++){							// for i = 1:len
			xout[i] = 0;												//   xcor12(i) = 0;
			for (int j = 0; j <= i; j++){								//   for j=1:i
				xout[i] += r1[i-j]*r2[p_nSamples-j];					//     xcor12(i) = xcor12(i) + r1C(i-j+1)*r2(len-j+1);
		}}	
		for(int i = 0; i < p_nSamples; i++){							//for i = 0:len-1
			xout[p_nSamples+i] = 0;										//   xcor12(len+i) = 0;
			for(int j = 0; j < p_nSamples-1-i; j ++){					//   for j = 1:len-i
			  xout[p_nSamples+i] += r1[p_nSamples-1 +i]*r2[j];  		//      xcor12(len+i) = xcor12(len+i) + r1C(i+j)*r2(j);
					}}
	}
	
	float xcorr_impl::findTheta(gr_complex* sig){
		float max_val = 0;
		int max_index = 0;
		
		for (int i = 0; i < p_nSamples-1; i++){							//for i = 1:len
			if (real(sig[i]) > max_val){
				max_val = real(sig[i]);
				max_index = i;
		}}
	return (max_index - p_nSamples)/(p_sampRate*2*M_PI*p_freq);
	}

		
	void xcorr_impl::set_freq(float freq)
	{	p_freq = freq;	}
	void xcorr_impl::set_sampRate(float sampRate)
	{	p_sampRate = sampRate;	}
	void xcorr_impl::set_nSamples(int nSamples)
	{	p_nSamples = nSamples;}
	
  } /* namespace eecs */
} /* namespace gr */

