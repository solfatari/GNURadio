#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include "rev_phase_shifter_impl.h"
#include <gr_io_signature.h>
#include <cmath>

namespace gr {
  	namespace eecs {

		rev_phase_shifter::sptr
		rev_phase_shifter::make(float Rs, float dx, float theta, float wl, float ph0)
		{return gnuradio::get_initial_sptr (new rev_phase_shifter_impl(Rs, dx, theta, wl, ph0));}

		rev_phase_shifter_impl::rev_phase_shifter_impl(float Rs, float dx, float theta, float wl, float ph0)
			: gr_sync_block("rev_phase_shifter",
			gr_make_io_signature(1,4,sizeof(gr_complex)),
			gr_make_io_signature(1,4,sizeof(gr_complex))),
			d_Rs(Rs), d_dx(dx), d_theta(theta), d_wl(wl), d_ph0(ph0)
		{}

		rev_phase_shifter_impl::~rev_phase_shifter_impl()
		{}

		int rev_phase_shifter_impl::work(int noutput_items,
			gr_vector_const_void_star &input_items,
			gr_vector_void_star &output_items)
		{
			gr_complex *in0 = (gr_complex *) input_items[0];
			gr_complex *in1 = (gr_complex *) input_items[1];
			gr_complex *in2 = (gr_complex *) input_items[2];
			gr_complex *in3 = (gr_complex *) input_items[3];

			gr_complex *out0 = (gr_complex *) output_items[0];
			gr_complex *out1 = (gr_complex *) output_items[1];
			gr_complex *out2 = (gr_complex *) output_items[2];
			gr_complex *out3 = (gr_complex *) output_items[3];

			//calculate antenna spacing distances
			float dx0 = -1*(d_dx+d_dx/2);	// <-- antenna furthest left
			float dx1 = -1*d_dx/2;		// <-- antenna left of center
			float dx2 = d_dx/2;		// <-- antenna right of center
			float dx3 = d_dx+d_dx/2;	// <-- antenna furthest right


			float phase0 = -1*(d_ph0 + 2*M_PI/(d_wl) * (sqrt(d_Rs*d_Rs+dx0*dx0-2*d_Rs*dx0*sin(d_theta))-d_Rs));
			float phase1 = -1*(d_ph0 + 2*M_PI/(d_wl) * (sqrt(d_Rs*d_Rs+dx1*dx1-2*d_Rs*dx1*sin(d_theta))-d_Rs));
			float phase2 = -1*(d_ph0 + 2*M_PI/(d_wl) * (sqrt(d_Rs*d_Rs+dx2*dx2-2*d_Rs*dx2*sin(d_theta))-d_Rs));
			float phase3 = -1*(d_ph0 + 2*M_PI/(d_wl) * (sqrt(d_Rs*d_Rs+dx3*dx3-2*d_Rs*dx3*sin(d_theta))-d_Rs));

			for(int i = 0; i < noutput_items; i++) {
				out0[i] = in0[i]*gr_complex(cos(phase0),sin(phase0));
				out1[i] = in1[i]*gr_complex(cos(phase1),sin(phase1));
				out2[i] = in2[i]*gr_complex(cos(phase2),sin(phase2));
				out3[i] = in3[i]*gr_complex(cos(phase3),sin(phase3));
			}

			return noutput_items;
		}

		void rev_phase_shifter_impl::set_Rs(float Rs) {d_Rs = Rs;}
		void rev_phase_shifter_impl::set_dx(float dx) {d_dx = dx;}
		void rev_phase_shifter_impl::set_theta(float theta) {d_theta = theta;}
		void rev_phase_shifter_impl::set_wl(float wl) {d_wl = wl;}
		void rev_phase_shifter_impl::set_ph0(float ph0) {d_ph0 = ph0;}

  	}
}
