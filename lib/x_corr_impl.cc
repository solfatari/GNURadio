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
#include "x_corr_impl.h"
#include <cmath>
#include <complex>

namespace gr {
  namespace eecs {

    x_corr::sptr
    x_corr::make(float freq, 
				float sampRate,
				int nSamples)
    {
      return gnuradio::get_initial_sptr (new x_corr_impl(freq, 
													    sampRate,
													    nSamples));
    }

    x_corr_impl::x_corr_impl(float freq, 
							float sampRate,
							int nSamples)
      : gr_sync_block("x_corr",
		      gr_make_io_signature(4, 4, sizeof (gr_complex)),
		      gr_make_io_signature(4, 4, sizeof (gr_complex))),
		      p_freq(freq), p_sampRate(sampRate), p_nSamples(nSamples)
		{
		set_history(p_nSamples);
		}

    x_corr_impl::~x_corr_impl(){}

    int
    x_corr_impl::work(int noutput_items,
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
		Sat1 += p_nSamples; Sat2 += p_nSamples; 
		Sat3 += p_nSamples; Sat4 += p_nSamples;// ensure that sample range is valid.
		

		float xcor[2][p_nSamples];		

		float (*theta) = new float[3];
//////////		
		xcorr(Sat1, Sat2, xcor[0]);
		//xcorr(Sat2, Sat3, xcor[1]);
		//xcorr(Sat3, Sat4, xcor[2]);
		theta[0] =0;
		theta[1] =findTheta(xcor[0]);
		theta[2] =0;
		theta[3] =0;
		for(int i = 0; i <noutput_items; i++){
			out1[i] = theta[0];//Sat1[i]*gr_complex(cos(theta[0]), sin(theta[0]));
			out2[i] = theta[1];//Sat2[i]*gr_complex(cos(theta[1]), sin(theta[1]));
			out3[i] = theta[0];//Sat3[i]*gr_complex(cos(theta[2]), sin(theta[2]));
			out4[i] = theta[1];//Sat4[i]*gr_complex(cos(theta[3]), sin(theta[3]));	
		}     
        
        return noutput_items;
    }
    
	void x_corr_impl::xcorr(const gr_complex* grc_r1, const gr_complex* grc_r2, float xout[])
	{
		float r1[p_nSamples] ,r2[p_nSamples];
		for (int i =0; i< p_nSamples; i++){
			r1[i] = real(grc_r1[i]);
			r2[i] = real(grc_r2[i]);
		}
		for(int i = 0; i < p_nSamples-1; i++){							// for i = 1:len
			xout[i] = 0;												//   xcor12(i) = 0;
			for (int j = 0; j <= i; j++){								//   for j=1:i
				xout[i] = xout[i]+ r1[i-j]*r2[p_nSamples-j];					//     xcor12(i) = xcor12(i) + r1C(i-j+1)*r2(len-j+1);
		}}	
		for(int i = 0; i < p_nSamples-2; i++){							//for i = 0:len-1
			xout[p_nSamples+i] = 0;										//   xcor12(len+i) = 0;
			for(int j = 0; j < (p_nSamples-1-i); j++){					//   for j = 1:len-i
			  xout[p_nSamples+i] += r1[p_nSamples-1 +i]*r2[j];  		//      xcor12(len+i) = xcor12(len+i) + r1C(i+j)*r2(j);
					}}
	}
	
	float x_corr_impl::findTheta(float sig[]){
		float max_val = 0;
		int max_index = 0;
		
		for (int i = 0; i < p_nSamples-1; i++){							//for i = 1:len
			if (sig[i] > max_val){
				max_val = sig[i];
				max_index = i;
		}}
	return (max_index - p_nSamples)/p_sampRate*2*p_freq*180;
	}

	void x_corr_impl::set_freq(float freq)
	{	p_freq = freq;	}
	void x_corr_impl::set_sampRate(float sampRate)
	{	p_sampRate = sampRate;	}
	void x_corr_impl::set_nSamples(int nSamples)
	{	p_nSamples = nSamples;}
	
  } /* namespace eecs */
} /* namespace gr */

