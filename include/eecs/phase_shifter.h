#ifndef INCLUDED_EECS_PHASE_SHIFTER_H
#define INCLUDED_EECS_PHASE_SHIFTER_H

#include <eecs/api.h>
#include <gr_sync_block.h>

namespace gr {
	namespace eecs {

		class EECS_API phase_shifter : virtual public gr_sync_block
		{
			public:

			typedef boost::shared_ptr<phase_shifter> sptr;

			static sptr make(float Rs, float dx, float theta, float wl, float ph0);

			virtual float Rs() const = 0;
			virtual float dx() const = 0;
			virtual float theta() const = 0;
			virtual float wl() const = 0;
			virtual float ph0() const = 0;

			virtual void set_Rs(float Rs) = 0;
			virtual void set_dx(float dx) = 0;
			virtual void set_theta(float theta) = 0;
			virtual void set_wl(float wl) = 0;
			virtual void set_ph0(float ph0) = 0;

		};

	}
}

#endif
