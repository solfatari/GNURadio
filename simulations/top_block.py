#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Top Block
# Generated: Sat Mar 30 16:49:29 2013
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.gr import firdes
from gnuradio.wxgui import constsink_gl
from gnuradio.wxgui import forms
from gnuradio.wxgui import scopesink2
from grc_gnuradio import wxgui as grc_wxgui
from optparse import OptionParser
import eecs
import math
import numpy
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
		self.samps_per_sym = samps_per_sym = 4
		self.samp_rate = samp_rate = fc*20
		self.wl = wl = 300e6/fc
		self.theta = theta = 0
		self.sym_rate = sym_rate = samp_rate/samps_per_sym
		self.noise = noise = .1
		self.n_samp = n_samp = 1024

		##################################################
		# Blocks
		##################################################
		self.notebook_0 = self.notebook_0 = wx.Notebook(self.GetWin(), style=wx.NB_TOP)
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Raw Const")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Constalations")
		self.notebook_0.AddPage(grc_wxgui.Panel(self.notebook_0), "Clock Sync Const")
		self.Add(self.notebook_0)
		_theta_sizer = wx.BoxSizer(wx.VERTICAL)
		self._theta_text_box = forms.text_box(
			parent=self.notebook_0.GetPage(2).GetWin(),
			sizer=_theta_sizer,
			value=self.theta,
			callback=self.set_theta,
			label="theta",
			converter=forms.float_converter(),
			proportion=0,
		)
		self._theta_slider = forms.slider(
			parent=self.notebook_0.GetPage(2).GetWin(),
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
		self.notebook_0.GetPage(2).Add(_theta_sizer)
		_noise_sizer = wx.BoxSizer(wx.VERTICAL)
		self._noise_text_box = forms.text_box(
			parent=self.notebook_0.GetPage(1).GetWin(),
			sizer=_noise_sizer,
			value=self.noise,
			callback=self.set_noise,
			label='noise',
			converter=forms.float_converter(),
			proportion=0,
		)
		self._noise_slider = forms.slider(
			parent=self.notebook_0.GetPage(1).GetWin(),
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
		self.notebook_0.GetPage(1).Add(_noise_sizer)
		self.wxgui_scopesink2_0_1_0 = scopesink2.scope_sink_f(
			self.notebook_0.GetPage(2).GetWin(),
			title="Correlated Output",
			sample_rate=samp_rate,
			v_scale=1.5,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=2,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.notebook_0.GetPage(2).Add(self.wxgui_scopesink2_0_1_0.win)
		self.wxgui_scopesink2_0_1 = scopesink2.scope_sink_f(
			self.notebook_0.GetPage(0).GetWin(),
			title="Phased Output",
			sample_rate=samp_rate,
			v_scale=0,
			v_offset=0,
			t_scale=0,
			ac_couple=False,
			xy_mode=False,
			num_inputs=3,
			trig_mode=gr.gr_TRIG_MODE_AUTO,
			y_axis_label="Counts",
		)
		self.notebook_0.GetPage(0).Add(self.wxgui_scopesink2_0_1.win)
		self.wxgui_constellationsink2_0_1 = constsink_gl.const_sink_c(
			self.notebook_0.GetPage(1).GetWin(),
			title="Constellation Plot",
			sample_rate=samp_rate,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=sym_rate,
			omega_limit=0.005,
		)
		self.notebook_0.GetPage(1).Add(self.wxgui_constellationsink2_0_1.win)
		self.wxgui_constellationsink2_0_0 = constsink_gl.const_sink_c(
			self.notebook_0.GetPage(1).GetWin(),
			title="Noise Constellation Plot",
			sample_rate=samp_rate,
			frame_rate=5,
			const_size=2048/2,
			M=4,
			theta=0,
			loop_bw=6.28/100.0,
			fmax=0.06,
			mu=0.5,
			gain_mu=0.005,
			symbol_rate=sym_rate,
			omega_limit=0.005,
		)
		self.notebook_0.GetPage(1).Add(self.wxgui_constellationsink2_0_0.win)
		self.random_source_x_0 = gr.vector_source_b(map(int, numpy.random.randint(0, 256, 2**4)), True)
		self.gr_null_sink_0_1 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_null_sink_0_0 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_null_sink_0 = gr.null_sink(gr.sizeof_gr_complex*1)
		self.gr_complex_to_real_0_3_1 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_3_0 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_3 = gr.complex_to_real(1)
		self.gr_complex_to_real_0_2 = gr.complex_to_real(1)
		self.gr_complex_to_real_0 = gr.complex_to_real(1)
		self.gr_channel_model_0 = gr.channel_model(
			noise_voltage=noise,
			frequency_offset=0,
			epsilon=1.0,
			taps=(1.0, ),
			noise_seed=42,
		)
		self.eecs_xcor2_0 = eecs.xcor2(2**16)
		self.eecs_phase_shifter_0 = eecs.phase_shifter(20*wl, wl/2, theta*math.pi/180, wl, 0)
		self.digital_dxpsk_mod_0 = digital.dqpsk_mod(
			samples_per_symbol=samps_per_sym,
			excess_bw=0.35,
			gray_coded=False,
			verbose=False,
			log=False)
			
		self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate)
		self.blocks_add_xx_1 = blocks.add_vcc(1)

		##################################################
		# Connections
		##################################################
		self.connect((self.gr_complex_to_real_0_3, 0), (self.wxgui_scopesink2_0_1_0, 0))
		self.connect((self.gr_complex_to_real_0, 0), (self.wxgui_scopesink2_0_1, 0))
		self.connect((self.gr_complex_to_real_0_2, 0), (self.wxgui_scopesink2_0_1, 1))
		self.connect((self.eecs_xcor2_0, 0), (self.gr_complex_to_real_0_3, 0))
		self.connect((self.eecs_xcor2_0, 1), (self.gr_complex_to_real_0_3_0, 0))
		self.connect((self.gr_complex_to_real_0_3_0, 0), (self.wxgui_scopesink2_0_1_0, 1))
		self.connect((self.blocks_add_xx_1, 0), (self.wxgui_constellationsink2_0_1, 0))
		self.connect((self.eecs_xcor2_0, 0), (self.blocks_add_xx_1, 0))
		self.connect((self.eecs_xcor2_0, 1), (self.blocks_add_xx_1, 1))
		self.connect((self.random_source_x_0, 0), (self.digital_dxpsk_mod_0, 0))
		self.connect((self.digital_dxpsk_mod_0, 0), (self.gr_channel_model_0, 0))
		self.connect((self.gr_channel_model_0, 0), (self.blocks_throttle_0_0, 0))
		self.connect((self.blocks_throttle_0_0, 0), (self.wxgui_constellationsink2_0_0, 0))
		self.connect((self.blocks_add_xx_1, 0), (self.gr_complex_to_real_0_3_1, 0))
		self.connect((self.gr_complex_to_real_0_3_1, 0), (self.wxgui_scopesink2_0_1, 2))
		self.connect((self.eecs_xcor2_0, 2), (self.gr_null_sink_0, 0))
		self.connect((self.blocks_throttle_0_0, 0), (self.eecs_phase_shifter_0, 0))
		self.connect((self.eecs_phase_shifter_0, 0), (self.eecs_xcor2_0, 0))
		self.connect((self.eecs_phase_shifter_0, 1), (self.eecs_xcor2_0, 1))
		self.connect((self.eecs_phase_shifter_0, 2), (self.gr_null_sink_0_0, 0))
		self.connect((self.eecs_phase_shifter_0, 3), (self.gr_null_sink_0_1, 0))
		self.connect((self.eecs_phase_shifter_0, 0), (self.gr_complex_to_real_0, 0))
		self.connect((self.eecs_phase_shifter_0, 1), (self.gr_complex_to_real_0_2, 0))


	def get_fc(self):
		return self.fc

	def set_fc(self, fc):
		self.fc = fc
		self.set_wl(300e6/self.fc)
		self.set_samp_rate(self.fc*20)

	def get_samps_per_sym(self):
		return self.samps_per_sym

	def set_samps_per_sym(self, samps_per_sym):
		self.samps_per_sym = samps_per_sym
		self.set_sym_rate(self.samp_rate/self.samps_per_sym)

	def get_samp_rate(self):
		return self.samp_rate

	def set_samp_rate(self, samp_rate):
		self.samp_rate = samp_rate
		self.set_sym_rate(self.samp_rate/self.samps_per_sym)
		self.wxgui_scopesink2_0_1_0.set_sample_rate(self.samp_rate)
		self.wxgui_scopesink2_0_1.set_sample_rate(self.samp_rate)
		self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)
		self.wxgui_constellationsink2_0_1.set_sample_rate(self.samp_rate)
		self.wxgui_constellationsink2_0_0.set_sample_rate(self.samp_rate)

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

	def get_sym_rate(self):
		return self.sym_rate

	def set_sym_rate(self, sym_rate):
		self.sym_rate = sym_rate

	def get_noise(self):
		return self.noise

	def set_noise(self, noise):
		self.noise = noise
		self.gr_channel_model_0.set_noise_voltage(self.noise)
		self._noise_slider.set_value(self.noise)
		self._noise_text_box.set_value(self.noise)

	def get_n_samp(self):
		return self.n_samp

	def set_n_samp(self, n_samp):
		self.n_samp = n_samp

if __name__ == '__main__':
	parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
	(options, args) = parser.parse_args()
	tb = top_block()
	tb.Run(True)

