#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sun Mar 24 10:56:40 2013
##################################################

from gnuradio import analog
from gnuradio import digital
from gnuradio import eng_notation
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
import math
import osmosdr
import wx

class top_block(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="Top Block")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.samp_rate = samp_rate = 2.5e6
		self.decim = decim = 1
		self.post_decim = post_decim = samp_rate/decim
		self.freq_ctr2 = freq_ctr2 = 990e6
		self.freq_ctr1 = freq_ctr1 = 990e6
		self.cutoff = cutoff = 1e4*5

		##################################################
		# Blocks
		##################################################
		self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "1")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "2")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "3")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "4")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "5")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "6")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "7")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "8")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "9")
		self.Add(self.notebook_0)
		_freq_ctr1_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq_ctr1_text_box = forms.text_box(
			parent=self.notebook_0.GetPage(0).GetWin(),
			sizer=_freq_ctr1_sizer,
			value=self.freq_ctr1,
			callback=self.set_freq_ctr1,
			label="center frequency",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq_ctr1_slider = forms.slider(
			parent=self.notebook_0.GetPage(0).GetWin(),
			sizer=_freq_ctr1_sizer,
			value=self.freq_ctr1,
			callback=self.set_freq_ctr1,
			minimum=989.1e6,
			maximum=990.1e6,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.notebook_0.GetPage(0).Add(_freq_ctr1_sizer)
		self.wxgui_scopesink2_1_0 = scopesink2.scope_sink_c(
			self.notebook_0.GetPage(3).GetWin(),
			title="Scope Plot",
			sample_rate=post_decim,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.notebook_0.GetPage(3).Add(self.wxgui_scopesink2_1_0.win)
		self.wxgui_scopesink2_1 = scopesink2.scope_sink_c(
			self.notebook_0.GetPage(2).GetWin(),
			title="Scope Plot",
			sample_rate=post_decim,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=1,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.notebook_0.GetPage(2).Add(self.wxgui_scopesink2_1.win)
		self.wxgui_numbersink2_0_0_0_1 = numbersink2.number_sink_f(
			self.notebook_0.GetPage(1).GetWin(),
			unit="Hz",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate*0+post_decim,
			number_rate=15,
			average=False,
			avg_alpha=0.001,
			label="phase",
			peak_hold=False,
			show_gauge=False,
		)
		self.notebook_0.GetPage(1).Add(self.wxgui_numbersink2_0_0_0_1.win)
		self.wxgui_numbersink2_0_0_0_0 = numbersink2.number_sink_f(
			self.notebook_0.GetPage(1).GetWin(),
			unit="Hz",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate*0+post_decim,
			number_rate=15,
			average=False,
			avg_alpha=0.001,
			label="error",
			peak_hold=False,
			show_gauge=False,
		)
		self.notebook_0.GetPage(1).Add(self.wxgui_numbersink2_0_0_0_0.win)
		self.wxgui_numbersink2_0_0_0 = numbersink2.number_sink_f(
			self.notebook_0.GetPage(1).GetWin(),
			unit="Hz",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate*0+post_decim,
			number_rate=15,
			average=False,
			avg_alpha=0.001,
			label="freq",
			peak_hold=False,
			show_gauge=False,
		)
		self.notebook_0.GetPage(1).Add(self.wxgui_numbersink2_0_0_0.win)
		self.wxgui_numbersink2_0_0 = numbersink2.number_sink_c(
			self.notebook_0.GetPage(1).GetWin(),
			unit="",
			minval=-100,
			maxval=100,
			factor=1.0,
			decimal_places=10,
			ref_level=0,
			sample_rate=samp_rate*0+post_decim,
			number_rate=15,
			average=False,
			avg_alpha=0.001,
			label="signal",
			peak_hold=False,
			show_gauge=False,
		)
		self.notebook_0.GetPage(1).Add(self.wxgui_numbersink2_0_0.win)
		self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
			self.notebook_0.GetPage(0).GetWin(),
			baseband_freq=freq_ctr1,
			y_per_div=10,
			y_divs=5,
			ref_level=-10,
			ref_scale=2.0,
			sample_rate=samp_rate*0+post_decim,
			fft_size=1024,
			fft_rate=15,
			average=True,
			avg_alpha=0.2,
			title="FFT Plot",
			peak_hold=False,
		)
		self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.notebook_0.GetPage(0).GetWin(),
			baseband_freq=freq_ctr1,
			y_per_div=10,
			y_divs=5,
			ref_level=-10,
			ref_scale=2.0,
			sample_rate=samp_rate*0+post_decim,
			fft_size=1024,
			fft_rate=15,
			average=True,
			avg_alpha=0.2,
			title="FFT Plot",
			peak_hold=False,
		)
		self.notebook_0.GetPage(0).Add(self.wxgui_fftsink2_0.win)
		self.osmosdr_source_c_0 = osmosdr.source_c( args="nchan=" + str(1) + " " + "rtl=0,xtal=28.8e6,tuner_xtal=28.8e6" )
		self.osmosdr_source_c_0.set_sample_rate(samp_rate)
		self.osmosdr_source_c_0.set_center_freq(freq_ctr1, 0)
		self.osmosdr_source_c_0.set_freq_corr(0, 0)
		self.osmosdr_source_c_0.set_iq_balance_mode(2, 0)
		self.osmosdr_source_c_0.set_gain_mode(1, 0)
		self.osmosdr_source_c_0.set_gain(0, 0)
		self.osmosdr_source_c_0.set_if_gain(0, 0)
			
		self.low_pass_filter_0 = gr.fir_filter_ccf(decim, firdes.low_pass(
			1, samp_rate, samp_rate/4, samp_rate/4, firdes.WIN_HAMMING, 6.76))
		_freq_ctr2_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq_ctr2_text_box = forms.text_box(
			parent=self.notebook_0.GetPage(4).GetWin(),
			sizer=_freq_ctr2_sizer,
			value=self.freq_ctr2,
			callback=self.set_freq_ctr2,
			label="center frequency",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq_ctr2_slider = forms.slider(
			parent=self.notebook_0.GetPage(4).GetWin(),
			sizer=_freq_ctr2_sizer,
			value=self.freq_ctr2,
			callback=self.set_freq_ctr2,
			minimum=989.1e6,
			maximum=990.1e6,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.notebook_0.GetPage(4).Add(_freq_ctr2_sizer)
		self.digital_fll_band_edge_cc_0 = digital.fll_band_edge_cc(2, .05, 512, .008)
		self.analog_pll_refout_cc_0 = analog.pll_refout_cc(math.pi/1000, 2, -2)

		##################################################
		# Connections
		##################################################
		self.connect((self.low_pass_filter_0, 0), (self.wxgui_fftsink2_0_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.wxgui_scopesink2_1_0, 0))
		self.connect((self.digital_fll_band_edge_cc_0, 2), (self.wxgui_numbersink2_0_0_0_1, 0))
		self.connect((self.digital_fll_band_edge_cc_0, 3), (self.wxgui_numbersink2_0_0_0_0, 0))
		self.connect((self.osmosdr_source_c_0, 0), (self.low_pass_filter_0, 0))
		self.connect((self.low_pass_filter_0, 0), (self.digital_fll_band_edge_cc_0, 0))
		self.connect((self.digital_fll_band_edge_cc_0, 1), (self.wxgui_numbersink2_0_0_0, 0))
		self.connect((self.digital_fll_band_edge_cc_0, 0), (self.analog_pll_refout_cc_0, 0))
		self.connect((self.analog_pll_refout_cc_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.analog_pll_refout_cc_0, 0), (self.wxgui_scopesink2_1, 0))
		self.connect((self.analog_pll_refout_cc_0, 0), (self.wxgui_numbersink2_0_0, 0))


	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.set_post_decim(self.samp_rate/self.decim)
		self.osmosdr_source_c_0.set_sample_rate(self.samp_rate)
		self.low_pass_filter_0.set_taps(firdes.low_pass(1, self.samp_rate, self.samp_rate/4, self.samp_rate/4, firdes.WIN_HAMMING, 6.76))
		self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate*0+self.post_decim)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate*0+self.post_decim)

	def get_decim(self):
		return self.decim

	def set_decim(self, decim):
		self.decim = decim
		self.set_post_decim(self.samp_rate/self.decim)

	def get_post_decim(self):
		return self.post_decim

	def set_post_decim(self, post_decim):
		self.post_decim = post_decim
		self.wxgui_scopesink2_1.set_sample_rate(self.post_decim)
		self.wxgui_scopesink2_1_0.set_sample_rate(self.post_decim)
		self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate*0+self.post_decim)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate*0+self.post_decim)

	def get_freq_ctr2(self):
		return self.freq_ctr2

	def set_freq_ctr2(self, freq_ctr2):
		self.freq_ctr2 = freq_ctr2
		self._freq_ctr2_slider.set_value(self.freq_ctr2)
		self._freq_ctr2_text_box.set_value(self.freq_ctr2)

	def get_freq_ctr1(self):
		return self.freq_ctr1

	def set_freq_ctr1(self, freq_ctr1):
		self.freq_ctr1 = freq_ctr1
		self.osmosdr_source_c_0.set_center_freq(self.freq_ctr1, 0)
		self._freq_ctr1_slider.set_value(self.freq_ctr1)
		self._freq_ctr1_text_box.set_value(self.freq_ctr1)
		self.wxgui_fftsink2_0_0.set_baseband_freq(self.freq_ctr1)
		self.wxgui_fftsink2_0.set_baseband_freq(self.freq_ctr1)

	def get_cutoff(self):
		return self.cutoff

	def set_cutoff(self, cutoff):
		self.cutoff = cutoff

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

