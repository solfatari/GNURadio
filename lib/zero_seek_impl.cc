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
#include <complex>
#include <math>
#include "zero_seek_impl.h"

namespace gr {
  namespace eecs {

    zero_seek::sptr
    zero_seek::make( int blockLen, int sampRate)
    {
      return gnuradio::get_initial_sptr (new zero_seek_impl(blockLen,
															sampRate));
    }

    zero_seek_impl::zero_seek_impl(int blockLen, int sampRate)
      : gr_sync_block("zero_seek",
		      gr_make_io_signature(1, 1, sizeof (gr_complex)),
		      gr_make_io_signature(1, 1, sizeof (float))),
		      p_blockLen(blockLen), p_sampRate(sampRate)
    {
		set_history(p_blockLen);
	}

    zero_seek_impl::~zero_seek_impl(){}

    int
    zero_seek_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *in = (const gr_complex *) input_items[0];
        float *out = (float *) output_items[0];
		in += p_blockLen;
		int count = 0;
		
		while (count++ < noutput_items){
			out[i] = findFreq(s1);
		}
        
        return noutput_items;
    }

	int zero_seek_impl::findFreq(const gr_complex s){
		int marker = 0; int index = 0;

		for (int i = 0; i<p_blockLen; i++){
			if(marker ==0){
				if (abs(s[i]) < .001){
					marker = 1;
					index = i;	
					i += 10;
			}}
			if (marker == 1){
				if (abs(s[i]) < .001){
					return (i-marker);
			}}
		}
		return -1;
	} // end findFreq

	void zero_seek_impl::set_blockLen(int blockLen)
	{	p_blockLen = blockLen;}
	void zero_seek_impl::set_sampRate(int sampRate)
	{	p_sampRate = sampRate;}
	
  
  } /* namespace eecs */
} /* namespace gr */

