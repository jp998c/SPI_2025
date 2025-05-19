#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed April 9 2025

@author: jp998c
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pdtha
import cftime as cft

from toolkit import ChemicalData as cd
from toolkit import chemical_toolbox as ct
from np_data_list import *

"""GAUSS BASELINE DATA (no SAI)"""

# Change folder name based on data location
fold = '/Users/bibimboy/Documents/Data/Baseline'
# Specifies the time range for our data (2044 to 2064)
time = (360, 600)

# Baseline Scenario 01 2015-2064
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.001.cam.h0zm.'
fname2 = '.201501-206412.nc'
bl1_data = cd.ChemicalData(fold, fname, fname2)
bl1_data.narrowTimeRange(time)

# Baseline Scenario 02 2015-2064
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.002.cam.h0zm.'
fname2 = '.201501-206412.nc'
bl2_data = cd.ChemicalData(fold, fname, fname2)
bl2_data.narrowTimeRange(time)

time = (288, 528)
# Baseline Scenario 03 2020-2069 (Note that date trange is different from 01/02)
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.003.cam.h0zm.'
fname2 = '.202001-206912.nc'
bl3_data = cd.ChemicalData(fold, fname, fname2)
bl3_data.narrowTimeRange(time)

# average all baseline scenario data together
bl_data = ct.averageData((bl1_data, bl2_data, bl3_data))


"""SINGLE POINT INJECTION (SPI) DATA"""

time = (360, 600)
fold = '/Users/bibimboy/Documents/Data/SPI'

# Single Point Injection at 0N (12 Tg) 2044-2064
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.INJANN0N_12Tg.001.cam.h0zm.' 
fname2 = '.204412-206412.nc'
spi_0N_data = cd.ChemicalData(fold, fname, fname2)

# Single Point Injection at 15N (12 Tg) 2044-2064
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.INJANN15N_12Tg.001.cam.h0zm.' 
fname2 = '.204501-206412.nc'
spi_15N_data = cd.ChemicalData(fold, fname, fname2)

# Single Point Injection at 30N (12 Tg) 2044-2064 
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.INJANN30N_12Tg.001.cam.h0zm.' 
fname2 = '.204501-206412.nc'
spi_30N_data = cd.ChemicalData(fold, fname, fname2)

# Single Point Injection at 15S (12 Tg) 2044-2064
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.INJANN15S_12Tg.001.cam.h0zm.' 
fname2 = '.204501-206412.nc'
spi_15S_data = cd.ChemicalData(fold, fname, fname2)

# Single Point Injection at 30S (12 Tg) 2044-2064
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.INJANN30S_12Tg.001.cam.h0zm.' 
fname2 = '.204501-206412.nc'
spi_30S_data = cd.ChemicalData(fold, fname, fname2)


"""GAUSS SAI DATA"""

fold = '/Users/bibimboy/Documents/Data/SSP245-MA-GAUSS-DEFAULT/002'
# Time trange should be 2044 to 2064
time = (108, 348)

# SSP245 SAI 1.5 GAUSS 02 2035-2069
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.SSP245-MA-GAUSS-DEFAULT.002.cam.h0zm.'
fname2 = '.203501-206912.nc'
gauss02_15data = cd.ChemicalData(fold, fname, fname2)
gauss02_15data.narrowTimeRange(time)

fold = '/Users/bibimboy/Documents/Data/SSP245-MA-GAUSS-DEFAULT/003'

# SSP245 SAI 1.5 GAUSS 03 2035-2069
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.SSP245-MA-GAUSS-.DEFAULT.003.cam.h0zm.'
fname2 = '.203501-206912.nc'
gauss03_15data = cd.ChemicalData(fold, fname, fname2)
gauss03_15data.narrowTimeRange(time)


fold = '/Users/bibimboy/Documents/Data/SSP245-MA-GAUSS-LOWER-0.5/002'
# Time trange should be 2044 to 2064
time = (108, 348)

# SSP245 SAI 1.0 GAUSS 02 2035-2069
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.SSP245-MA-GAUSS-.LOWER-0.5.002.cam.h0zm.'
fname2 = '.203501-206912.nc'
gauss02_10data = cd.ChemicalData(fold, fname, fname2)
gauss02_10data.narrowTimeRange(time)

fold = '/Users/bibimboy/Documents/Data/SSP245-MA-GAUSS-LOWER-0.5/003'

# SSP245 SAI 1.0 GAUSS 03 2035-2069
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.SSP245-MA-GAUSS-.LOWER-0.5.003.cam.h0zm.'
fname2 = '.203501-206912.nc'
gauss03_10data = cd.ChemicalData(fold, fname, fname2)
gauss03_10data.narrowTimeRange(time)


fold = '/Users/bibimboy/Documents/Data/SSP245-MA-GAUSS-LOWER-1.0/002'
# Time trange should be 2044 to 2064
time = (108, 348)

# SSP245 SAI 0.5 GAUSS 02 2035-2069
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.SSP245-MA-GAUSS-LOWER-1.0.002.cam.h0zm.'
fname2 = '.203501-207012.nc'
gauss02_05data = cd.ChemicalData(fold, fname, fname2)
gauss02_05data.narrowTimeRange(time)

fold = '/Users/bibimboy/Documents/Data/SSP245-MA-GAUSS-LOWER-1.0/003'

# SSP245 SAI 0.5 GAUSS 03 2035-2069
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.SSP245-MA-GAUSS-LOWER-1.0.003.cam.h0zm.'
fname2 = '.203501-207012.nc'
gauss03_05data = cd.ChemicalData(fold, fname, fname2)
gauss03_05data.narrowTimeRange(time)


# (128,160) trange is 30.63 N to 59.84 N
# (160, 191) trange is 59.84 N to 90 N
# (1, 33) trange is 90 S to 60 S probable
#trange = (160, 191)
#trange = (1, 33)
latrange = (128,160)
# average clox data between 30 N and 60 N
# scaled down by a magnitude of 5

# average all baseline data together
bl_clox = ct.averageLatitudeBand(bl_data, latrange, "OddOx_CLOxBROx_Loss")
bl_clox_t = np.average(bl_clox, axis=0)

# average all GAUSS data 
gauss_15data = ct.averageData((gauss02_15data, gauss03_15data))
# average by latitude band
gauss_15clox = ct.averageLatitudeBand(gauss_15data, latrange, "OddOx_CLOxBROx_Loss")
gauss_15clox_t = np.average(gauss_15clox, axis=0) 

gauss_10data = ct.averageData((gauss02_10data, gauss03_10data))
# average by latitude band
gauss_10clox = ct.averageLatitudeBand(gauss_10data, latrange, "OddOx_CLOxBROx_Loss")
gauss_10clox_t = np.average(gauss_10clox, axis=0) 

gauss_05data = ct.averageData((gauss02_05data, gauss03_05data))
# average by latitude band
gauss_05clox = ct.averageLatitudeBand(gauss_05data, latrange, "OddOx_CLOxBROx_Loss")
gauss_05clox_t = np.average(gauss_05clox, axis=0) 

# same thing for all SAI injections
spi_0N_clox = ct.averageLatitudeBand(spi_0N_data, latrange, "OddOx_CLOxBROx_Loss")
spi_0N_clox_t = np.average(spi_0N_clox, axis=0)

spi_15N_clox = ct.averageLatitudeBand(spi_15N_data, latrange, "OddOx_CLOxBROx_Loss")
spi_15N_clox_t = np.average(spi_15N_clox, axis=0)

spi_30N_clox = ct.averageLatitudeBand(spi_30N_data, latrange, "OddOx_CLOxBROx_Loss")
spi_30N_clox_t = np.average(spi_30N_clox, axis=0)

spi_15S_clox = ct.averageLatitudeBand(spi_15S_data, latrange, "OddOx_CLOxBROx_Loss")
spi_15S_clox_t = np.average(spi_15S_clox, axis=0)

spi_30S_clox = ct.averageLatitudeBand(spi_30S_data, latrange, "OddOx_CLOxBROx_Loss")
spi_30S_clox_t = np.average(spi_30S_clox, axis=0)

year_range = (2044, 2064)
lat_range = ("30N", "60N")

# ClOx Loss Rate Numpy Data Save Pathways
spi_30N_abs_PATH = np_data_dir + clox_loss_dir + f"SPI_30N_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"
spi_15N_abs_PATH = np_data_dir + clox_loss_dir + f"SPI_15N_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"
spi_0N_abs_PATH = np_data_dir + clox_loss_dir + f"SPI_0N_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"
spi_15S_abs_PATH = np_data_dir + clox_loss_dir + f"SPI_15S_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"
spi_30S_abs_PATH = np_data_dir + clox_loss_dir + f"SPI_30S_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"
bl_abs_PATH = np_data_dir + clox_loss_dir + f"Baseline_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"
gauss_15abs_PATH = np_data_dir + clox_loss_dir + f"SAI1.5_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"
gauss_10abs_PATH = np_data_dir + clox_loss_dir + f"SAI1.0_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"
gauss_05abs_PATH = np_data_dir + clox_loss_dir + f"SAI0.5_ClOx_Loss_{year_range[0]}-{year_range[1]}_{lat_range[0]}-{lat_range[1]}_ZM"

np.save(spi_30N_abs_PATH, spi_30N_clox_t)
np.save(spi_15N_abs_PATH, spi_15N_clox_t)
np.save(spi_0N_abs_PATH, spi_0N_clox_t)
np.save(spi_15S_abs_PATH, spi_15S_clox_t)
np.save(spi_30S_abs_PATH, spi_30S_clox_t)
np.save(bl_abs_PATH, bl_clox_t)
np.save(gauss_15abs_PATH, gauss_15clox_t)
np.save(gauss_10abs_PATH, gauss_10clox_t)
np.save(gauss_05abs_PATH, gauss_05clox_t)