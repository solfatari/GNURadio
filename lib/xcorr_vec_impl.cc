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
#include "xcorr_vec_impl.h"

namespace gr {
  namespace eecs {

    xcorr_vec::sptr
    xcorr_vec::make()
    {
      return gnuradio::get_initial_sptr (new xcorr_vec_impl());
    }

    /*
     * The private constructor
     */
    xcorr_vec_impl::xcorr_vec_impl()
      : gr_sync_block("xcorr_vec",
		      gr_make_io_signature(<+MIN_IN+>, <+MAX_IN+>, sizeof (<+float+>)),
		      gr_make_io_signature(<+MIN_IN+>, <+MAX_IN+>, sizeof (<+float+>)))
    {}

    /*
     * Our virtual destructor.
     */
    xcorr_vec_impl::~xcorr_vec_impl()
    {
    }

    int
    xcorr_vec_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const float *in = (const float *) input_items[0];
        float *out = (float *) output_items[0];

        // Do <+signal processing+>

        // Tell runtime system how many output items we produced.
        return noutput_items;
    }

  } /* namespace eecs */
} /* namespace gr */

