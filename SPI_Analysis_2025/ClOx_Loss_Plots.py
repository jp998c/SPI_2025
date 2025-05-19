#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed April 9 2025

@author: jp998c
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cftime as cft

from toolkit import ChemicalData as cd
from toolkit import chemical_toolbox as ct
from np_data_list import *

# Loading relevant data from np_data/clox_loss/

CESM_lat = np.load("np_data/CESM_lat.npy")
CESM_lev = np.load("np_data/CESM_lev.npy")

bl_clox = np.load("np_data/clox_loss/Baseline_ClOx_Loss_2044-2064_30N-60N_ZM.npy")
sai15_clox = np.load("np_data/clox_loss/SAI1.5_ClOx_Loss_2044-2064_30N-60N_ZM.npy")
sai10_clox = np.load("np_data/clox_loss/SAI1.0_ClOx_Loss_2044-2064_30N-60N_ZM.npy")
sai05_clox = np.load("np_data/clox_loss/SAI0.5_ClOx_Loss_2044-2064_30N-60N_ZM.npy")
print(sai05_clox)
#sai1_0 = 
#sai0_5 = 
spi_30N_clox = np.load("np_data/clox_loss/SPI_30N_ClOx_Loss_2044-2064_30N-60N_ZM.npy")
spi_30S_clox = np.load("np_data/clox_loss/SPI_30S_ClOx_Loss_2044-2064_30N-60N_ZM.npy")
spi_15N_clox = np.load("np_data/clox_loss/SPI_15N_ClOx_Loss_2044-2064_30N-60N_ZM.npy")
spi_15S_clox = np.load("np_data/clox_loss/SPI_15S_ClOx_Loss_2044-2064_30N-60N_ZM.npy")
spi_0N_clox = np.load("np_data/clox_loss/SPI_0N_ClOx_Loss_2044-2064_30N-60N_ZM.npy")

scalef = 10**5

bl_abs = bl_clox / scalef
sai15_abs = (sai15_clox-bl_clox) / scalef
sai10_abs = (sai10_clox-bl_clox) / scalef
sai05_abs = (sai05_clox-bl_clox) / scalef
spi_30N_abs = (spi_30N_clox-bl_clox) / scalef
spi_15N_abs = (spi_15N_clox-bl_clox) / scalef
spi_0N_abs = (spi_0N_clox-bl_clox) / scalef
spi_15S_abs = (spi_15S_clox-bl_clox) / scalef
spi_30S_abs = (spi_30S_clox-bl_clox) / scalef

sai15_percent = (sai15_clox-bl_clox) / bl_clox
sai10_percent = (sai10_clox-bl_clox) / bl_clox
sai05_percent = (sai05_clox-bl_clox) / bl_clox
spi_30N_percent = (spi_30N_clox-bl_clox) / bl_clox
spi_15N_percent = (spi_15N_clox-bl_clox) / bl_clox
spi_0N_percent = (spi_0N_clox-bl_clox)  / bl_clox
spi_15S_percent = (spi_15S_clox-bl_clox) / bl_clox
spi_30S_percent = (spi_30S_clox-bl_clox) / bl_clox

# linecolors for each dataset
sai15_color = "#2A47DB"
sai10_color = "#2A7FDB"
sai05_color = "#2AB7DB"

spi_30N_color = "#ED1717"
spi_15N_color = "#F24D11"
spi_0N_color = "#F6830C"
spi_15S_color = "#FBB806"
spi_30S_color = "#FFEE00"
bl_color = "#000000"

gauss_width = 5
spi_width = 2

year_range = (2044, 2064)
lat_range = ("30N", "60N")

# PLOT DATA

zeroes = np.zeros(len(CESM_lev))

ylog_lim = [300, 5]
x_lim = [-0.2,0.3]
fig, (ax, ax2) = plt.subplots(1, 2,figsize=(12,6), layout='constrained')
fig.suptitle(f"OddOx_CloxBrox Rate Differences From Baseline [{lat_range[0]}-{lat_range[1]}]")

# Absolute Changes
z0 = ax.axvline(0, color='black',linestyle='--')
l0, = ax.plot(sai15_abs, CESM_lev, label='SAI 1.5', color=sai15_color, linewidth=gauss_width)
l1, = ax.plot(sai10_abs, CESM_lev, label='SAI 1.0', color=sai10_color, linewidth=gauss_width)
l2, = ax.plot(sai05_abs, CESM_lev, label='SAI 0.5', color=sai05_color, linewidth=gauss_width)
l3, = ax.plot(spi_30N_abs, CESM_lev, label='SPI 30N', color=spi_30N_color, linewidth=spi_width)
l4, = ax.plot(spi_15N_abs, CESM_lev, label='SPI 15N', color=spi_15N_color, linewidth=spi_width)
l5, = ax.plot(spi_0N_abs, CESM_lev, label='SPI EQ', color=spi_0N_color, linewidth=spi_width)
l6, = ax.plot(spi_15S_abs, CESM_lev, label='SPI 15S', color=spi_15S_color, linewidth=spi_width)
l7, = ax.plot(spi_30S_abs, CESM_lev, label='SPI 30S', color=spi_30S_color, linewidth=spi_width)

ax.set_title("Absolute Change")
ax.set_yscale('log')
ax.set_ylim(ylog_lim)
ax.set_xlim(x_lim)
ax.set_ylabel("pressure (hPa)")
ax.set_xlabel("Rate (molecule/cm3/sec) $10^5$")
#ax.set_xticks(xtick_val, xtick_txt)

ylog_lim = [300, 5]
x_lim = [-0.5,3]

# Percent Changes
z0 = ax2.axvline(0, color='black', linestyle='--')
l0, = ax2.plot(sai15_percent, CESM_lev, label='SAI 1.5', color=sai15_color, linewidth=gauss_width)
l1, = ax2.plot(sai10_percent, CESM_lev, label='SAI 1.0', color=sai10_color, linewidth=gauss_width)
l2, = ax2.plot(sai05_percent, CESM_lev, label='SAI 0.5', color=sai05_color, linewidth=gauss_width)
l3, = ax2.plot(spi_30N_percent, CESM_lev, label='SPI 30N', color=spi_30N_color, linewidth=spi_width)
l4, = ax2.plot(spi_15N_percent, CESM_lev, label='SPI 15N', color=spi_15N_color, linewidth=spi_width)
l5, = ax2.plot(spi_0N_percent, CESM_lev, label='SPI EQ', color=spi_0N_color, linewidth=spi_width)
l6, = ax2.plot(spi_15S_percent, CESM_lev, label='SPI 15S', color=spi_15S_color, linewidth=spi_width)
l7, = ax2.plot(spi_30S_percent, CESM_lev, label='SPI 30S', color=spi_30S_color, linewidth=spi_width)
fig.legend(handles=[l0, l1, l2, l3, l4, l5, l6, l7], loc='outside right')

ax2.set_title("Percent Change")
ax2.set_yscale('log')
ax2.set_ylim(ylog_lim)
ax2.set_xlim(x_lim)
#ax2.set_ylabel("pressure (hPa)")
ax2.set_xlabel("% Change in Rate")
#ax.set_xticks(xtick_val, xtick_txt)

fig.savefig(img_dir + 'ClOxBrOx_comparisons.png', dpi=300)
plt.show()