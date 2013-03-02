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
    d_theta::make(float test)
    {
      return gnuradio::get_initial_sptr (new d_theta_impl(test));
    }

    /*
     * The private constructor
     */
    d_theta_impl::d_theta_impl(float test)
      : gr_sync_block("d_theta",
		      gr_make_io_signature(2,2, sizeof (float)),
		      gr_make_io_signature(1,1, sizeof (float)))
    {
		t_test = test;
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
        const float *rSat = (const float *) input_items[0];
        const float *thetaSat = (const float *) input_items[1];
        float *out = (float *) output_items[0];
// temp constants
		float lambda = .3030303;
		float dx1 = -(lambda/4 +lambda/2);
		float k = 2*3.1415926/lambda;

        for(int i = 0; i <noutput_items; i++){
			out[i] = t_test + k*(sqrt(rSat[i]*rSat[i]+dx1*dx1 - 2*rSat[i]*dx1*sin(thetaSat[i])) - rSat[i]);
		}

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace eecs */
} /* namespace gr */

