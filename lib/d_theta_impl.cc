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
#include "d_theta_impl.h"
#include <cmath>


namespace gr {
  namespace eecs {

    d_theta::sptr
    d_theta::make(float freq, 
				  float rSat,
				  float thetaSat,
				  float sampRate)
    {
      return gnuradio::get_initial_sptr (new d_theta_impl(freq, 
														  rSat,
														  thetaSat,
														  sampRate));
    }

    /*
     * The private constructor
     */
    d_theta_impl::d_theta_impl(float freq, 
							   float rSat,
							   float thetaSat,
							   float sampRate)
      : gr_sync_block("d_theta",
		      gr_make_io_signature(4,4, sizeof (gr_complex)),
		      gr_make_io_signature(1,1, sizeof (gr_complex))),
			  p_freq(freq), p_rSat(rSat), 
			  p_thetaSat(thetaSat), p_sampRate(sampRate)
		{
			lambda = 300000000/p_freq;
		}

    /*
     * Our virtual destructor.
     */
    d_theta_impl::~d_theta_impl()
    {
    }

    int
    d_theta_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *Sat1 = (const gr_complex *) input_items[0];
        const gr_complex *Sat2 = (const gr_complex *) input_items[1];
        const gr_complex *Sat3 = (const gr_complex *) input_items[2];
        const gr_complex *Sat4 = (const gr_complex *) input_items[3];
        gr_complex (*out1);// = (gr_complex *) output_items[0];
			out1 = (gr_complex*)malloc(sizeof(gr_complex));
        gr_complex (*out2);// = (gr_complex *) output_items[1];
			out2 = (gr_complex*)malloc(sizeof(gr_complex));
        gr_complex (*out3);// = (gr_complex *) output_items[2];
			out3 = (gr_complex*)malloc(sizeof(gr_complex));
        gr_complex (*out4);// = (gr_complex *) output_items[3];
			out4 = (gr_complex*)malloc(sizeof(gr_complex));
        
        gr_complex *fout = (gr_complex *) output_items[0];
//Constants
		float (*dx);				
			dx = (float*)malloc(4*sizeof(float));
			dx[0] = -1*(lambda/4 +lambda/2);
			dx[1] = -1*(lambda/4);
			dx[2] =  (lambda/4);
			dx[3] =  (lambda/4 +lambda/2);
//floating variables

		float (*theta);
			theta = (float*)malloc(4*sizeof(float));
		findTheta(dx,theta);
 
        
        for(int i = 0; i <noutput_items; i++){
			out1[0] = Sat1[i]*gr_complex(cos(theta[0]), sin(theta[0]));
			out2[0] = Sat2[i]*gr_complex(cos(theta[1]), sin(theta[1]));
			out3[0] = Sat3[i]*gr_complex(cos(theta[2]), sin(theta[2]));
			out4[0] = Sat4[i]*gr_complex(cos(theta[3]), sin(theta[3]));
			
			fout[i] = out1[0] + out2[0] + out3[0] + out4[0];
		}

        // Tell runtime system how many output items we produced.
        //delete theta; do i need to delete?
		 
        return noutput_items;
    }
	
	void 
	d_theta_impl::findTheta(float* dx, float* dt){
		float k = 2*M_PI/lambda;
		for(int i = 0; i<4 ; i++){
			dt[i] = -1*k*(sqrt(p_rSat*p_rSat+dx[i]*dx[i] - 2*p_rSat*dx[i]*sin(p_thetaSat)) - p_rSat);
		}
	}
	
	
	void d_theta_impl::set_freq(float freq)
	{	p_freq = freq;	}
	void d_theta_impl::set_rSat(float rSat)
	{	p_rSat = rSat;	}
	void d_theta_impl::set_thetaSat(float thetaSat)
	{	p_thetaSat = thetaSat;	}
	void d_theta_impl::set_sampRate(float sampRate)
	{	p_sampRate = sampRate;	}
	
  }
   /* namespace eecs */
} /* namespace gr */

