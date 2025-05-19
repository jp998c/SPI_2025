import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

from toolkit import ChemicalData as cd

"""
Created on Tues Feb 4

@author: jp998
"""

# The functions in this file are generally used for manipulating ChemicalData objects.

# Takes in a tuple of ChemicalData objects and averages all species data of the same type with each other. Objects' lat/lev/time must match. 
# Returns a new ChemicalData object containing the averaged data.
def averageData(data_tuple):
    tup_len = len(data_tuple)
    if(tup_len > 1):
        
        # We go through all species types as specified in ChemicalData
        chem_type = data_tuple[0].type_str
        
        # We initialize an empty ChemicalData object to store the averaged data
        avg_data = cd.ChemicalData(None, None, None)
        avg_data.lat = data_tuple[0].lat
        avg_data.lev = data_tuple[0].lev
        avg_data.time = data_tuple[0].time
        
        for ct in chem_type:
            count = 0
            temp_averages = np.zeros((240, 70, 192))
            for cdata in data_tuple:
                # We check if the data type is available for each cdata instance and if it is, add it to temp_averages and increment count by 1.
                # Also sets type_available for that data type to True in avg_data
                if(cdata.isTypeAvailable(ct)):
                    count = count + 1
                    temp_averages = temp_averages + cdata.getTypeData(ct)
                    avg_data.type_available[cdata.typeIndex(ct)] = True
            if(count > 0):
                temp_averages = temp_averages / count
                avg_data.updateData(ct, temp_averages)
        
        return avg_data

    else:
        raise ValueError("Please specify a tuple with 2 or more objects!")

    return 0

# Takes a ChemicalData object and averages across a specified time range (provided as a tuple) for all species.
# Returns a ChemicalData object conaining the averaged data. 
def dataTimeRange(cdata, range, species):
    temp_data = cd.ChemicalData(None, None, None)
    for sp in cdata:
        if(cdata.isTypeAvailable(sp)):
            temp_data = cdata.data[sp]
            time_avg = np.mean(temp_data[range[0]:range[1], :, :], axis=0)
    
    return time_avg

# Takes a ChemicalData object and averages across a specified time range (provided as a tuple) for a given species.
# Returns an array containing the averaged data. 
def averageOverTime(cdata, range, species):
    chem_type = cdata.type_str

    if(cdata.isTypeAvailable(species)):
        temp_data = cdata.data[species]
        time_avg = np.mean(temp_data[range[0]:range[1], :, :], axis=0)
    
    return time_avg

# Get latitude from index
def getLatitudeFromIndex(index, cdata):
    latitude = cdata.lat
    return latitude[index]

# Takes a ChemicalData object and averages across a specified latitude range (provided as a tuple) for a given species.
# Returns an array containing the average data (or, if the data type is not available, return an empty array).
def averageLatitudeBand(cdata, range, species):

    if(cdata.isTypeAvailable(species)):
        temp_data = cdata.data[species]
        # Obtain all latitude data and convert into radians
        lat_rad = (temp_data.lat[range[0]:range[1]] * np.pi) / 180
        # calculate the latitude weight (just the cosine of the latitude)
        weight = np.absolute(np.cos(lat_rad))
        # sum up the weighted latitude bands of interest and then divide by the weight count
        lat_avg = np.sum(temp_data[ :, :, range[0]:range[1]] * weight, axis=2) / np.sum(weight, axis=0)
        return lat_avg
    
    else:
        return []


# Takes a pre-time averaged array and averages across a specified seasonal range (provided as a tuple) for a given species over a given time range.
# Returns an array containing the average data. 
# i'm still working on this one ok
def averageOverSeason(carray, season_range, reshape_param):

    years = reshape_param[0]
    months = reshape_param[1]
    levels = reshape_param[2]
    lat = reshape_param[3]

    # Defines the range of months that we are interested in.
    season = slice(season_range[0], season_range[1])

    temp_data = carray
    #print(temp_data)
    # Reshape the data array into twelve month segments so that we can isolate specific months of interest.
    # This kinda assumes that the time range always start with January, which is not the case. Might try to change in the future
    temp_reshape = temp_data.values.reshape(years, months, levels, lat)
    # Isolate the months of interest 
    temp_season = temp_reshape[:, season, :]
    temp_season = temp_season.mean(axis = (0,1))

        #cloxbrox_15_s = cloxbrox_15.values.reshape(20, 12, 70)
        #cloxbrox_15_s = xr.DataArray(cloxbrox_15_s)
        #cloxbrox_15_s = cloxbrox_15_s[:, season, :]
        #cloxbrox_15_s = cloxbrox_15_s.mean(axis = (0,1))
    return temp_season