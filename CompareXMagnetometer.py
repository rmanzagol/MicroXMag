
#!/usr/bin/env python

# this is a start at finding the calibration for the magnetometer

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#loading and data
Magnetometerdata = pd.read_csv('MagData.csv')
XRocketMag=pd.read_csv('MagXRocket.csv')


XRocketMag.rename(columns={'# Time':' TimeZ'}, inplace=True)
                           
decimals = 2 
Magnetometerdata[' TimeZ'] = Magnetometerdata[' TimeZ'].apply(lambda x: round(x, decimals))
Magnetometerdata=Magnetometerdata[(Magnetometerdata[' TimeZ']>88.00)]


XRocketMag[' TimeZ'] = XRocketMag[' TimeZ'].apply(lambda x: round(x, decimals))

#merging dataframes by matching the values times 
#merged_df = XRocketMag.merge(Magnetometerdata, how = 'left', on = [' TimeZ'])
merged_df = Magnetometerdata.merge(XRocketMag, how = 'left', on = [' TimeZ'])
merged_df = merged_df.dropna()

# new file with merged data 
outfile1 = 'CompareXMagnetometer.csv'
merged_df.to_csv(outfile1,index=False)


XCOMPARE = pd.read_csv('CompareXMagnetometer.csv')
print(list(XCOMPARE.columns.values))

Xrocket=XCOMPARE['Gauss']
Xmagnet=XCOMPARE[' MagX']


plt.figure(figsize=(10,10))
plt.scatter(Xrocket, Xmagnet, color='b')
plt.xlabel('X Field (G)')
plt.ylabel('Magnetometer Reading (V)')
#Using np.unique(x) instead of x handles x where there are duplicate values.
plt.plot(np.unique(Xrocket), np.poly1d(np.polyfit(Xrocket, Xmagnet, 1))(np.unique(Xrocket)), label='best fit')
plt.legend()
plt.show()


