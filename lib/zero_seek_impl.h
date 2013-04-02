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

#ifndef INCLUDED_EECS_ZERO_SEEK_IMPL_H
#define INCLUDED_EECS_ZERO_SEEK_IMPL_H

#include <eecs/zero_seek.h>

namespace gr {
  namespace eecs {

    class zero_seek_impl : public zero_seek
    {
    private:
      int blockLen;
      int sampRate;
      
      int findFreq(const gr_complex* s);

    public:
      zero_seek_impl(int blockLen, int sampRate);
      ~zero_seek_impl();

      int blockLen() const{return p_blockLen;}	  
	  void set_blockLen(int blockLen);
	  int sampRate() const{return p_sampRate;}	  
	  void set_sampRate(int sampRate);
	  
      int work(int noutput_items,
	       gr_vector_const_void_star &input_items,
	       gr_vector_void_star &output_items);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_ZERO_SEEK_IMPL_H */

