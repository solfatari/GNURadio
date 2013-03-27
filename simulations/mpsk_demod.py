#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: MPSK Demod Demo
# Generated: Tue Mar 26 23:22:52 2013
##################################################

execfile("/home/chris/.grc_gnuradio/freq_match_2.py")
from gnuradio import analog
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import window
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import fftsink2
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import eecs
import math
import numpy
import wx

class mpsk_demod(grc_wxgui.top_block_gui):

	def __init__(self):
		grc_wxgui.top_block_gui.__init__(self, title="MPSK Demod Demo")
		_icon_path = "/usr/share/icons/hicolor/32x32/apps/gnuradio-grc.png"
		self.SetIcon(wx.Icon(_icon_path, wx.BITMAP_TYPE_ANY))

		##################################################
		# Variables
		##################################################
		self.fc = fc = 2000
		self.wl = wl = 300e6/fc
		self.theta = theta = 0
		self.samps_per_sym = samps_per_sym = 4
		self.samp_rate = samp_rate = 32000
		self.noise = noise = 0
		self.n_samp = n_samp = 52
		self.freq_off = freq_off = 0

		##################################################
		# Blocks
		##################################################
		self.notebook = self.notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Constellation")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Spectrum")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Complex Scope")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Phased Output")
		self.Add(self.notebook)
		_theta_sizer = wx.BoxSizer(wx.VERTICAL)
		self._theta_text_box = forms.text_box(
			parent=self.notebook.GetPage(3).GetWin(),
			sizer=_theta_sizer,
			value=self.theta,
			callback=self.set_theta,
			label="theta",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._theta_slider = forms.slider(
			parent=self.notebook.GetPage(3).GetWin(),
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
		self.notebook.GetPage(3).Add(_theta_sizer)
		_noise_sizer = wx.BoxSizer(wx.VERTICAL)
		self._noise_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_noise_sizer,
			value=self.noise,
			callback=self.set_noise,
			label="Noise",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._noise_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_noise_sizer,
			value=self.noise,
			callback=self.set_noise,
			minimum=0,
			maximum=1,
			num_steps=100,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_noise_sizer)
		_freq_off_sizer = wx.BoxSizer(wx.VERTICAL)
		self._freq_off_text_box = forms.text_box(
			parent=self.GetWin(),
			sizer=_freq_off_sizer,
			value=self.freq_off,
			callback=self.set_freq_off,
			label="Freq Offset",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._freq_off_slider = forms.slider(
			parent=self.GetWin(),
			sizer=_freq_off_sizer,
			value=self.freq_off,
			callback=self.set_freq_off,
			minimum=-.5,
			maximum=.5,
			num_steps=1000,
			style=wx.SL_HORIZONTAL,
			cast=float,
			proportion=1,
		)
		self.Add(_freq_off_sizer)
		self.wxgui_scopesink2_0_0_0_0_0 = scopesink2.scope_sink_f(
			self.notebook.GetPage(3).GetWin(),
			title="1st Rephasing",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=2,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
			size=((400,150)),
		)
		self.notebook.GetPage(3).Add(self.wxgui_scopesink2_0_0_0_0_0.win)
		self.wxgui_scopesink2_0_0_0_0 = scopesink2.scope_sink_f(
			self.notebook.GetPage(3).GetWin(),
			title="Phased Signals",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=4,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
			size=((400,150)),
		)
		self.notebook.GetPage(3).Add(self.wxgui_scopesink2_0_0_0_0.win)
		self.wxgui_fftsink2_0_0 = fftsink2.fft_sink_c(
			self.notebook.GetPage(1).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=50,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=30,
			average=False,
			avg_alpha=None,
			title="FFT Plot, up",
			peak_hold=False,
			size=((400,300)),
		)
		self.notebook.GetPage(1).Add(self.wxgui_fftsink2_0_0.win)
		self.wxgui_fftsink2_0 = fftsink2.fft_sink_c(
			self.notebook.GetPage(1).GetWin(),
			baseband_freq=0,
			y_per_div=10,
			y_divs=10,
			ref_level=50,
			ref_scale=2.0,
			sample_rate=samp_rate,
			fft_size=1024,
			fft_rate=30,
			average=False,
			avg_alpha=None,
			title="FFT Plot",
			peak_hold=False,
			size=((400,300)),
		)
		self.notebook.GetPage(1).Add(self.wxgui_fftsink2_0.win)
		self.wxgui_constellationsink2_0_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(0).GetWin(),
			title="Restored Constellation Plot",
			sample_rate=samp_rate,
			frame_rate=5,
			const_size=2048,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=samp_rate/4.,
			omega_limit=0.005,
			size=((250,300)),
		)
		self.notebook.GetPage(0).Add(self.wxgui_constellationsink2_0_0.win)
		self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(0).GetWin(),
			title="Constellation Plot",
			sample_rate=samp_rate,
			frame_rate=5,
			const_size=2048,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=samp_rate/4.,
			omega_limit=0.005,
			size=((250,300)),
		)
		self.notebook.GetPage(0).Add(self.wxgui_constellationsink2_0.win)
		self.random_source_x_0 = gr.vector_source_b(map(int, numpy.random.randint(0, 2**8, 10000)), True)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.gr_complex_to_real_0_4 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_3 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_2 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_1 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_0 = gr.complex_to_real(1)
		self.gr_complex_to_real_0 = gr.complex_to_real(1)
		self.gr_channel_model_0 = gr.channel_model(
			noise_voltage=noise,
			frequency_offset=freq_off,
			epsilon=1.0,
			taps=(1.0, ),
			noise_seed=42,
		)
		self.freq_match_2_0 = freq_match_2()
		self.eecs_x_corr_0_1 = eecs.x_corr(fc, samp_rate, n_samp)
		self.eecs_x_corr_0_0 = eecs.x_corr(fc, samp_rate, n_samp)
		self.eecs_x_corr_0 = eecs.x_corr(fc, samp_rate, n_samp)
		self.eecs_phase_shifter_0_0 = eecs.phase_shifter(20*wl, wl/2, theta*math.pi/180, wl, 0)
		self.digital_dxpsk_mod_0 = digital.dqpsk_mod(
			samples_per_symbol=samps_per_sym,
			excess_bw=0.35,
			gray_coded=True,
			verbose=False,
			log=False)
			
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, fc, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_channel_model_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.digital_dxpsk_mod_0, 0), (self.gr_channel_model_0, 0))
		self.connect((self.random_source_x_0, 0), (self.digital_dxpsk_mod_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.wxgui_fftsink2_0, 0))
		self.connect((self.gr_throttle_0, 0), (self.wxgui_constellationsink2_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 0), (self.gr_complex_to_real_0, 0))
		self.connect((self.gr_complex_to_real_0, 0), (self.wxgui_scopesink2_0_0_0_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 0), (self.eecs_x_corr_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 1), (self.eecs_x_corr_0, 1))
		self.connect((self.eecs_phase_shifter_0_0, 2), (self.eecs_x_corr_0_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 3), (self.eecs_x_corr_0_0, 1))
		self.connect((self.eecs_x_corr_0, 0), (self.eecs_x_corr_0_1, 0))
		self.connect((self.eecs_x_corr_0_0, 0), (self.eecs_x_corr_0_1, 1))
		self.connect((self.eecs_x_corr_0_1, 0), (self.wxgui_constellationsink2_0_0, 0))
		self.connect((self.gr_complex_to_real_0_3, 0), (self.wxgui_scopesink2_0_0_0_0_0, 0))
		self.connect((self.gr_complex_to_real_0_4, 0), (self.wxgui_scopesink2_0_0_0_0_0, 1))
		self.connect((self.eecs_x_corr_0, 0), (self.gr_complex_to_real_0_3, 0))
		self.connect((self.eecs_x_corr_0_0, 0), (self.gr_complex_to_real_0_4, 0))
		self.connect((self.gr_complex_to_real_0_0, 0), (self.wxgui_scopesink2_0_0_0_0, 1))
		self.connect((self.gr_complex_to_real_0_1, 0), (self.wxgui_scopesink2_0_0_0_0, 2))
		self.connect((self.gr_complex_to_real_0_2, 0), (self.wxgui_scopesink2_0_0_0_0, 3))
		self.connect((self.eecs_phase_shifter_0_0, 3), (self.gr_complex_to_real_0_2, 0))
		self.connect((self.eecs_phase_shifter_0_0, 2), (self.gr_complex_to_real_0_1, 0))
		self.connect((self.eecs_phase_shifter_0_0, 1), (self.gr_complex_to_real_0_0, 0))
		self.connect((self.freq_match_2_0, 0), (self.wxgui_fftsink2_0_0, 0))
		self.connect((self.analog_sig_source_x_0, 0), (self.freq_match_2_0, 1))
		self.connect((self.freq_match_2_0, 0), (self.eecs_phase_shifter_0_0, 0))
		self.connect((self.gr_channel_model_0, 0), (self.freq_match_2_0, 0))


	def get_fc(self):
		return self.fc

	def set_fc(self, fc):
		self.fc = fc
		self.set_wl(300e6/self.fc)
		self.eecs_x_corr_0.set_freq(self.fc)
		self.eecs_x_corr_0_0.set_freq(self.fc)
		self.eecs_x_corr_0_1.set_freq(self.fc)
		self.analog_sig_source_x_0.set_frequency(self.fc)

	def get_wl(self):
		return self.wl

	def set_wl(self, wl):
		self.wl = wl
		self.eecs_phase_shifter_0_0.set_Rs(20*self.wl)
		self.eecs_phase_shifter_0_0.set_wl(self.wl)

	def get_theta(self):
		return self.theta

	def set_theta(self, theta):
		self.theta = theta
		self._theta_slider.set_value(self.theta)
		self._theta_text_box.set_value(self.theta)
		self.eecs_phase_shifter_0_0.set_theta(self.theta*math.pi/180)

	def get_samps_per_sym(self):
		return self.samps_per_sym

	def set_samps_per_sym(self, samps_per_sym):
		self.samps_per_sym = samps_per_sym

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.wxgui_constellationsink2_0_0.set_sample_rate(self.samp_rate)
		self.wxgui_constellationsink2_0.set_sample_rate(self.samp_rate)
		self.eecs_x_corr_0.set_sampRate(self.samp_rate)
		self.eecs_x_corr_0_0.set_sampRate(self.samp_rate)
		self.wxgui_scopesink2_0_0_0_0.set_sample_rate(self.samp_rate)
		self.wxgui_scopesink2_0_0_0_0_0.set_sample_rate(self.samp_rate)
		self.eecs_x_corr_0_1.set_sampRate(self.samp_rate)
		self.wxgui_fftsink2_0.set_sample_rate(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.wxgui_fftsink2_0_0.set_sample_rate(self.samp_rate)
		self.gr_throttle_0.set_sample_rate(self.samp_rate)

	def get_noise(self):
		return self.noise

	def set_noise(self, noise):
		self.noise = noise
		self._noise_slider.set_value(self.noise)
		self._noise_text_box.set_value(self.noise)
		self.gr_channel_model_0.set_noise_voltage(self.noise)

	def get_n_samp(self):
		return self.n_samp

	def set_n_samp(self, n_samp):
		self.n_samp = n_samp
		self.eecs_x_corr_0.set_nSamples(self.n_samp)
		self.eecs_x_corr_0_0.set_nSamples(self.n_samp)
		self.eecs_x_corr_0_1.set_nSamples(self.n_samp)

	def get_freq_off(self):
		return self.freq_off

	def set_freq_off(self, freq_off):
		self.freq_off = freq_off
		self._freq_off_slider.set_value(self.freq_off)
		self._freq_off_text_box.set_value(self.freq_off)
		self.gr_channel_model_0.set_frequency_offset(self.freq_off)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = mpsk_demod()
	tb.Run(True)

