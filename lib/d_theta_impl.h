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

namespace gr {
  namespace eecs {

    class d_theta_impl : public d_theta
    {
    private:
      double p_freq;
      double p_rSat;
      double p_thetaSat;
      double p_sampRate;
	
	  double findTheta(double dx, double lambda);
	  void  getDelay(double theta[3], double dt[3]);
    public:
      d_theta_impl(double freq, 
				   double rSat,
				   double thetaSat,
				   double sampRate);
      ~d_theta_impl();

      // Where all the action really happens
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_D_THETA_IMPL_H */

