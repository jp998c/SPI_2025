import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cftime as cft

from toolkit import ChemicalData as cd
from toolkit import chemical_toolbox as ct
from np_data_list import *

""" ONLY RUN THIS FILE IF CESM_lat.npy OR CESM_lev.npy ARE MISSING """

# Change folder name based on data location
fold = '/Users/bibimboy/Documents/Data/Chemical_zm'

# Baseline Scenario 01 2015-2064
fname = 'b.e21.BWSSP245.f09_g17.release-cesm2.1.3.WACCM-MA-1deg.001.cam.h0zm.'
fname2 = '.201501-206412.nc'
bl1_data = cd.ChemicalData(fold, fname, fname2)

lat_PATH = np_data_directory + "CESM_lat"
lev_PATH = np_data_directory + "CESM_lev"

np.save(lat_PATH, bl1_data.lat)
np.save(lev_PATH, bl1_data.lev)