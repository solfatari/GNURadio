#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Thu Mar  7 15:01:45 2013
##################################################

execfile("/home/sdr/.grc_gnuradio/two_sim.py")
from gnuradio import analog
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 100000
		self.dthetas = dthetas = 0

		##################################################
		# Blocks
		##################################################
		_dthetas_sizer = wx.BoxSizer(wx.VERTICAL)
		self._dthetas_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_dthetas_sizer,
			value=self.dthetas,
			callback=self.set_dthetas,
			label="dthetas",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._dthetas_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_dthetas_sizer,
			value=self.dthetas,
			callback=self.set_dthetas,
			minimum=-180,
			maximum=180,
			num_steps=360,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_dthetas_sizer)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.GetWin(),
			title="Scope Plot",
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
		self.two_sim_0 = two_sim(
			samp_rate=samp_rate,
			dtheta=dthetas,
		)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.gr_complex_to_real_0_0 = gr.complex_to_real(1)
		self.gr_complex_to_real_0 = gr.complex_to_real(1)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 10000, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.analog_sig_source_x_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.two_sim_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.gr_complex_to_real_0, 0))
		self.connect((self.two_sim_0, 0), (self.gr_complex_to_real_0_0, 0))
		self.connect((self.gr_complex_to_real_0_0, 0), (self.wxgui_scopesink2_0, 1))
		self.connect((self.gr_complex_to_real_0, 0), (self.wxgui_scopesink2_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.gr_throttle_0.set_sample_rate(self.samp_rate)
		self.two_sim_0.set_samp_rate(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)

	def get_dthetas(self):
		return self.dthetas

	def set_dthetas(self, dthetas):
		self.dthetas = dthetas
		self._dthetas_slider.set_value(self.dthetas)
		self._dthetas_text_box.set_value(self.dthetas)
		self.two_sim_0.set_dtheta(self.dthetas)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

