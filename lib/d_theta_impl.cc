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
				  float thetaSat)
    {
      return gnuradio::get_initial_sptr (new d_theta_impl(freq, 
														  rSat,
														  thetaSat));
    }

    /*
     * The private constructor
     */
    d_theta_impl::d_theta_impl(float freq, 
							   float rSat,
							   float thetaSat)
      : gr_sync_block("d_theta",
		      gr_make_io_signature(4,4, sizeof (float)),
		      gr_make_io_signature(1,1, sizeof (float)))
		{
		p_freq = freq;
		p_rSat = rSat;
		p_thetaSat = thetaSat;
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
        const float *Sat1 = (const float *) input_items[0];
        const float *Sat2 = (const float *) input_items[1];
        const float *Sat3 = (const float *) input_items[2];
        const float *Sat4 = (const float *) input_items[3];
        float *out = (float *) output_items[0];
//Constants
		float lambda = 300000000/p_freq;
		float dx1 = -(lambda/4 +lambda/2);
		float dx2 = -(lambda/2);
		float dx3 =  (lambda/2);
		float dx4 =  (lambda/4 +lambda/2);
//floating variables
		float theta[3], delays[3];
		
		
        for(int i = 0; i <noutput_items; i++){
			theta[0] = findTheta(dx1, lambda);
			theta[1] = findTheta(dx2, lambda);
			theta[2] = findTheta(dx3, lambda);
			theta[3] = findTheta(dx4, lambda);
			getDelay(theta, delays);
			
			out[i] = delays[0];
		}

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }
	
	float 
	d_theta_impl::findTheta(float dx, float lambda){
		float k = 2*3.1415926/lambda;
	
	return k*(sqrt(p_rSat*p_rSat+dx*dx - 2*p_rSat*dx*sin(p_thetaSat)) - p_rSat);
	}
	
	void
	d_theta_impl::getDelay(float theta[3], float dt[3]){
		if (theta[0] > theta[3]){
			for (int i = 0; i<3; i++){
				dt[i] = (theta[0]-theta[4])/(2*3.1415926*p_freq);
			}
		}
		else{
			for (int i = 0; i<3; i++){
				dt[i] = (theta[0]+theta[4])/(2*3.1415926*p_freq);
			}
		}
	
	}
	
	
	
  } /* namespace eecs */
} /* namespace gr */

