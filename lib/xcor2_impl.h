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

#ifndef INCLUDED_EECS_XCOR2_IMPL_H
#define INCLUDED_EECS_XCOR2_IMPL_H

#include <eecs/xcor2.h>

namespace gr {
  namespace eecs {

    class xcor2_impl : public xcor2
    {
    private:
		float p_sampRate;
		int p_nSamples;
		
		void 	xcorr(const gr_complex* r1, const gr_complex* r2, float xout[]);
		float findTheta(float sig[]);
    public:
      xcor2_impl(float sampRate,
				  int nSamples);
      ~xcor2_impl();

      float sampRate() const{ return p_sampRate;}
	  int nSamples() const{return p_nSamples;}
	  
	  void set_sampRate(float sampRate);
	  void set_nSamples(int nSamples);
	  
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_XCOR2_IMPL_H */

