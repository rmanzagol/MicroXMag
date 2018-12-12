#!/usr/bin/env python
"""
plot the Earth's magneitc field versus time, this is saying how the magnetic field changed with out lat, long, and alt. 
This is not yet with respect to our pointing. 


D: declination (+ve east) - 
I: inclination (+ve down) - 
H: horizontal intensity - 
X: north component - 
Y: east component - 
Z: vertical component (+ve down) -
F: total intensity unit: degree or nT
"""


import matplotlib.pyplot as plt
import pandas as pd


#set tmin and tmax for graph, 
#as it is set right not it is redundant to the range of the file 
# wanted to give option to crop to 110-441 seconds for uptime table range or for other desired range 
tmin=87.99 
tmax=441
#loading and data
EarthMagdata = pd.read_csv('EarthMagdata.csv')


#below was for checking my column headers 
#print(list(EarthMagdata.columns.values))

time = EarthMagdata ['# Time']
North= EarthMagdata ['X (north)']
East= EarthMagdata ['Y (east)']
Down= EarthMagdata  ['Z (down)']
Total= EarthMagdata['F(total)']

#plotting Magnetic Field North, East, Down  with reference to the Zenith 
fig = plt.figure(figsize=(20,10)) 

ax1 = fig.add_subplot(411, facecolor = 'w')
ax1.plot(time,North,'b',lw=1,ls='-',label='North')
ax1.set_title('Earth Magnetic Field at Location of Rocket')
ax1.set_ylabel('BNorth (nT)')
ax1.set_xlim(tmin, tmax)
ax1.legend()

ax2 = fig.add_subplot(412, facecolor = 'w')
ax2.plot(time, East,'r',lw=1,ls='-',label='East')
ax2.set_ylabel('BEast (nT)')
ax2.set_xlim(tmin, tmax)
ax2.legend()

ax3 = fig.add_subplot(413, facecolor = 'w')
ax3.plot(time, Down,'g',lw=1,ls='-',label='Down')
ax3.set_xlabel('Time (sec)')
ax3.set_ylabel('BDown (nT)')
ax3.set_xlim(tmin, tmax)
ax3.legend()

ax4 = fig.add_subplot(414, facecolor = 'w')
ax4.plot(time, Total,'y',lw=1,ls='-',label='Total')
ax4.set_xlabel('Time (sec)')
ax4.set_ylabel('Total (nT)')
ax4.set_xlim(tmin, tmax)
ax4.legend()

plt.savefig('EarthMagneticFieldnT.png')
plt.show()

"""
below is for plotting in Gauss units instead of nT
"""


NorthG= EarthMagdata ['X (north)']*0.00001
EastG= EarthMagdata ['Y (east)']*0.00001
DownG= EarthMagdata  ['Z (down)']*0.00001
TotalG= EarthMagdata['F(total)']*0.00001

#plotting Magnetic Field North, East, Down  with reference to the Zenith 
fig = plt.figure(figsize=(20,10)) 

ax1 = fig.add_subplot(411, facecolor = 'w')
ax1.plot(time,NorthG,'b',lw=1,ls='-',label='North')
ax1.set_title('Earth Magnetic Field at Location of Rocket')
ax1.set_ylabel('BNorth (G)')
ax1.set_xlim(tmin, tmax)
ax1.legend()

ax2 = fig.add_subplot(412, facecolor = 'w')
ax2.plot(time, EastG,'r',lw=1,ls='-',label='East')
ax2.set_ylabel('BEast (G)')
ax2.set_xlim(tmin, tmax)
ax2.legend()

ax3 = fig.add_subplot(413, facecolor = 'w')
ax3.plot(time, DownG,'g',lw=1,ls='-',label='Down')
ax3.set_xlabel('Time (sec)')
ax3.set_ylabel('BDown (G)')
ax3.set_xlim(tmin, tmax)
ax3.legend()

ax4 = fig.add_subplot(414, facecolor = 'w')
ax4.plot(time, TotalG,'y',lw=1,ls='-',label='Total')
ax4.set_xlabel('Time (sec)')
ax4.set_ylabel('Total (G)')
ax4.set_xlim(tmin, tmax)
ax4.legend()

plt.savefig('EarthMagneticFieldG.png')
plt.show()



    
