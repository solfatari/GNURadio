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
#include "max_vec_impl.h"

namespace gr {
  namespace eecs {

    max_vec::sptr
    max_vec::make(int window)
    {
      return gnuradio::get_initial_sptr (new max_vec_impl(window));
    }

    /*
     * The private constructor
     */
    max_vec_impl::max_vec_impl(int window)
      : gr_sync_block("max_vec",
		      gr_make_io_signature(4, 4, window * sizeof (gr_complex)),
			gr_make_io_signature(4, 4, window * sizeof (gr_complex))),
			p_window(window)
    {}

    /*
     * Our virtual destructor.
     */
    max_vec_impl::~max_vec_impl()
    {
    }

    int
    max_vec_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        size_t block_size = output_signature()->sizeof_stream_item (0);
		gr_complex *s1 = (gr_complex *) input_items[0];
		gr_complex *s2 = (gr_complex *) input_items[1];
		gr_complex *s3 = (gr_complex *) input_items[2];
		gr_complex *s4 = (gr_complex *) input_items[3];
		gr_complex *max1 = (gr_complex *) output_items[0];
		gr_complex *max2 = (gr_complex *) output_items[1];
		gr_complex *max3 = (gr_complex *) output_items[2];
		gr_complex *max4 = (gr_complex *) output_items[3];
		int order[4] = {0,1,2,3};
		dmax(s1,s2,s3,s4,order);

		for (int i =0; i <noutput_items; i++){
			gr_complex *s1 = (gr_complex *) input_items[order[0]];
			gr_complex *s2 = (gr_complex *) input_items[order[1]];
			gr_complex *s3 = (gr_complex *) input_items[order[2]];
			gr_complex *s4 = (gr_complex *) input_items[order[3]];
			memcpy(max1,s1, noutput_items * block_size);	
			memcpy(max2,s2, noutput_items * block_size);
			memcpy(max3,s3, noutput_items * block_size);
			memcpy(max4,s4, noutput_items * block_size);
		}
       return noutput_items;
    }

	void max_vec_impl::dmax(gr_complex* ms1, gr_complex* ms2,
							gr_complex* ms3, gr_complex* ms4, int out[]){
		bool done = 0;
		float t_s1, t_s2, t_s3, t_s4, tmp;
		for(int i = 0; i < p_window; i++){
			t_s1 += abs(ms1[i])*abs(ms1[i]);
			t_s2 += abs(ms2[i])*abs(ms2[i]);
			t_s3 += abs(ms3[i])*abs(ms3[i]);
			t_s4 += abs(ms4[i])*abs(ms4[i]); 
		}
		float t[4] = {t_s1, t_s2, t_s3, t_s4};
		while(!done){
			if (t[0] <t[1]){
				tmp = t[0];	t[0] = t[1]; t[1] = tmp;}
			else if (t[1] < t[2]){
				tmp = t[1];	t[1] = t[2]; t[2] = tmp;}
			else if (t[2] <t[3]){
				tmp = t[2];	t[2] = t[3]; t[3] = tmp;}
			else
				done = 1;
		}

		for (int i = 0; i < 3; i++){
			if (t[i] == t_s1)
				out[i] = 0;
			if (t[i] == t_s2)
				out[i] = 1;
			if (t[i] == t_s3)
				out[i] = 2;
			if (t[i] == t_s4)
				out[i] = 3;
		}
	}

void max_vec_impl::set_window(int window)
{	p_window = window;}	 

  } /* namespace eecs */
} /* namespace gr */

