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


#ifndef INCLUDED_EECS_ZERO_SEEK_H
#define INCLUDED_EECS_ZERO_SEEK_H

#include <eecs/api.h>
#include <gr_sync_block.h>

namespace gr {
  namespace eecs {

    /*!
     * \brief <+description of block+>
     * \ingroup eecs
     *
     */
    class EECS_API zero_seek : virtual public gr_sync_block
    {
    public:
       typedef boost::shared_ptr<zero_seek> sptr;

       /*!
        * \brief Return a shared_ptr to a new instance of eecs::zero_seek.
        *
        * To avoid accidental use of raw pointers, eecs::zero_seek's
        * constructor is in a private implementation
        * class. eecs::zero_seek::make is the public interface for
        * creating new instances.
        */
       static sptr make(int block_len);
       
       virtual int	  block_len() const = 0;
	   virtual void set_block_len(int block_len) = 0;
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_ZERO_SEEK_H */

