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


#ifndef INCLUDED_EECS_PHASE_SHIFTER_H
#define INCLUDED_EECS_PHASE_SHIFTER_H

#include <eecs/api.h>
#include <gr_sync_block.h>

namespace gr {
  namespace eecs {

    /*!
     * \brief <+description of block+>
     * \ingroup eecs
     *
     */
    class EECS_API phase_shifter : virtual public gr_sync_block
    {
    public:
       typedef boost::shared_ptr<phase_shifter> sptr;

       /*!
        * \brief Return a shared_ptr to a new instance of eecs::phase_shifter.
        *
        * To avoid accidental use of raw pointers, eecs::phase_shifter's
        * constructor is in a private implementation
        * class. eecs::phase_shifter::make is the public interface for
        * creating new instances.
        */
       static sptr make(float Rs, float dx, float theta, float wl, float ph0);
    };

  } // namespace eecs
} // namespace gr

#endif /* INCLUDED_EECS_PHASE_SHIFTER_H */

