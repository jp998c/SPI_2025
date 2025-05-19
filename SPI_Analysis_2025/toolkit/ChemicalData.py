import xarray as xr
import numpy as np
import pandas as pd
import os

"""
ChemicalData is an object that stores data taken from the CESM models 
"""
class ChemicalData:
    def __init__(self, path, fname1, fname2):

        # Lists all potential species data to look for. 
        # This SHOULD be modular so if you need something else just add additional species of interest to the array and it should still work.
        self.type_str = ["HOX", "NOX", "OddOx_HOx_Loss", "OddOx_NOx_Loss", "OddOx_Ox_Loss", "OddOx_CLOxBROx_Loss", "CLONO2", "CLOX", "CLOY", "HCL", "H2O", "SAD_AERO", "O3"] 

        # OVERRIDE: in case a ChemicalData object needs to be made without an attached file. All parameters should be filled with None.
        if(path == None and fname1 == None and fname2 == None):
            self.path = ''
            self.fname1 = ''
            self.fname2 = ''
            
            self.lat = []
            self.lev =[]
            self.time = []

            self.type_available = []
            for str in self.type_str:
                self.type_available.append(False)

            self.data = {}
            
        else:
            # path is the directory in which to look for the file
            self.path = path

            # fname1 is the file name prefix, fname 2 is the file name suffix
            self.fname1 = fname1
            self.fname2 = fname2

            # Not sure if I should have individual lat/lev stored for each type. Probably unnecessary but idk
            self.lat = []
            self.lev =[]
            
            self.type_available = []
            self.time = []

            # self.data stores the actual data. Set as a dictionary to facilitate the retrieval of data
            self.data = {}

            # Goes through all strings in self.type_str and checks for data files of type in the directory self.path. 
            # If the file exists, uploaded the relevant type data and mark that the type of data is available in self.type_available
            for sp in self.type_str:
                full_dir = f"{self.path}/{self.fname1}{sp}{self.fname2}"

                if(os.path.exists(full_dir)):
                    #print(f"File Exists: {full_dir}")
                    data_temp = xr.open_dataset(full_dir)
                    self.lat = data_temp.lat
                    self.lev = data_temp.lev
                    self.time = data_temp.time
                    
                    self.data[sp] = data_temp[sp]
                    self.type_available.append(True)
                else:
                    #print(f"File Does Not Exist: {full_dir}")
                    self.type_available.append(False)

            # If the length of self.type_str does not match self.type_available, data read has somehow gone wrong.
            # Maybe there's a better way to do this
            if(len(self.type_str) != len(self.type_available)):
                print(f"type_str: {len(self.type_str)}")
                print(f"type_available:{len(self.type_available)}")
                raise ValueError("Error reading file! type_str and type_available do not match up")
            #self.printTypeAvailable()


    # Searches the object's self.type_str array and returns the index value at which the specified type string is found.
    # If none is found, returns -1
    def typeIndex(self, species):
        index = 0
        for sp in self.type_str:
            if(sp == species):
                return index
            index = index + 1
        return -1
    
    # Determines if the object contains data of the specified type string and returns True if the data is available (according to self.type_available) and False otherwise.
    def isTypeAvailable(self, species):
        index = self.typeIndex(species)
        return self.type_available[index]
    
    def printTypeAvailable(self):
        print(f"For {self.fname1}____{self.fname2}")
        print("The following data types are available:")
        for type in self.data:
            print (type)

    # Returns the data for a specified species if available. If the data is not available, then an error is thrown
    def getTypeData(self, species):
        if(self.isTypeAvailable(species)):
            return self.data[species]
        else:
            raise ValueError(f"No data for type {species} is available!")

    # Updates data for a given species with the specified new data
    def updateData(self, species, newdata):
        self.data[species] = newdata

    # Returns a new ChemicalData object with the same data file, but shortened to a specified time trange
    # trange is a tuple two values, start and end
    def narrowTimeRange(self, trange):
        rangeData = ChemicalData(None, None, None)

        # Sets all variables of rangeData to that of the original object
        rangeData.path = self.path
        rangeData.fname1 = self.fname1
        rangeData.fname2 = self.fname2
            
        rangeData.lat = self.lat
        rangeData.lev = self.lev
        rangeData.time = self.time[trange[0]:trange[1]]

        rangeData.type_available = self.type_available
        rangeData.data = self.data

        # Goes through the data and shortens the time trange
        for sp in rangeData.data:
            temp_data = rangeData.data[sp]
            rangeData.data[sp] = temp_data[trange[0]:trange[1], :, :]

        return rangeData

    def getYearRange(self):
        start = self.time[0]
        end = self.time[len(self.time) - 1]
        return (start, end)
    
    def getYearRangeStr(self):
        start = str(self.time[0])
        end = str(self.time[len(self.time) - 1])
        return (start, end)

        
    

