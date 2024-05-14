import numpy as np
import pandas as pd

#load data
omi = pd.read_csv('/data0/shr/bne/data/raw/nox/omi/omi_no2_2010_daily.csv') #or the appropriate year

#replace fill values with nans
omi['omi'][(omi['omi'] < 1e-20)] = np.nan

omi_points = omi.groupby(['lat','lon']).aggregate('count').reset_index()

omi_final = []
for i in np.arange(0,len(omi_points['lat']),1):
    omi_now = omi[(omi['lat'] == omi_points['lat'][i]) & (omi['lon']==omi_points['lon'][i])]
    omi_filled = pd.concat([omi_now.ffill(),omi_now.bfill()]).groupby(['date']).mean().reset_index()[['lat','lon','date','omi']]
    omi_final.append(omi_filled)

omi_final_df = pd.concat(omi_final)
omi_final_df = omi_final_df.sort_values(by=['date'])
    
omi_final_df.to_csv('/data0/shr/bne/data/nox/base_models/daily/formatted/omi/omi_no2_2010_daily.csv',index=False)
