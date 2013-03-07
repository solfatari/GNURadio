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
#include <volk/volk.h>
#include <gr_delay.h>

namespace gr {
  namespace eecs {

    d_theta::sptr
    d_theta::make(double freq, 
				  double rSat,
				  double thetaSat,
				  double sampRate)
    {
      return gnuradio::get_initial_sptr (new d_theta_impl(freq, 
														  rSat,
														  thetaSat,
														  sampRate));
    }

    /*
     * The private constructor
     */
    d_theta_impl::d_theta_impl(double freq, 
							   double rSat,
							   double thetaSat,
							   double sampRate)
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
		double (*dx);				
			dx = (double*)malloc(4*sizeof(double));
			dx[0] = -1*(lambda/4 +lambda/2);
			dx[1] = -1*(lambda/4);
			dx[2] =  (lambda/4);
			dx[3] =  (lambda/4 +lambda/2);
//floating variables
		double (*theta);
			theta = (double*)malloc(4*sizeof(double));
		int (*delays);
			delays = (int*)malloc(4*sizeof(int));
		//Gonn start doing stupid shit
		 int d_vlen = 1;
		 int noi = d_vlen*noutput_items;

			
					 		
    //    for(int i = 0; i <noutput_items; i++){}
			findTheta(dx,theta);
			//getDelay(theta, delays);
//preload outputbuffer
memcpy(out1, Sat1, noi*sizeof(gr_complex));
memcpy(out2, Sat2, noi*sizeof(gr_complex));
memcpy(out3, Sat3, noi*sizeof(gr_complex));
memcpy(out4, Sat4, noi*sizeof(gr_complex));

  if(is_unaligned()) {
    for(size_t i = 1;i < input_items.size(); i++)
      volk_32fc_x2_multiply_32fc_u(out1, Sat1, Sat1, noi);
      volk_32fc_x2_multiply_32fc_u(out2, Sat2, Sat2, noi);
      volk_32fc_x2_multiply_32fc_u(out3, Sat3, Sat3, noi);
      volk_32fc_x2_multiply_32fc_u(out4, Sat4, Sat4, noi);
  }
  else {
    for(size_t i = 1;i < input_items.size(); i++)
      volk_32fc_x2_multiply_32fc_a(out1, Sat1, Sat1, noi);
      volk_32fc_x2_multiply_32fc_a(out2, Sat2, Sat2, noi);
      volk_32fc_x2_multiply_32fc_a(out3, Sat3, Sat3, noi);
      volk_32fc_x2_multiply_32fc_a(out4, Sat4, Sat4, noi);
  }
      
			
//			out1[i] = theta[0];
//			out2[i] = theta[1];
//			out3[i] = theta[2];
//			out4[i] = theta[3];
	

        // Tell runtime system how many output items we produced.
        delete theta;
        delete delays;
        return noutput_items;
    }
	
	void 
	d_theta_impl::findTheta(double* dx, double* dt){
		double k = 2*M_PI/lambda;
		for(int i = 0; i<4 ; i++){
			dt[i] = k*(sqrt(p_rSat*p_rSat+dx[i]*dx[i] - 2*p_rSat*dx[i]*sin(p_thetaSat)) - p_rSat);
		}
	}
	
	void
	d_theta_impl::getDelay(double* theta, int* dt){
		if (theta[0] > theta[3]){
			for (int i = 0; i<4; i++){
				dt[i] = floor(p_sampRate*(theta[i]-theta[3])/(2*M_PI*p_freq)+.5);}}
		else{
			for (int i = 0; i<4; i++){
				dt[i] = floor(p_sampRate*(theta[i]-theta[0])/(2*M_PI*p_freq)+.5);}}
	}
	
	
	
	void d_theta_impl::set_freq(double freq)
	{	p_freq = freq;	}
	void d_theta_impl::set_rSat(double rSat)
	{	p_rSat = rSat;	}
	void d_theta_impl::set_thetaSat(double thetaSat)
	{	p_thetaSat = thetaSat;	}
	void d_theta_impl::set_sampRate(double sampRate)
	{	p_sampRate = sampRate;	}
	
  }
   /* namespace eecs */
} /* namespace gr */

