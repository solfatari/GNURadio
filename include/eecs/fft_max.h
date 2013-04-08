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


#ifndef INCLUDED_EECS_FFT_MAX_H
#define INCLUDED_EECS_FFT_MAX_H

#include <eecs/api.h>
#include <gr_sync_block.h>

namespace gr {
  namespace eecs {

    /*!
     * \brief <+description of block+>
     * \ingroup eecs
     *
     */
    class EECS_API fft_max : virtual public gr_sync_block
    {
    public:
       typedef boost::shared_ptr<fft_max> sptr;

       /*!
        * \brief Return a shared_ptr to a new instance of eecs::fft_max.
        *
        * To avoid accidental use of raw pointers, eecs::fft_max's
        * constructor is in a private implementation
        * class. eecs::fft_max::make is the public interface for
        * creating new instances.
        */
       static sptr make(int window);
       
		virtual int	  window() const = 0;
		virtual void set_window(int window) = 0;
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_FFT_MAX_H */

