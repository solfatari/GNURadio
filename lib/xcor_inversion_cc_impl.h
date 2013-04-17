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

#ifndef INCLUDED_EECS_XCOR_INVERSION_CC_IMPL_H
#define INCLUDED_EECS_XCOR_INVERSION_CC_IMPL_H

#include <eecs/xcor_inversion_cc.h>

namespace gr {
  namespace eecs {

    class xcor_inversion_cc_impl : public xcor_inversion_cc
    {
    private:
		int p_nSamples;
		
		int xcorr(const gr_complex* r1, const gr_complex* r2, bool iflag);
		int findTheta(gr_complex sig[]);
    
    public:
      xcor_inversion_cc_impl(int nSamples);
      ~xcor_inversion_cc_impl();

	  int nSamples() const{return p_nSamples;}
	  
	  void set_nSamples(int nSamples);
	  
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_xcor_inversion_cc_IMPL_H */
