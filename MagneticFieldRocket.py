#!/usr/bin/env python

import math
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

CombinedMagdata = pd.read_csv('PointingandEarthMagData.csv')

time = CombinedMagdata ['time']
North= CombinedMagdata ['X (north)']
East= CombinedMagdata ['Y (east)']
Down= CombinedMagdata  ['Z (down)']
RApointing= CombinedMagdata['RA']
DECpointing= CombinedMagdata['DEC']
AZpointing= CombinedMagdata ['AZ']

#finding the cos of the angle inbetween the zenith and the pointing direction
#zenith was found from using the average long and lat which was determined in STEP1, Directional Data Plots and Earth Mag Dataout 
RAzenith=301.0
DECzenith=32.0 


costheta=np.sin(np.radians(DECzenith))*np.sin(np.radians(DECpointing))+np.cos(np.radians(DECzenith))*np.cos(np.radians(DECpointing))*np.cos(np.radians(RApointing-RAzenith))


MagXRocket=np.empty((len(time),3))
for i in range(len(time)):
    #if want to calculate costheta in the loop, checked both ways, get same answer, question of efficiecy 
    #costheta=math.sin(math.radians(DECzenith))*math.sin(math.radians(DECpointing[i]))+math.cos(math.radians(DECzenith))*math.cos(math.radians(DECpointing[i]))*math.cos(math.radians(RApointing[i]-RAzenith))
    Bx=-Down[i]*costheta[i]+North[i]*math.cos(math.radians(AZpointing[i]))+East[i]*math.sin(math.radians(AZpointing[i]))
    MagXRocket[i,0]=time[i]
    # - sign to get it to point in the direction of the rocket nose versus pointing direction 
    MagXRocket[i,1]=-Bx
    #and convert to guass
    MagXRocket[i,2]=-Bx*0.00001
    


fig = plt.figure(figsize=(20,5)) 

#doing subplots so can eventaully add By and Bz
ax1 = fig.add_subplot(111, facecolor = 'w')
ax1.plot(MagXRocket[:,0],MagXRocket[:,1],'g',lw=1,ls='-',label='Bx')
ax1.set_title('Magnetic Field with respect to Rocket')
ax1.set_ylabel('Bx (nT)')
ax1.set_xlabel('Time (sec)')
ax1.set_xlim(min(time), max(time))
ax1.legend()

#doing subplots so can eventaully adding By and Bz
#below is calculating in Gauss units 
fig = plt.figure(figsize=(20,5)) 

ax1 = fig.add_subplot(111, facecolor = 'w')
ax1.plot(MagXRocket[:,0],MagXRocket[:,2],'g',lw=1,ls='-',label='Bx')
ax1.set_title('Magnetic Field with respect to Rocket')
ax1.set_ylabel('Bx (Gauss)')
ax1.set_xlabel('Time (sec)')
ax1.set_xlim(min(time), max(time))
ax1.legend()

fig.savefig('MagneticFieldRocket.png', transparent=True)
plt.show()

np.savetxt('MagXRocket.csv', MagXRocket, delimiter=', ', header='Time,nT,Gauss')
