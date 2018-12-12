Author:
Renee Manzagol
Earth 361 Project
December 11, 2018 

Project is for plotting pixel update, magnetometer data, calculating and plotting Earth's magnetic field data in rocket coordinates. Please see documentation folder for more information. 

Starting files:
36245estcoord.csv
Postzero36.245original.csv
UptimeTable.csv
MagData.csv

Prerequisites:
Package pyIGRF will need to be installed: 
https://pypi.org/project/pyIGRF/
Download the files (they are also in this folder) 
>python setup.py install


If starting from the four initial files, please run in this order:
Please also see the process flow diagram in the documentation folder 

For Magnetometer plots
PlotMagnetometerdata.py

For Squid Uptime Graph:
1) ConvertUptimeTableForScatter.py
2) SquidLockGraph.py

Direction Data Plots (and lat/long/alt range):
DirectionalDataPlots.py 

Magnetic Field 
1)EarthMagData.py
(Optional, if want plots) MagEastNorthDownPlots.py 
2) PointingandMagData.py
3) MagneticFieldRocket.py

Calibration Graph:
CompareXMagnetometer.py 


This folder contains additional folders:
1) Documentation- see project report and flow diagram 
2) Previous version code
3) Extra TDAS Data (this has original source code for TDAS and python script to plot with Renee's snippet of code added 
4) RollPitchYaw- data and script to plot the rotational data 
5) pyIGRF-0.1.8 2- Package to be installed 