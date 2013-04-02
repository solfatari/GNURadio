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
#include "max_energy_impl.h"

namespace gr {
  namespace eecs {

    max_energy::sptr
    max_energy::make(int window)
    {
      return gnuradio::get_initial_sptr (new max_energy_impl(window));
    }

    /*
     * The private constructor
     */
    max_energy_impl::max_energy_impl(int window)
      : gr_sync_block("max_energy",
		      gr_make_io_signature(4, 4, sizeof (gr_complex)),
		      gr_make_io_signature(2, 2, sizeof (gr_complex))),
		      p_window(window)
    {
		set_history(p_window);
	}

    /*
     * Our virtual destructor.
     */
    max_energy_impl::~max_energy_impl()
    {
    }

    int
    max_energy_impl::work(int noutput_items,
			  gr_vector_const_void_star &input_items,
			  gr_vector_void_star &output_items)
    {
        const gr_complex *s1 = (const gr_complex *) input_items[0];
        const gr_complex *s2 = (const gr_complex *) input_items[1];
        const gr_complex *s3 = (const gr_complex *) input_items[2];
        const gr_complex *s4 = (const gr_complex *) input_items[3];
        gr_complex *max = (gr_complex *) output_items[0];
        gr_complex *du_signal = (gr_complex *) output_items[1];
		s1 += p_window; s2 +=p_window;
		s3 += p_window; s4 +=p_window;
		int m_sig = 1;
		
		m_sig = dmax(s1,s2,s3,s4);
		
		for (int i =0; i <noutput_items; i++){
			if (m_sig == 2)
				max[i] = s2[i];
			else if (m_sig ==3)
				max[i] = s3[i];
			else if (m_sig ==4)
				max[i] = s4[i];
			else
				max[i] = s1[i];
			du_signal[i] = m_sig;
		}
       return noutput_items;
    }
	
	int max_energy_impl::dmax(const gr_complex* ms1, const gr_complex* ms2,
						  const gr_complex* ms3, const gr_complex* ms4){
		float t_s1, t_s2, t_s3, t_s4;
		for(int i = 0; i < p_window; i++){
			t_s1 += abs(ms1[i])*abs(ms1[i]);
			t_s2 += abs(ms2[i])*abs(ms2[i]);
			t_s3 += abs(ms3[i])*abs(ms3[i]);
			t_s4 += abs(ms4[i])*abs(ms4[i]); 
		}
		t_s1 = t_s1/p_window;	t_s3 = t_s3/p_window;
		t_s2 = t_s2/p_window;	t_s4 = t_s4/p_window;
		if (t_s4>t_s3 && t_s4>t_s2 && t_s4>t_s1)
			return 4;
		else if (t_s3>t_s2 && t_s3>t_s1)	
			return 3;
		else if (t_s2>t_s1)
			return 2;
		else
			return 1;
	}
	  
	void max_energy_impl::set_window(int window)
	{	p_window = window;}						  
							
  } /* namespace eecs */
} /* namespace gr */

