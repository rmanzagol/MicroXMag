#!/usr/bin/env python

"""
Plot uptime (SQUID locked) data
Please note that the data starts at 111 seconds which corresponds to the gate valve opening 

@author: reneemanzagol
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data1 = pd.read_csv('fixedUptimeTable.csv')
data2= pd.read_csv('UptimeTable.csv')

#to get the column headers 
pixels=list(data1.columns.values)
#print(pixels)   

time=data2['Time']
# set time we would like to plot for 
tmin=110
tmax=439


plt.figure(figsize=(20,10))
for i, pixel in enumerate(pixels):
    times=data1[pixel]
    pixel_id=i*np.ones(times.shape)
    
    #Column A is black 
    if pixel in ['XA01','XA05','YA00','YA03','YA07']:
        colordot='black'
    #Column B is green
    if pixel in ['XB01','XB04','XB05','XB07','XB08','XB09','XB10','YB00','YB01','YB04','YB07','YB09' ,'YB10']:
        colordot='green'
    #Column C is blue
    if pixel in [ 'XC00','XC01','XC02','XC04','XC05','XC06','XC07','XC08','XC09','XC10','XC11','YC00','YC01','YC02','YC03','YC04','YC06','YC08','YC09','YC10','YC11']:
       colordot='blue'
    #Column D is red
    if pixel in ['XD04','XD05','XD06','XD07','XD08','XD09','XD10','YD03','YD06','YD07','YD08','YD09','YD10','YD11','YD12']:
        colordot='red'
    plt.scatter(times, pixel_id, color=colordot)
 
#time we would like to plot for
plt.xlim(tmin,tmax)
plt.xlabel('Time [s]')
plt.ylabel('Pixel ID code')
#below puts the pixel labels in, instead of having to use the ID codes. 
plt.yticks(np.arange(54), pixels)
plt.title('Pixel Uptime')

"""
#prints out Pixel ID Code List, in case you rather the graph NOT have the pixel labels and just show number in list 
print('Pixel ID')
for i in range(len(pixels)):
    print(i, pixels[i])
"""

figurename = 'SQUIDUptime.pdf'
plt.savefig(figurename)

