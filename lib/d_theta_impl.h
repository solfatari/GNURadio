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

#ifndef INCLUDED_EECS_D_THETA_IMPL_H
#define INCLUDED_EECS_D_THETA_IMPL_H

#include <eecs/d_theta.h>
#include <gr_delay.h>
#include <gr_block.h>

namespace gr {
  namespace eecs {

    class d_theta_impl : public d_theta
    {
    private:
      double p_freq;
      double p_rSat;
      double p_thetaSat;
      double p_sampRate;
      double lambda;
	
	  void findTheta(double* dx, double* dt);
	  void  getDelay(double* theta, int* dt);
	  
	  
    public:
      d_theta_impl(double freq, 
				   double rSat,
				   double thetaSat,
				   double sampRate);
      ~d_theta_impl();
	  
	  double freq() const{ return p_freq;}
	  double rSat() const{ return p_rSat;}
	  double thetaSat() const{ return p_thetaSat;}
	  double sampRate() const{ return p_sampRate;}
	  
	  
	  void set_freq(double freq);
	  void set_rSat(double rSat);
	  void set_thetaSat(double thetaSat);
	  void set_sampRate(double sampRate);
	  
      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_D_THETA_IMPL_H */

