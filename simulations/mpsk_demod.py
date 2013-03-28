#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: MPSK Demod Demo
# Generated: Wed Mar 27 11:38:58 2013
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from gnuradio.gr import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import forms
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
		self.fc = fc = 32000
		self.wl = wl = 300e6/fc
		self.theta = theta = 0
		self.samps_per_sym = samps_per_sym = 2
		self.samp_rate = samp_rate = 10*fc
		self.noise = noise = .1
		self.n_samp = n_samp = 2**4

		##################################################
		# Blocks
		##################################################
		self.notebook = self.notebook = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "Constellations BA")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "2nd Tier")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "1st Tier 1/2")
		self.notebook.AddPage(grc_wxgui.Panel(self.notebook), "1st Tier 3/4")
		self.Add(self.notebook)
		_theta_sizer = wx.BoxSizer(wx.VERTICAL)
		self._theta_text_box = forms.text_box(
			parent=self.notebook.GetPage(0).GetWin(),
			sizer=_theta_sizer,
			value=self.theta,
			callback=self.set_theta,
			label="theta",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._theta_slider = forms.slider(
			parent=self.notebook.GetPage(0).GetWin(),
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
		self.notebook.GetPage(0).Add(_theta_sizer)
		_noise_sizer = wx.BoxSizer(wx.VERTICAL)
		self._noise_text_box = forms.text_box(
			parent=self.notebook.GetPage(0).GetWin(),
			sizer=_noise_sizer,
			value=self.noise,
			callback=self.set_noise,
			label="Noise",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._noise_slider = forms.slider(
			parent=self.notebook.GetPage(0).GetWin(),
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
		self.notebook.GetPage(0).Add(_noise_sizer)
		self.wxgui_constellationsink2_0_0_0_0_1_0_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(1).GetWin(),
			title="Restored Constellation Plot",
			sample_rate=fc,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=fc/2,
			omega_limit=0.005,
			size=((250,300)),
		)
		self.notebook.GetPage(1).Add(self.wxgui_constellationsink2_0_0_0_0_1_0_0.win)
		self.wxgui_constellationsink2_0_0_0_0_1_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(1).GetWin(),
			title="Restored Constellation Plot",
			sample_rate=fc,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=fc/2,
			omega_limit=0.005,
			size=((250,300)),
		)
		self.notebook.GetPage(1).Add(self.wxgui_constellationsink2_0_0_0_0_1_0.win)
		self.wxgui_constellationsink2_0_0_0_0_1 = constsink_gl.const_sink_c(
			self.notebook.GetPage(3).GetWin(),
			title="Restored Constellation Plot",
			sample_rate=fc,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=fc/2,
			omega_limit=0.005,
			size=((250,300)),
		)
		self.notebook.GetPage(3).Add(self.wxgui_constellationsink2_0_0_0_0_1.win)
		self.wxgui_constellationsink2_0_0_0_0_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(3).GetWin(),
			title="Restored Constellation Plot",
			sample_rate=fc,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=fc/2,
			omega_limit=0.005,
			size=((250,300)),
		)
		self.notebook.GetPage(3).Add(self.wxgui_constellationsink2_0_0_0_0_0.win)
		self.wxgui_constellationsink2_0_0_0_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(2).GetWin(),
			title="Restored Constellation Plot",
			sample_rate=fc,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=fc/2,
			omega_limit=0.005,
			size=((250,300)),
		)
		self.notebook.GetPage(2).Add(self.wxgui_constellationsink2_0_0_0_0.win)
		self.wxgui_constellationsink2_0_0_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(2).GetWin(),
			title="Restored Constellation Plot",
			sample_rate=fc,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=fc/2,
			omega_limit=0.005,
			size=((250,300)),
		)
		self.notebook.GetPage(2).Add(self.wxgui_constellationsink2_0_0_0.win)
		self.wxgui_constellationsink2_0_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(0).GetWin(),
			title="Restored Constellation Plot",
			sample_rate=fc,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=fc/2,
			omega_limit=0.005,
			size=((400,300)),
		)
		self.notebook.GetPage(0).Add(self.wxgui_constellationsink2_0_0.win)
		self.wxgui_constellationsink2_0 = constsink_gl.const_sink_c(
			self.notebook.GetPage(0).GetWin(),
			title="Constellation Plot",
			sample_rate=fc,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=fc/2.,
			omega_limit=0.005,
			size=((400,300)),
		)
		self.notebook.GetPage(0).Add(self.wxgui_constellationsink2_0.win)
		self.random_source_x_0 = gr.vector_source_b(map(int, numpy.random.randint(0, 2**4, 10000)), True)
		self.gr_throttle_0_0 = gr.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.gr_throttle_0 = gr.throttle(gr.sizeof_gr_complex*1, fc)
		self.eecs_x_corr_0_2 = eecs.x_corr(fc, samp_rate, n_samp)
		self.eecs_x_corr_0_0 = eecs.x_corr(fc, samp_rate, n_samp)
		self.eecs_x_corr_0 = eecs.x_corr(fc, samp_rate, n_samp)
		self.eecs_phase_shifter_0_0 = eecs.phase_shifter(20*wl, wl/2, theta*math.pi/180, wl, 0)
		self.digital_dxpsk_mod_0 = digital.dbpsk_mod(
			samples_per_symbol=samps_per_sym,
			excess_bw=0.35,
			gray_coded=True,
			verbose=False,
			log=False)
			
		self.channel_model_0 = filter.channel_model(
			noise_voltage=noise,
			frequency_offset=0.0,
			epsilon=1.0,
			taps=(1.0 + 1.0j, ),
			noise_seed=0,
		)
		self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
		self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, fc, 1, 0)

		##################################################
		# Connections
		##################################################
		self.connect((self.random_source_x_0, 0), (self.digital_dxpsk_mod_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 3), (self.wxgui_constellationsink2_0_0_0_0_1, 0))
		self.connect((self.eecs_phase_shifter_0_0, 2), (self.wxgui_constellationsink2_0_0_0_0_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 1), (self.wxgui_constellationsink2_0_0_0_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 0), (self.wxgui_constellationsink2_0_0_0, 0))
		self.connect((self.blocks_multiply_xx_0, 0), (self.gr_throttle_0_0, 0))
		self.connect((self.gr_throttle_0_0, 0), (self.eecs_phase_shifter_0_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 0), (self.eecs_x_corr_0, 0))
		self.connect((self.eecs_phase_shifter_0_0, 1), (self.eecs_x_corr_0, 1))
		self.connect((self.eecs_phase_shifter_0_0, 3), (self.eecs_x_corr_0_0, 1))
		self.connect((self.eecs_phase_shifter_0_0, 2), (self.eecs_x_corr_0_0, 0))
		self.connect((self.eecs_x_corr_0, 0), (self.eecs_x_corr_0_2, 0))
		self.connect((self.eecs_x_corr_0_0, 0), (self.eecs_x_corr_0_2, 1))
		self.connect((self.eecs_x_corr_0_2, 0), (self.wxgui_constellationsink2_0_0, 0))
		self.connect((self.analog_sig_source_x_0, 0), (self.blocks_multiply_xx_0, 1))
		self.connect((self.gr_throttle_0, 0), (self.blocks_multiply_xx_0, 0))
		self.connect((self.eecs_x_corr_0, 0), (self.wxgui_constellationsink2_0_0_0_0_1_0, 0))
		self.connect((self.eecs_x_corr_0_0, 0), (self.wxgui_constellationsink2_0_0_0_0_1_0_0, 0))
		self.connect((self.channel_model_0, 0), (self.gr_throttle_0, 0))
		self.connect((self.digital_dxpsk_mod_0, 0), (self.channel_model_0, 0))
		self.connect((self.gr_throttle_0_0, 0), (self.wxgui_constellationsink2_0, 0))


	def get_fc(self):
		return self.fc

	def set_fc(self, fc):
		self.fc = fc
		self.set_samp_rate(10*self.fc)
		self.eecs_x_corr_0.set_freq(self.fc)
		self.eecs_x_corr_0_0.set_freq(self.fc)
		self.set_wl(300e6/self.fc)
		self.analog_sig_source_x_0.set_frequency(self.fc)
		self.eecs_x_corr_0_2.set_freq(self.fc)
		self.gr_throttle_0.set_sample_rate(self.fc)
		self.wxgui_constellationsink2_0_0.set_sample_rate(self.fc)
		self.wxgui_constellationsink2_0_0_0_0_1_0_0.set_sample_rate(self.fc)
		self.wxgui_constellationsink2_0_0_0_0_1_0.set_sample_rate(self.fc)
		self.wxgui_constellationsink2_0_0_0_0_1.set_sample_rate(self.fc)
		self.wxgui_constellationsink2_0_0_0.set_sample_rate(self.fc)
		self.wxgui_constellationsink2_0_0_0_0_0.set_sample_rate(self.fc)
		self.wxgui_constellationsink2_0_0_0_0.set_sample_rate(self.fc)
		self.wxgui_constellationsink2_0.set_sample_rate(self.fc)

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
		self.eecs_phase_shifter_0_0.set_theta(self.theta*math.pi/180)
		self._theta_slider.set_value(self.theta)
		self._theta_text_box.set_value(self.theta)

	def get_samps_per_sym(self):
		return self.samps_per_sym

	def set_samps_per_sym(self, samps_per_sym):
		self.samps_per_sym = samps_per_sym

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.eecs_x_corr_0.set_sampRate(self.samp_rate)
		self.eecs_x_corr_0_0.set_sampRate(self.samp_rate)
		self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
		self.eecs_x_corr_0_2.set_sampRate(self.samp_rate)
		self.gr_throttle_0_0.set_sample_rate(self.samp_rate)

	def get_noise(self):
		return self.noise

	def set_noise(self, noise):
		self.noise = noise
		self.channel_model_0.set_noise_voltage(self.noise)
		self._noise_slider.set_value(self.noise)
		self._noise_text_box.set_value(self.noise)

	def get_n_samp(self):
		return self.n_samp

	def set_n_samp(self, n_samp):
		self.n_samp = n_samp
		self.eecs_x_corr_0.set_nSamples(self.n_samp)
		self.eecs_x_corr_0_0.set_nSamples(self.n_samp)
		self.eecs_x_corr_0_2.set_nSamples(self.n_samp)

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = mpsk_demod()
	tb.Run(True)

