#!/usr/bin/env python
"""
Renee Manzagol 

Will want a combined file with RA, DEC, AZ and the Earth Mag Data 
so that we can relate the magnetic field to the orientation of the rocket
"""

import pandas as pd


#loading and data
EarthMagdata = pd.read_csv('EarthMagdata.csv')


#below was for checking my column headers 
#print(list(EarthMagdata.columns.values))

time = EarthMagdata ['# Time']
North= EarthMagdata ['X (north)']
East= EarthMagdata ['Y (east)']
Down= EarthMagdata  ['Z (down)']


#reading in the pointing data 
pointing = pd.read_csv('36245estcoord.csv')
timepointing = pointing['time']
RApointing= pointing['RA']
DECpointing= pointing['DEC']
AZpointing= pointing ['AZ']

"""
There are different times between the RA, DEC, AZ and the EarthMagdata
The Magdata starts at 0.007499999999999990 and goes up by 0.01 second intervals
However, we have already applied the start time above for the plot  
The pointing data starts at 87.99 and goes up by 0.02 second intervals 
"""
decimals = 2    
EarthMagdata['# Time'] = EarthMagdata['# Time'].apply(lambda x: round(x, decimals))
                
#if want to check on decimal places and keep as a file
#will comment out for now but useful for testing
#outfile = 'CroppedEarthMagdata.csv'
#EarthMagdata.to_csv(outfile,index=False)

#finding the cos of the angle inbetween the zenith and the pointing direction
#zenith was found from using the average long and lat which was determined in STEP1, Directional Data Plots and Earth Mag Dataout 
RAzenith=301.0
DECzenith=32.0 

EarthMagdata.rename(columns={'# Time':'time'}, inplace=True)
#check changed the header name                                        
#print(list(EarthMagdata.columns.values))
#merging dataframes by matching the values times 
merged_df = pointing.merge(EarthMagdata, how = 'left', on = ['time'])
# new file with merged data 
outfile1 = 'PointingandEarthMagData.csv'
merged_df.to_csv(outfile1,index=False)

print('output file:', outfile1)




    
