#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Mar  7 17:32:23 2013
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
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.theta = theta = 3.14159/8
		self.samp_rate = samp_rate = 32000
		self.freq = freq = 1000

		##################################################
		# Blocks
		##################################################
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=4,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.Add(self.wxgui_scopesink2_0.win)
		_theta_sizer = wx.BoxSizer(wx.VERTICAL)
		self._theta_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_theta_sizer,
			value=self.theta,
			callback=self.set_theta,
			label='theta',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._theta_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_theta_sizer,
			value=self.theta,
			callback=self.set_theta,
			minimum=-3.14159/2,
			maximum=3.14159/2,
			num_steps=180,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_theta_sizer)
		self.gr_complex_to_real_0_2 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_1 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_0 = gr.complex_to_real(1)
		self.gr_complex_to_real_0 = gr.complex_to_real(1)
		self.eecs_d_theta_0 = eecs.d_theta(freq=freq, rSat=10, thetaSat=0, sampRate=samp_rate)
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, freq, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.eecs_d_theta_0, 3), (self.gr_complex_to_real_0_0, 0))
		self.connect((self.eecs_d_theta_0, 2), (self.gr_complex_to_real_0_1, 0))
		self.connect((self.eecs_d_theta_0, 1), (self.gr_complex_to_real_0_2, 0))
		self.connect((self.eecs_d_theta_0, 0), (self.gr_complex_to_real_0, 0))
		self.connect((self.gr_complex_to_real_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.gr_complex_to_real_0_2, 0), (self.wxgui_scopesink2_0, 1))
		self.connect((self.gr_complex_to_real_0_1, 0), (self.wxgui_scopesink2_0, 2))
		self.connect((self.gr_complex_to_real_0_0, 0), (self.wxgui_scopesink2_0, 3))
		self.connect((self.blocks_throttle_0, 0), (self.eecs_d_theta_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.eecs_d_theta_0, 1))
		self.connect((self.blocks_throttle_0, 0), (self.eecs_d_theta_0, 2))
		self.connect((self.blocks_throttle_0, 0), (self.eecs_d_theta_0, 3))
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))


	def get_theta(self):
		return self.theta

	def set_theta(self, theta):
		self.theta = theta
		self._theta_slider.set_value(self.theta)
		self._theta_text_box.set_value(self.theta)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.blocks_throttle_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

	def get_freq(self):
		return self.freq

	def set_freq(self, freq):
		self.freq = freq
		self.analog_sig_source_x_0.set_frequency(self.freq)
		self.eecs_d_theta_0.set_freq(self.freq)
		self.eecs_d_theta_0.set_rSat(self.freq)
		self.eecs_d_theta_0.set_thetaSat(self.freq)
		self.eecs_d_theta_0.set_sampRate(self.freq)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)
