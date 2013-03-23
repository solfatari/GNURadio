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

#ifndef INCLUDED_EECS_XCORR_IMPL_H
#define INCLUDED_EECS_XCORR_IMPL_H

#include <eecs/xcorr.h>

namespace gr {
  namespace eecs {

    class xcorr_impl : public xcorr
    {
    private:
      float p_freq;
      float p_sampRate;
      int p_nSamples;

	  void 	x_corr(const gr_complex* r1, const gr_complex* r2, gr_complex* xout);
	  float findTheta(gr_complex* sig);
	
    public:
      xcorr_impl( 	float freq,
					float sampRate,
					int nSamples);
      ~xcorr_impl();

	  float freq() const{ return p_freq;}
	  float sampRate() const{ return p_sampRate;}
	  int nSamples() const{return p_nSamples;}
	  
	  void set_freq(float freq);
	  void set_sampRate(float sampRate);
	  void set_nSamples(int nSamples);

      void forecast (int noutput_items, gr_vector_int &ninput_items_required);

      // Where all the action really happens
      int general_work(int noutput_items,
		       gr_vector_int &ninput_items,
		       gr_vector_const_void_star &input_items,
		       gr_vector_void_star &output_items);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_XCORR_IMPL_H */

