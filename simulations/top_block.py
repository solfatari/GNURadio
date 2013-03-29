#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Mar 28 22:46:26 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
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
		self.fc = fc = 1000
		self.wl = wl = 300e6/fc
		self.theta = theta = 0
		self.samp_rate = samp_rate = fc*10

		##################################################
		# Blocks
		##################################################
		_theta_sizer = wx.BoxSizer(wx.VERTICAL)
		self._theta_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_theta_sizer,
			value=self.theta,
			callback=self.set_theta,
			label="theta",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._theta_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_theta_sizer,
			value=self.theta,
			callback=self.set_theta,
			minimum=-1*math.pi/2*0+-90,
			maximum=math.pi/2*0+90,
			num_steps=360*0+180,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_theta_sizer)
		self.wxgui_scopesink2_0_0_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=3,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
			size=((700,200)),
		)
		self.Add(self.wxgui_scopesink2_0_0_0.win)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.gr_null_sink_1 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_null_sink_0_0 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_complex_to_real_0_2_1_0_0 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_2_1_0 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_2_1 = gr.complex_to_real(1)
		self.eecs_xcor2_0 = eecs.xcor2(samp_rate, 2**8)
		self.eecs_phase_shifter_0 = eecs.phase_shifter(20*wl, wl/2, theta*math.pi/180, wl, 0)
		self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_SIN_WAVE, fc, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.analog_sig_source_x_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.eecs_phase_shifter_0, 0))
		self.connect((self.eecs_phase_shifter_0, 1), (self.gr_complex_to_real_0_2_1, 0))
		self.connect((self.eecs_phase_shifter_0, 2), (self.gr_null_sink_0_0, 0))
		self.connect((self.eecs_phase_shifter_0, 3), (self.gr_null_sink_0, 0))
		self.connect((self.gr_complex_to_real_0_2_1_0_0, 0), (self.wxgui_scopesink2_0_0_0, 1))
		self.connect((self.gr_complex_to_real_0_2_1_0, 0), (self.wxgui_scopesink2_0_0_0, 0))
		self.connect((self.eecs_phase_shifter_0, 1), (self.eecs_xcor2_0, 1))
		self.connect((self.eecs_xcor2_0, 1), (self.gr_complex_to_real_0_2_1_0_0, 0))
		self.connect((self.blocks_conjugate_cc_0, 0), (self.eecs_xcor2_0, 0))
		self.connect((self.eecs_xcor2_0, 0), (self.gr_null_sink_1, 0))
		self.connect((self.eecs_phase_shifter_0, 0), (self.blocks_conjugate_cc_0, 0))
		self.connect((self.eecs_phase_shifter_0, 0), (self.gr_complex_to_real_0_2_1_0, 0))
		self.connect((self.gr_complex_to_real_0_2_1, 0), (self.wxgui_scopesink2_0_0_0, 2))


	def get_fc(self):
		return self.fc

	def set_fc(self, fc):
		self.fc = fc
		self.set_wl(300e6/self.fc)
		self.analog_sig_source_x_0.set_frequency(self.fc)
		self.set_samp_rate(self.fc*10)

	def get_wl(self):
		return self.wl

	def set_wl(self, wl):
		self.wl = wl
		self.eecs_phase_shifter_0.set_Rs(20*self.wl)
		self.eecs_phase_shifter_0.set_wl(self.wl)

	def get_theta(self):
		return self.theta

	def set_theta(self, theta):
		self.theta = theta
		self._theta_slider.set_value(self.theta)
		self._theta_text_box.set_value(self.theta)
		self.eecs_phase_shifter_0.set_theta(self.theta*math.pi/180)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.gr_throttle_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink2_0_0_0.set_sample_rate(self.samp_rate)
		self.eecs_xcor2_0.set_sampRate(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

