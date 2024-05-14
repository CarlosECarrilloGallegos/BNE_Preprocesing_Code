import pandas as pd
import numpy as np
import glob
import scipy
import datetime

time = ['2013','2014','2015','2016']

for j in time:
    
    csvs = sorted(glob.glob('/data0/shr/bne/data/pm25/base_models/daily/formatted/liu/' + j + '/' +j +'/*.csv'))
    liu_year = []
    
    
    k = 1
    for i in csvs:
        liu = pd.read_csv(i)
        liu_fin = liu.rename(columns={'Lat':'lat','Lon':'lon','PM25_Pred':'liu'})
        liu_fin['day'] = k
        #liu_fin[['lat','lon','day','liu']]
        k = k+1
        del(liu)

        liu_year.append(liu_fin)
    
    liu_full = pd.concat(liu_year)
    liu_full['date'] = pd.to_datetime(liu_full['day']-1, unit='D', origin=j)
    liu_full = liu_full[['lat','lon','date','liu']]
    
    liu_full.to_csv('/data0/shr/bne/data/pm25/base_models/daily/formatted/liu/liu_pm25_' + j + '_daily.csv', index=False)
