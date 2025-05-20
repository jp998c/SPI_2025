import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cftime as cft

from toolkit import ChemicalData as cd
from toolkit import chemical_toolbox as ct
from np_data_list import *

folder = '/Users/bibimboy/Documents/Data/Controller_Injections'
fname = 'Controller_start_DefaultMA_001.txt'
path = f"{folder}/{fname}"

d1_inj_30N = np.array([], dtype="float")
d1_inj_15N = np.array([], dtype="float")
d1_inj_15S = np.array([], dtype="float")
d1_inj_30S = np.array([], dtype="float")
d1_year = np.array([], dtype="int")

with open(path) as f:
    for line in f:
        line = line.replace("\n", "")
        data = line.split(" ")
        length = len(data)
        #print(data[(length-4):length])
        if(not (data[0] == 'Timestamp')):
            d1_year = np.append(d1_year, int(data[0]))
            d1_inj_30S = np.append(d1_inj_30S, float(data[length-4]))
            d1_inj_15S = np.append(d1_inj_15S, float(data[length-3]))
            d1_inj_15N = np.append(d1_inj_15N, float(data[length-2]))
            d1_inj_30N = np.append(d1_inj_30N, float(data[length-1]))


folder = '/Users/bibimboy/Documents/Data/Controller_Injections'
fname = 'Controller_start_Lower-0.5-MA_002.txt'
path = f"{folder}/{fname}"

l05_inj_30N = np.array([], dtype="float")
l05_inj_15N = np.array([], dtype="float")
l05_inj_15S = np.array([], dtype="float")
l05_inj_30S = np.array([], dtype="float")
l05_year = np.array([], dtype="int")

with open(path) as f:
    for line in f:
        line = line.replace("\n", "")
        data = line.split(" ")
        length = len(data)
        #print(data[(length-4):length])
        if(not (data[0] == 'Timestamp')):
            l05_year = np.append(l05_year, int(data[0]))
            l05_inj_30S = np.append(l05_inj_30S, float(data[length-4]))
            l05_inj_15S = np.append(l05_inj_15S, float(data[length-3]))
            l05_inj_15N = np.append(l05_inj_15N, float(data[length-2]))
            l05_inj_30N = np.append(l05_inj_30N, float(data[length-1]))


folder = '/Users/bibimboy/Documents/Data/Controller_Injections'
fname = 'Controller_start_Lower-1.0-MA_002.txt'
path = f"{folder}/{fname}"

l10_inj_30N = np.array([], dtype="float")
l10_inj_15N = np.array([], dtype="float")
l10_inj_15S = np.array([], dtype="float")
l10_inj_30S = np.array([], dtype="float")
l10_year = np.array([], dtype="int")

with open(path) as f:
    for line in f:
        line = line.replace("\n", "")
        data = line.split(" ")
        length = len(data)
        #print(data[(length-4):length])
        if(not (data[0] == 'Timestamp')):
            l10_year = np.append(l10_year, int(data[0]))
            l10_inj_30S = np.append(l10_inj_30S, float(data[length-4]))
            l10_inj_15S = np.append(l10_inj_15S, float(data[length-3]))
            l10_inj_15N = np.append(l10_inj_15N, float(data[length-2]))
            l10_inj_30N = np.append(l10_inj_30N, float(data[length-1]))

print(l10_year)
print(d1_inj_15N)

spi_30N_color = "#ED1717"
spi_15N_color = "#F24D11"
spi_0N_color = "#F6830C"
spi_15S_color = "#FBB806"
spi_30S_color = "#FFEE00"
spi_width = 3

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(10,4))
fig.suptitle(f"Controller Injections for Controller Runs")
ax1.set_xlabel("Year")
ax1.set_ylabel("Injection Amount (Tg)")
ax1.set_title("SAI 1.5")

l0, = ax1.plot(d1_year, d1_inj_30N, label='30 N', color=spi_30N_color, linewidth=spi_width)
l1, = ax1.plot(d1_year, d1_inj_15N, label='15 N', color=spi_15N_color, linewidth=spi_width)
l2, = ax1.plot(d1_year, d1_inj_15S, label='15 S', color=spi_15S_color, linewidth=spi_width)
l3, = ax1.plot(d1_year, d1_inj_30S, label='30 S', color=spi_30S_color, linewidth=spi_width)

l0, = ax2.plot(l05_year, l05_inj_30N, label='30 N', color=spi_30N_color, linewidth=spi_width)
l1, = ax2.plot(l05_year, l05_inj_15N, label='15 N', color=spi_15N_color, linewidth=spi_width)
l2, = ax2.plot(l05_year, l05_inj_15S, label='15 S', color=spi_15S_color, linewidth=spi_width)
l3, = ax2.plot(l05_year, l05_inj_30S, label='30 S', color=spi_30S_color, linewidth=spi_width)

l0, = ax3.plot(l10_year, l10_inj_30N, label='30 N', color=spi_30N_color, linewidth=spi_width)
l1, = ax3.plot(l10_year, l10_inj_15N, label='15 N', color=spi_15N_color, linewidth=spi_width)
l2, = ax3.plot(l10_year, l10_inj_15S, label='15 S', color=spi_15S_color, linewidth=spi_width)
l3, = ax3.plot(l10_year, l10_inj_30S, label='30 S', color=spi_30S_color, linewidth=spi_width)

ax1.set_xlabel("Year")
ax1.set_title("SAI 1.5")
ax2.set_xlabel("Year")
ax2.set_title("SAI 1.0")
ax3.set_xlabel("Year")
ax3.set_title("SAI 0.5")

fig.legend(handles=[l0, l1, l2, l3], loc='outside right')

fig.savefig(img_dir + 'controller_inj.png', dpi=300)
plt.show()