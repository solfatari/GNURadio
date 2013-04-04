/* -*- c++ -*- */
/* 
 * Copyright 2013 Costa and Acosta Space Systems.
 * 
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
		
		void dmax(gr_complex* s1, gr_complex* s2,
				  gr_complex* s3, gr_complex* s4, int out[]);
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

