
#!/usr/bin/env python

"""
Plot ACS data (pointing data) from file 36245estcoord.csv 
Plot Location data from file 'postZero36.245original.csv'
@author: reneemanzagol
"""

import matplotlib.pyplot as plt
import pandas as pd


def minmax(val_list):
    min_val = min(val_list)
    max_val = max(val_list)

    return (min_val, max_val)

"""
Plotting ACS data (pointing data)

"""

#read in file 
datapanda = pd.read_csv('36245estcoord.csv')

#below was for checking my column headers 
#print(list(datapanda.columns.values))

timepanda = datapanda['time']
RApanda= datapanda['RA']
DECpanda= datapanda['DEC']
AZpanda= datapanda ['AZ']

#used for axis for plots and for croppping the other data
mintime, maxtime= minmax(timepanda)

fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(311, facecolor = 'w')
ax1.plot(timepanda,RApanda,'b',lw=1,ls='-',label='RA')
ax1.set_title('Pointing Data (RA, DEC, AZ)')
ax1.set_ylabel('RA (deg)')
ax1.set_xlim(mintime, maxtime)
ax1.legend()

ax2 = fig.add_subplot(312, facecolor = 'w')
ax2.plot(timepanda,DECpanda,'r',lw=1,ls='-',label='DEC')
ax2.set_ylabel('DEC (deg)')
ax2.set_xlim(mintime, maxtime)
ax2.legend()

ax3 = fig.add_subplot(313, facecolor = 'w')
ax3.plot(timepanda,AZpanda,'g',lw=1,ls='-',label='AZ')
ax3.set_xlabel('Time (sec)')
ax3.set_ylabel('AZ (deg)')
ax3.set_xlim(mintime, maxtime)
ax3.legend()


plt.savefig('Pointing Data.png')
plt.show()

"""
Below is for plotting the Long, Lat, Alt data, 
This is NOT pointing data but for the rocket's location
input file is postZero36.245original.cvs  

"""
#read in file 
Fulldata2 = pd.read_csv('postZero36.245original.csv')


#the locational data is for a much longer time frame than the pointing data, so will crop
data2=Fulldata2[(Fulldata2[' Time LO    ']<maxtime) & (Fulldata2[' Time LO    ']>mintime)]

#below was for checking my column headers names
#print(list(data2.columns.values))

time2 = data2[' Time LO    ']
Long= data2[' Longitude ']
Lat= data2[' Latitude  ']
Alt= data2 [' Altitude  ']


fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(311, facecolor = 'w')
ax1.plot(time2,Long,'b',lw=1,ls='-',label='Long (deg)')
ax1.set_title('Trajectory Data (Lat, Long, Alt)')
ax1.set_ylabel('Long (deg)')
ax1.set_xlim(mintime, maxtime)
ax1.legend()

ax2 = fig.add_subplot(312, facecolor = 'w')
ax2.plot(time2,Lat,'r',lw=1,ls='-',label='Lat (deg)')
ax2.set_ylabel('Lat (deg)')
ax2.set_xlim(mintime, maxtime)
ax2.legend()

ax3 = fig.add_subplot(313, facecolor = 'w')
ax3.plot(time2,Alt,'g',lw=1,ls='-',label='Alt (ft)')
ax3.set_xlabel('Time (sec)')
ax3.set_ylabel('Alt (ft)')
ax3.set_xlim(mintime, maxtime)
ax3.legend()

plt.savefig('TrajectoryData.png')
plt.show()



#the below is to check that the long, late didn't change much  so that we can assume the zenith stays pretty much constant
print('For reference and for calculating the zenith')
print('Long Range', minmax(Long))
print('Lat Range', minmax(Lat)) 
print('Alt Range', minmax(Alt)) 
#the zenith for 32.4, -106.32 is RA: 20 h 04 m, DEC 32 degrees. 



