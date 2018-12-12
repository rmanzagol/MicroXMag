#!/usr/bin/env python
"""

Location data from file 'postZero36.245original.csv'

This script was originally put with the directional data plots but was split 

To get the magnetic field data, we will use the position of where it was 
Use pyIGRF, this is a package of IGRF-12 (Internation Geomagnetic Reference Field)
pyIGRF will need to be installed 


To calculate magnetic field intensity
pyIGRF.igrf_value(lat, lon, alt, date)
pyIGRF.igrf_variation(lat, lon, alt, date)

There was NOT documentation for altitude input 
after comparring a few points with the official online calculator 
input for altitude needs ot be in km not ft. 


Output of pyIGRF is in the format:
D: declination (+ve east) - 
I: inclination (+ve down) - 
H: horizontal intensity - 
X: north component - 
Y: east component - 
Z: vertical component (+ve down) -
F: total intensity 
unit: degree or nT
  

@author: reneemanzagol
"""

import pandas as pd
import numpy as np

import pyIGRF


def minmax(val_list):
    min_val = min(val_list)
    max_val = max(val_list)

    return (min_val, max_val)


#read in file 
Fulldata2 = pd.read_csv('postZero36.245original.csv')



#the locational data is for a much longer time frame than the pointing data, so will crop 
datapointing = pd.read_csv('36245estcoord.csv')
timepointing = datapointing['time']
mintime, maxtime= minmax(timepointing)

#the locational data is for a much longer time frame than the pointing data, so will crop
data2=Fulldata2[(Fulldata2[' Time LO    ']<maxtime) & (Fulldata2[' Time LO    ']>mintime)]

#below was for checking my column headers names
#print(list(data2.columns.values))

time2 = data2[' Time LO    ']
Long= data2[' Longitude ']
Lat= data2[' Latitude  ']
Alt= data2 [' Altitude  ']


#convert ft to km 
Altkm= Alt*0.0003048


EarthMagData=np.empty((len(time2),8))
for i in range(len(time2)):
    A=pyIGRF.igrf_value(Lat.iloc[i],Long.iloc[i],Altkm.iloc[i],2018)
    EarthMagData[i,0]=time2.iloc[i]
    EarthMagData[i,1]=A[0]
    EarthMagData[i,2]=A[1]
    EarthMagData[i,3]=A[2]
    EarthMagData[i,4]=A[3]
    EarthMagData[i,5]=A[4]
    EarthMagData[i,6]=A[5]
    EarthMagData[i,7]=A[6]
    
    
#saving magnetic field data and time 
np.savetxt('EarthMagdata.csv', EarthMagData, delimiter=', ', header='Time,D(east),I(down), H,X (north),Y (east),Z (down),F(total)')

print('output file: EarthMagdata.csv')









