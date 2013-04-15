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
#include "fft_shift_impl.h"

namespace gr {
  namespace eecs {

    fft_shift::sptr
    fft_shift::make(int window, int shift)
    {
      return gnuradio::get_initial_sptr (new fft_shift_impl(window, shift));
    }

    /*
     * The private constructor
     */
    fft_shift_impl::fft_shift_impl(int window, int shift)
      : gr_sync_block("fft_shift",
		      gr_make_io_signature(1, 1, window*sizeof (gr_complex)),
		      gr_make_io_signature(1, 1, window*sizeof (gr_complex))),
		      p_window(window), p_shift(shift)
    {}

    /*
     * Our virtual destructor.
     */
    fft_shift_impl::~fft_shift_impl()
    {
    }

    int
    fft_shift_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex*) input_items[0];
        gr_complex *out = (gr_complex*) output_items[0];
        size_t block_size = output_signature()->sizeof_stream_item (0);
		gr_complex tmp[p_window];
		
		for (int i = 0; i < p_window-p_shift; i++)
			tmp[i] = in[i+p_shift]; 
		for (int i = p_window-p_shift; i < p_window; i++)
			tmp[i] = 0;
		for (int i =0; i <noutput_items; i++)
			memcpy(out, tmp, p_window*sizeof(gr_complex));

        return noutput_items;
    }
	
	void fft_shift_impl::set_window(int window)
		{p_window = window;}
	void fft_shift_impl::set_shift(int shift)
		{p_shift = shift;}
  } /* namespace eecs */
} /* namespace gr */

