
#!/usr/bin/env python

"""
Plot Magnetometer data from Magdata.csv
Set tmin and tmax below 

@author: reneemanzagol
"""
import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('Magdata.csv')

#set how long you want to plot 
#I have set it here to match the ASC data 
tmin=87.99 
tmax=441

#below was for checking my column headers to pull correct data
#print(list(data.columns.values))

timeZ = data[' TimeZ']
MagZ= data[' MagZ']
timeY= data[' TimeY']
MagY= data[' MagY']
timeX= data [' TimeX']
MagX= data [' MagX']
#until we determine the gain the tot mag is not that insightful but still worth plotting for now 
TotMag= (((MagZ)**2+(MagY)**2+(MagX)**2))**0.5


fig = plt.figure(figsize=(20,10))

ax1 = fig.add_subplot(411, facecolor = 'w')
ax1.plot(timeZ,MagZ,'b',lw=1,ls='-',label='MagZ')
ax1.set_title('Magnetometers')
ax1.set_ylabel('MagZ')
ax1.set_xlim(tmin, tmax)
ax1.legend()

ax2 = fig.add_subplot(412, facecolor = 'w')
ax2.plot(timeY,MagY,'r',lw=1,ls='-',label='MagY')
ax2.set_ylabel('MagY')
ax2.set_xlim(tmin, tmax)
ax2.legend()

ax3 = fig.add_subplot(413, facecolor = 'w')
ax3.plot(timeX,MagX,'g',lw=1,ls='-',label='MagX')
ax3.set_xlabel('Time (sec)')
ax3.set_ylabel('MagX')
ax3.set_xlim(tmin, tmax)
ax3.legend()

ax4 = fig.add_subplot(414, facecolor = 'w')
ax4.plot(timeZ,TotMag,'y',lw=1,ls='-',label='TotMag')
ax4.set_xlabel('Time (sec)')
ax4.set_ylabel('TotMag')
ax4.set_xlim(tmin, tmax)
ax4.legend()

figurename = 'MagDataPlot.pdf'
plt.savefig(figurename)
plt.show()



