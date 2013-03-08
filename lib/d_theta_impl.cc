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
//#include <gr_delay.h>

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
		      gr_make_io_signature(4,4, sizeof (gr_complex))),
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
        gr_complex *Sat1 = (gr_complex *) input_items[0];
        gr_complex *Sat2 = (gr_complex *) input_items[1];
        gr_complex *Sat3 = (gr_complex *) input_items[2];
        gr_complex *Sat4 = (gr_complex *) input_items[3];
        gr_complex *out1 = (gr_complex *) output_items[0];
        gr_complex *out2 = (gr_complex *) output_items[1];
        gr_complex *out3 = (gr_complex *) output_items[2];
        gr_complex *out4 = (gr_complex *) output_items[3];
//Constants
	//	float (*dx);				
	//		dx = (float*)malloc(4*sizeof(float));
	float dx[3];
			dx[0] = -1*(lambda/4 +lambda/2);
			dx[1] = -1*(lambda/4);
			dx[2] =  (lambda/4);
			dx[3] =  (lambda/4 +lambda/2);
//floating variables
		float (*theta);
			theta = (float*)malloc(4*sizeof(float));
		
		//int (*delays);
		//	delays = (int*)malloc(4*sizeof(int));
		
		findTheta(dx,theta);
       // theta[0] = 2*M_PI/lambda*(sqrt(p_rSat*p_rSat+dx[0]*dx[0] - 2*p_rSat*dx[0]*sin(p_thetaSat)) - p_rSat);
        //theta[1] = 2*M_PI/lambda*(sqrt(p_rSat*p_rSat+dx[1]*dx[1] - 2*p_rSat*dx[1]*sin(p_thetaSat)) - p_rSat);
        //theta[2] = 2*M_PI/lambda*(sqrt(p_rSat*p_rSat+dx[2]*dx[2] - 2*p_rSat*dx[2]*sin(p_thetaSat)) - p_rSat);
        //theta[3] = 2*M_PI/lambda*(sqrt(p_rSat*p_rSat+dx[3]*dx[3] - 2*p_rSat*dx[3]*sin(p_thetaSat)) - p_rSat);
        
        for(int i = 0; i <noutput_items; i++){
			//getDelay(theta, delays);
			out1[i] = Sat1[i]*gr_complex(cos(theta[0]), sin(theta[0]));
			out2[i] = Sat2[i]*gr_complex(cos(theta[1]), sin(theta[1]));
			out3[i] = Sat3[i]*gr_complex(cos(theta[2]), sin(theta[2]));
			out4[i] = Sat4[i]*gr_complex(cos(theta[3]), sin(theta[3]));
		}

        // Tell runtime system how many output items we produced.
        //delete theta;
//        delete delays;
        return noutput_items;
    }
	
	void 
	d_theta_impl::findTheta(float* dx, float* dt){
		float k = 2*M_PI/lambda;
		for(int i = 0; i<4 ; i++){
			dt[i] = k*(sqrt(p_rSat*p_rSat+dx[i]*dx[i] - 2*p_rSat*dx[i]*sin(p_thetaSat)) - p_rSat);
		}
	}
	
	void
	d_theta_impl::getDelay(float* theta, int* dt){
		if (theta[0] > theta[3]){
			for (int i = 0; i<4; i++){
				dt[i] = floor(p_sampRate*(theta[i]-theta[3])/(2*M_PI*p_freq)+.5);}}
		else{
			for (int i = 0; i<4; i++){
				dt[i] = floor(p_sampRate*(theta[i]-theta[0])/(2*M_PI*p_freq)+.5);}}
	}
	
	
	
	void d_theta_impl::set_freq(float freq)
	{	p_freq = freq;	}
	void d_theta_impl::set_rSat(float rSat)
	{	p_rSat = rSat;	}
	void d_theta_impl::set_thetaSat(float thetaSat)
	{	p_thetaSat = thetaSat;	}
	void d_theta_impl::set_sampRate(float sampRate)
	{	p_sampRate = sampRate;	}
	
  } /* namespace eecs */
} /* namespace gr */

