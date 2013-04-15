#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Mon Apr  8 22:58:36 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import fft
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import numbersink2
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
		self.fft_window = fft_window = 2**10
		self.window_type = window_type = window.hamming(fft_window)
		self.samp_rate = samp_rate = 2**20
		self.offset = offset = 200
		self.fft_shift = fft_shift = 1

		##################################################
		# Blocks
		##################################################
		self.nb = self.nb = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "tab1")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "fft_max")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "tab3")
		self.nb.AddPage(grc_wxgui.Panel(self.nb), "tab4")
		self.Add(self.nb)
		_offset_sizer = wx.BoxSizer(wx.VERTICAL)
		self._offset_text_box = forms.text_box(
			parent=self.nb.GetPage(1).GetWin(),
			sizer=_offset_sizer,
			value=self.offset,
			callback=self.set_offset,
			label='offset',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._offset_slider = forms.slider(
			parent=self.nb.GetPage(1).GetWin(),
			sizer=_offset_sizer,
			value=self.offset,
			callback=self.set_offset,
			minimum=0,
			maximum=2000,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.nb.GetPage(1).Add(_offset_sizer)
		_fft_shift_sizer = wx.BoxSizer(wx.VERTICAL)
		self._fft_shift_text_box = forms.text_box(
			parent=self.nb.GetPage(2).GetWin(),
			sizer=_fft_shift_sizer,
			value=self.fft_shift,
			callback=self.set_fft_shift,
			label='fft_shift',
			converter=forms.int_converter(),
			proportion=0,
		)
		self._fft_shift_slider = forms.slider(
			parent=self.nb.GetPage(2).GetWin(),
			sizer=_fft_shift_sizer,
			value=self.fft_shift,
			callback=self.set_fft_shift,
			minimum=0,
			maximum=100,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=int,
			proportion=1,
		)
		self.nb.GetPage(2).Add(_fft_shift_sizer)
		self.wxgui_scopesink2_0 = scopesink2.scope_sink_f(
			self.nb.GetPage(3).GetWin(),
			title="Reference/Offset/Shifted",
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
		self.nb.GetPage(3).Add(self.wxgui_scopesink2_0.win)
		self.wxgui_numbersink2_0_0_0 = numbersink2.number_sink_f(
			self.nb.GetPage(1).GetWin(),
			unit="Units",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate,
			number_rate=15,
			average=False,
			avg_alpha=None,
			label="Shifted Output",
			peak_hold=False,
			show_gauge=True,
		)
		self.nb.GetPage(1).Add(self.wxgui_numbersink2_0_0_0.win)
		self.wxgui_numbersink2_0_0 = numbersink2.number_sink_f(
			self.nb.GetPage(1).GetWin(),
			unit="Units",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate,
			number_rate=15,
			average=False,
			avg_alpha=None,
			label="Channel2",
			peak_hold=False,
			show_gauge=True,
		)
		self.nb.GetPage(1).Add(self.wxgui_numbersink2_0_0.win)
		self.wxgui_numbersink2_0 = numbersink2.number_sink_f(
			self.nb.GetPage(1).GetWin(),
			unit="Units",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate,
			number_rate=15,
			average=False,
			avg_alpha=None,
			label="Channel1",
			peak_hold=False,
			show_gauge=True,
		)
		self.nb.GetPage(1).Add(self.wxgui_numbersink2_0.win)
		self.wxgui_fftsink2_0_0_0 = fftsink2.fft_sink_c(
			self.nb.GetPage(0).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=fft_window,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
			win=window.blackmanharris,
		)
		self.nb.GetPage(0).Add(self.wxgui_fftsink2_0_0_0.win)
		self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
			self.nb.GetPage(0).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=fft_window,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
			win=window.blackmanharris,
		)
		self.nb.GetPage(0).Add(self.wxgui_fftsink2_0_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.nb.GetPage(2).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=0,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=fft_window,
			fft_rate=15,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
		)
		self.nb.GetPage(2).Add(self.wxgui_fftsink2_0.win)
		self.gr_null_source_0 = gr.null_source(gr.sizeof_gr_complex*fft_window)
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_float*fft_window)
		self.gr_complex_to_real_0_0_0 = gr.complex_to_real(1)
		self.gr_complex_to_real_0 = gr.complex_to_real(1)
		self.fft_vxx_0_0_0 = fft.fft_vcc(fft_window, False, (window_type), True, 1)
		self.fft_vxx_0_0 = fft.fft_vcc(fft_window, True, (window_type), True, 1)
		self.fft_vxx_0 = fft.fft_vcc(fft_window, True, (window_type), True, 1)
		self.eecs_fft_shift_0 = eecs.fft_shift(fft_window, fft_shift)
		self.eecs_fft_max_0_0 = eecs.fft_max(fft_window)
		self.eecs_fft_max_0 = eecs.fft_max(fft_window)
		self.blocks_vector_to_stream_0_0_0_1_0 = blocks.vector_to_stream(gr.sizeof_float*1, fft_window)
		self.blocks_vector_to_stream_0_0_0_1 = blocks.vector_to_stream(gr.sizeof_float*1, fft_window)
		self.blocks_vector_to_stream_0_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, fft_window)
		self.blocks_vector_to_stream_0_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, 3*samp_rate)
		self.blocks_throttle_0 = blocks.throttle(gr.sizeof_gr_complex*1, 3*samp_rate)
		self.blocks_stream_to_vector_0_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, fft_window)
		self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((2**-10, ))
		self.analog_sig_source_x_0_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 4000+offset, 1, 0)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, 4000, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.blocks_throttle_0, 0), (self.wxgui_fftsink2_0_0, 0))
		self.connect((self.blocks_throttle_0_0, 0), (self.wxgui_fftsink2_0_0_0, 0))
		self.connect((self.analog_sig_source_x_0_0, 0), (self.blocks_throttle_0_0, 0))
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle_0, 0))
		self.connect((self.blocks_vector_to_stream_0_0_0_0, 0), (self.wxgui_numbersink2_0, 0))
		self.connect((self.blocks_vector_to_stream_0_0_0_1, 0), (self.wxgui_numbersink2_0_0, 0))
		self.connect((self.blocks_vector_to_stream_0_0_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.fft_vxx_0_0_0, 0), (self.blocks_vector_to_stream_0_0_0, 0))
		self.connect((self.eecs_fft_max_0_0, 0), (self.blocks_vector_to_stream_0_0_0_1_0, 0))
		self.connect((self.eecs_fft_max_0_0, 1), (self.gr_null_sink_0, 0))
		self.connect((self.blocks_vector_to_stream_0_0_0_1_0, 0), (self.wxgui_numbersink2_0_0_0, 0))
		self.connect((self.blocks_vector_to_stream_0_0_0, 0), (self.blocks_multiply_const_vxx_0, 0))
		self.connect((self.blocks_multiply_const_vxx_0, 0), (self.gr_complex_to_real_0, 0))
		self.connect((self.gr_complex_to_real_0_0_0, 0), (self.wxgui_scopesink2_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.gr_complex_to_real_0_0_0, 0))
		self.connect((self.gr_complex_to_real_0, 0), (self.wxgui_scopesink2_0, 1))
		self.connect((self.gr_null_source_0, 0), (self.eecs_fft_max_0_0, 1))
		self.connect((self.eecs_fft_shift_0, 0), (self.eecs_fft_max_0_0, 0))
		self.connect((self.fft_vxx_0_0, 0), (self.eecs_fft_max_0, 1))
		self.connect((self.eecs_fft_max_0, 1), (self.blocks_vector_to_stream_0_0_0_1, 0))
		self.connect((self.fft_vxx_0_0, 0), (self.eecs_fft_shift_0, 0))
		self.connect((self.eecs_fft_shift_0, 0), (self.fft_vxx_0_0_0, 0))
		self.connect((self.eecs_fft_max_0, 0), (self.blocks_vector_to_stream_0_0_0_0, 0))
		self.connect((self.fft_vxx_0, 0), (self.eecs_fft_max_0, 0))
		self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_vxx_0_0, 0))
		self.connect((self.blocks_stream_to_vector_0_0_0, 0), (self.fft_vxx_0, 0))
		self.connect((self.blocks_throttle_0, 0), (self.blocks_stream_to_vector_0_0_0, 0))
		self.connect((self.blocks_throttle_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))


	def get_fft_window(self):
		return self.fft_window

	def set_fft_window(self, fft_window):
		self.fft_window = fft_window
		self.set_window_type(window.hamming(self.fft_window))
		self.eecs_fft_shift_0.set_window(self.fft_window)
		self.eecs_fft_max_0.set_window(self.fft_window)
		self.eecs_fft_max_0_0.set_window(self.fft_window)

	def get_window_type(self):
		return self.window_type

	def set_window_type(self, window_type):
		self.window_type = window_type

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.analog_sig_source_x_0_0.set_sampling_freq(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
		self.wxgui_fftsink2_0_0_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.wxgui_scopesink2_0.set_sample_rate(self.samp_rate)
		self.blocks_throttle_0.set_sample_rate(3*self.samp_rate)
		self.blocks_throttle_0_0.set_sample_rate(3*self.samp_rate)

	def get_offset(self):
		return self.offset

	def set_offset(self, offset):
		self.offset = offset
		self.analog_sig_source_x_0_0.set_frequency(4000+self.offset)
		self._offset_slider.set_value(self.offset)
		self._offset_text_box.set_value(self.offset)

	def get_fft_shift(self):
		return self.fft_shift

	def set_fft_shift(self, fft_shift):
		self.fft_shift = fft_shift
		self._fft_shift_slider.set_value(self.fft_shift)
		self._fft_shift_text_box.set_value(self.fft_shift)
		self.eecs_fft_shift_0.set_shift(self.fft_shift)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

