#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Tue Apr 16 21:02:38 2013
##################################################

from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import eecs
import math
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="untouched",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=2,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0_0.win)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="inversion",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=2,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		self.gr_null_sink_0_2 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_null_sink_0_0 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_multiply_const_vxx_0 = gr.multiply_const_vcc((-1, ))
		self.gr_complex_to_real_0_2 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_1 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_0 = gr.complex_to_real(1)
		self.gr_complex_to_real_0 = gr.complex_to_real(1)
		self.eecs_xcor_inversion_cc_0 = eecs.xcor_inversion_cc(2**7)
		self.eecs_phase_shifter_0 = eecs.phase_shifter(20*3e8/3000, 3e8/3000/2, 75, 3e8/3000, 0)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 3000, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.analog_sig_source_x_0, 0), (self.eecs_phase_shifter_0, 0))
		self.connect((self.eecs_phase_shifter_0, 3), (self.gr_null_sink_0_2, 0))
		self.connect((self.eecs_phase_shifter_0, 2), (self.gr_null_sink_0_0, 0))
		self.connect((self.gr_complex_to_real_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.gr_complex_to_real_0_0, 0), (self.wxgui_scopesink2_0, 1))
		self.connect((self.eecs_xcor_inversion_cc_0, 1), (self.gr_complex_to_real_0_0, 0))
		self.connect((self.eecs_xcor_inversion_cc_0, 0), (self.gr_complex_to_real_0, 0))
		self.connect((self.gr_complex_to_real_0_1, 0), (self.wxgui_scopesink2_0_0, 0))
		self.connect((self.gr_complex_to_real_0_2, 0), (self.wxgui_scopesink2_0_0, 1))
		self.connect((self.eecs_phase_shifter_0, 1), (self.gr_complex_to_real_0_2, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.gr_complex_to_real_0_1, 0))
		self.connect((self.eecs_phase_shifter_0, 0), (self.gr_multiply_const_vxx_0, 0))
		self.connect((self.gr_multiply_const_vxx_0, 0), (self.eecs_xcor_inversion_cc_0, 0))
		self.connect((self.eecs_phase_shifter_0, 1), (self.eecs_xcor_inversion_cc_0, 1))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

