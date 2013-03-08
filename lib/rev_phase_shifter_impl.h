#ifndef INCLUDED_EECS_REV_PHASE_SHIFTER_IMPL_H
#define INCLUDED_EECS_REV_PHASE_SHIFTER_IMPL_H

#include <eecs/rev_phase_shifter.h>

namespace gr {
	namespace eecs {

		class rev_phase_shifter_impl : public rev_phase_shifter
		{
			private:
			float d_Rs;
			float d_dx;
			float d_theta;
			float d_wl;
			float d_ph0;

			public:
			rev_phase_shifter_impl(float Rs, float dx, float theta, float wl, float ph0);
			~rev_phase_shifter_impl();

			float Rs() const { return d_Rs; }
			float dx() const { return d_dx; }
			float theta() const { return d_theta; }
			float wl() const { return d_wl; }
			float ph0() const { return d_ph0; }

			void set_Rs(float Rs);
			void set_dx(float dx);
			void set_theta(float theta);
			void set_wl(float wl);
			void set_ph0(float ph0);

			int work(int noutput_items,
			       gr_vector_const_void_star &input_items,
			       gr_vector_void_star &output_items);
		};

	}
}

#endif
