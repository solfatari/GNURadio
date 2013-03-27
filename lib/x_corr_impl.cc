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
		      gr_make_io_signature(2, 2, sizeof (gr_complex)),
		      gr_make_io_signature(1, 1, sizeof (gr_complex))),
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
		gr_complex *out = (gr_complex *) output_items[0];

		Sat1 += p_nSamples; Sat2 += p_nSamples;//ensure that sample range is valid.
		
		float xcor[2*p_nSamples];
		float theta;
//////////		
		xcorr(Sat1, Sat2, xcor);
		theta =findTheta(xcor);

		for(int i = 0; i <noutput_items; i++){
			out[i] = Sat1[i]+Sat2[i]*gr_complex(cos(-1*theta), sin(-1*theta));
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
	
	float x_corr_impl::findTheta(float sig[]){
		float max_val = 0;
		int max_index = 0;
		
		for (int i = 0; i < p_nSamples-1; i++){							//for i = 1:len
			if (sig[i] > max_val){
				max_val = sig[i];
				max_index = i;
		}}
	return dp((max_index - p_nSamples)/p_sampRate*2*M_PI*p_freq);
	}
	
	float x_corr_impl::dp(float phase){
		if (phase < -2*M_PI || phase == -2*M_PI){
			return dp(phase+2*M_PI);}
		else if (phase > 2*M_PI || phase == 2*M_PI){
			return dp(phase-2*M_PI);}
		else
			return(phase);
	}

	void x_corr_impl::set_freq(float freq)
	{	p_freq = freq;	}
	void x_corr_impl::set_sampRate(float sampRate)
	{	p_sampRate = sampRate;	}
	void x_corr_impl::set_nSamples(int nSamples)
	{	p_nSamples = nSamples;}
	
  } /* namespace eecs */
} /* namespace gr */

