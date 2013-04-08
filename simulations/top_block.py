#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sun Apr  7 23:25:19 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import window
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
		self.samp_rate = samp_rate = 32000
		self.offset = offset = 100
		self.fft_window = fft_window = 2**10

		##################################################
		# Blocks
		##################################################
		_offset_sizer = wx.BoxSizer(wx.VERTICAL)
		self._offset_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_offset_sizer,
			value=self.offset,
			callback=self.set_offset,
			label='offset',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._offset_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_offset_sizer,
			value=self.offset,
			callback=self.set_offset,
			minimum=0,
			maximum=1000,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_offset_sizer)
		self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "tab1")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "tab2")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "tab3")
		self.Add(self.nb)
		self.wxgui_scopesink2_1_0 = scopesink2.scope_sink_f(
			self.nb.GetPage(2).GetWin(),
			title="FFT_add",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.nb.GetPage(2).Add(self.wxgui_scopesink2_1_0.win)
		self.wxgui_scopesink2_1 = scopesink2.scope_sink_c(
			self.nb.GetPage(0).GetWin(),
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
		self.nb.GetPage(0).Add(self.wxgui_scopesink2_1.win)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.nb.GetPage(1).GetWin(),
			title="Outputs",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=2,
			trig_mode=gr.gr_TRIG_MODE_STRIPCHART,
			y_axis_label="Counts",
		)
		self.nb.GetPage(1).Add(self.wxgui_scopesink2_0.win)
		self.gr_null_source_0 = gr.null_source(gr.sizeof_gr_complex*1)
		self.gr_complex_to_real_0 = gr.complex_to_real(1)
		self.fft_vxx_0_0 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 1)
		self.fft_vxx_0 = fft.fft_vcc(1024, True, (window.blackmanharris(1024)), True, 1)
		self.eecs_fft_max_0 = eecs.fft_max(fft_window)
		self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_add_xx_0 = blocks.add_vcc(fft_window)
		self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000+offset, 1, 0)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 1000, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0, 0))
		self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_vxx_0, 0))
		self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
		self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_throttle_0_0, 0))
		self.connect((self.blocks_throttle_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))
		self.connect((self.eecs_fft_max_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.eecs_fft_max_0, 1), (self.wxgui_scopesink2_0, 1))
		self.connect((self.blocks_vector_to_stream_0, 0), (self.wxgui_scopesink2_1, 0))
		self.connect((self.blocks_vector_to_stream_1, 0), (self.wxgui_scopesink2_1, 1))
		self.connect((self.fft_vxx_0, 0), (self.blocks_vector_to_stream_0, 0))
		self.connect((self.fft_vxx_0_0, 0), (self.blocks_vector_to_stream_1, 0))
		self.connect((self.gr_null_source_0, 0), (self.blocks_stream_to_vector_0_0_0, 0))
		self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.eecs_fft_max_0, 1))
		self.connect((self.fft_vxx_0, 0), (self.blocks_add_xx_0, 0))
		self.connect((self.fft_vxx_0_0, 0), (self.blocks_add_xx_0, 1))
		self.connect((self.blocks_add_xx_0, 0), (self.eecs_fft_max_0, 0))
		self.connect((self.blocks_add_xx_0, 0), (self.blocks_vector_to_stream_0_0, 0))
		self.connect((self.gr_complex_to_real_0, 0), (self.wxgui_scopesink2_1_0, 0))
		self.connect((self.blocks_vector_to_stream_0_0, 0), (self.gr_complex_to_real_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.blocks_throttle_0.set_sample_rate(self.samp_rate)
		self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink2_1.set_sample_rate(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_scopesink2_1_0.set_sample_rate(self.samp_rate)

	def get_offset(self):
		return self.offset

	def set_offset(self, offset):
		self.offset = offset
		self._offset_slider.set_value(self.offset)
		self._offset_text_box.set_value(self.offset)
		self.analog_sig_source_x_0_0.set_frequency(1000+self.offset)

	def get_fft_window(self):
		return self.fft_window

	def set_fft_window(self, fft_window):
		self.fft_window = fft_window
		self.eecs_fft_max_0.set_window(self.fft_window)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

