
#!/usr/bin/env python
"""
The original file is a table of pixels and seconds. 
There is a 1 for each second that a pixel is on and is blank otherwise
In order to plot the uptime of the squids as a scatter plot, 
one method was to change each 1 to the corresponding seconds value

@author: reneemanzagol
"""

import pandas as pd


data2= pd.read_csv('UptimeTable.csv')
data1=data2.iloc[:, 1:]
time=data2['Time']

#to get the column headers 
pixels=list(data1.columns.values)
print(pixels)

for i, pixel in enumerate(pixels):
        data1[pixel].fillna('0',inplace=True)
        data1[pixel].loc[data2[pixel] == 1] = data2['Time']

outfile = 'fixedUptimeTable.csv'
data1.to_csv(outfile,index=False)

