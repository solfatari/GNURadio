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
#include <cmath>
#include <complex>
#include "xcorr_vec_impl.h"

namespace gr {
  namespace eecs {

    xcorr_vec::sptr
    xcorr_vec::make(int block_len)
    {
      return gnuradio::get_initial_sptr (new xcorr_vec_impl(block_len));
    }

    /*
     * The private constructor
     */
    xcorr_vec_impl::xcorr_vec_impl(int block_len)
      : gr_sync_block("xcorr_vec",
		      gr_make_io_signature(2, 2, block_len * sizeof (gr_complex)),
		      gr_make_io_signature(2, 2, block_len * sizeof (gr_complex))),
		      p_block_len(block_len)
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
        const gr_complex *r1 = (const gr_complex *) input_items[0];
        const gr_complex *r2 = (const gr_complex *) input_items[1];
        gr_complex *out1 = (gr_complex *) output_items[0];
		gr_complex *out2 = (gr_complex *) output_items[1];
		
		unsigned int input_data_size = input_signature()->sizeof_stream_item (0);
		unsigned int output_data_size = output_signature()->sizeof_stream_item (0);

		int count = 0;
		
        while (count++ < noutput_items){
			
		
		}
        return noutput_items;
    }

	void xcorr_vec_impl::set_block_len(int block_len)
	{	p_block_len = block_len;}
	
  } /* namespace eecs */
} /* namespace gr */

