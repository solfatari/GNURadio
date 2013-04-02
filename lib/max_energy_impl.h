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

#ifndef INCLUDED_EECS_MAX_ENERGY_IMPL_H
#define INCLUDED_EECS_MAX_ENERGY_IMPL_H

#include <eecs/max_energy.h>

namespace gr {
  namespace eecs {

    class max_energy_impl : public max_energy
    {
    private:
		int p_window;
		
		int dmax(const gr_complex* s1, const gr_complex* s2,
				 const gr_complex* s3, const gr_complex* s4);
    public:
      max_energy_impl(int window);
      ~max_energy_impl();
		
	  int window() const{return p_window;}	  
	  void set_window(int window);

      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_MAX_ENERGY_IMPL_H */

