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

#ifndef INCLUDED_EECS_XCORR_VEC_IMPL_H
#define INCLUDED_EECS_XCORR_VEC_IMPL_H

#include <eecs/xcorr_vec.h>

namespace gr {
  namespace eecs {

    class xcorr_vec_impl : public xcorr_vec
    {
    private:
		int p_window;
		gr_complex *saved[100];
		
		void xcorr(const gr_complex* r1, const gr_complex* r2, gr_complex xout[]);
		int findTheta(gr_complex sig[]);
   
    public:
      xcorr_vec_impl(int window);
      ~xcorr_vec_impl();

	  int window() const{return p_window;}	  
	  void set_window(int window);
	  
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_XCORR_VEC_IMPL_H */

