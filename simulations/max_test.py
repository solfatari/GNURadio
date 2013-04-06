#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Max Test
# Generated: Sat Apr  6 14:03:23 2013
##################################################

from gnuradio import analog
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

class max_test(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Max Test")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.window = window = 512
		self.var_amp = var_amp = .1
		self.samp_rate = samp_rate = 32000

		##################################################
		# Blocks
		##################################################
		_var_amp_sizer = wx.BoxSizer(wx.VERTICAL)
		self._var_amp_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_var_amp_sizer,
			value=self.var_amp,
			callback=self.set_var_amp,
			label='var_amp',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._var_amp_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_var_amp_sizer,
			value=self.var_amp,
			callback=self.set_var_amp,
			minimum=-.5,
			maximum=.5,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_var_amp_sizer)
		self.wxgui_scopesink2_0_0 = scopesink2.scope_sink_c(
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
		self.Add(self.wxgui_scopesink2_0_0.win)
		self.gr_vector_to_stream_0_0 = gr.vector_to_stream(gr.sizeof_gr_complex*1, window)
		self.gr_vector_to_stream_0 = gr.vector_to_stream(gr.sizeof_gr_complex*1, window)
		self.gr_stream_to_vector_1 = gr.stream_to_vector(gr.sizeof_gr_complex*1, window)
		self.gr_stream_to_vector_0 = gr.stream_to_vector(gr.sizeof_gr_complex*1, window)
		self.gr_null_source_3 = gr.null_source(gr.sizeof_gr_complex*window)
		self.gr_null_source_2 = gr.null_source(gr.sizeof_gr_complex*window)
		self.gr_null_sink_3 = gr.null_sink(gr.sizeof_gr_complex*window)
		self.gr_null_sink_2 = gr.null_sink(gr.sizeof_gr_complex*window)
		self.eecs_max_vec_0 = eecs.max_vec(512)
		self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1+var_amp, 0)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 5)

		##################################################
		# Connections
		##################################################
		self.connect((self.eecs_max_vec_0, 2), (self.gr_null_sink_3, 0))
		self.connect((self.eecs_max_vec_0, 3), (self.gr_null_sink_2, 0))
		self.connect((self.gr_stream_to_vector_0, 0), (self.eecs_max_vec_0, 0))
		self.connect((self.gr_stream_to_vector_1, 0), (self.eecs_max_vec_0, 1))
		self.connect((self.gr_null_source_2, 0), (self.eecs_max_vec_0, 3))
		self.connect((self.gr_null_source_3, 0), (self.eecs_max_vec_0, 2))
		self.connect((self.analog_sig_source_x_0_0, 0), (self.gr_stream_to_vector_0, 0))
		self.connect((self.analog_sig_source_x_0, 0), (self.gr_stream_to_vector_1, 0))
		self.connect((self.eecs_max_vec_0, 1), (self.gr_vector_to_stream_0, 0))
		self.connect((self.gr_vector_to_stream_0, 0), (self.wxgui_scopesink2_0_0, 1))
		self.connect((self.gr_vector_to_stream_0_0, 0), (self.wxgui_scopesink2_0_0, 0))
		self.connect((self.eecs_max_vec_0, 0), (self.gr_vector_to_stream_0_0, 0))


	def get_window(self):
		return self.window

	def set_window(self, window):
		self.window = window

	def get_var_amp(self):
		return self.var_amp

	def set_var_amp(self, var_amp):
		self.var_amp = var_amp
		self.analog_sig_source_x_0_0.set_amplitude(1+self.var_amp)
		self._var_amp_slider.set_value(self.var_amp)
		self._var_amp_text_box.set_value(self.var_amp)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink2_0_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = max_test()
	tb.Run(True)

