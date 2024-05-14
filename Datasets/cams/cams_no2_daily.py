import xarray as xr
import pandas as pd
import numpy as np
import glob
import scipy
import datetime
import gc

#CAMS

time = ['2003','2004','2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021']

cams = xr.open_dataset('/data0/shr/bne/data/raw/nox/cams/cams_daymean.nc')
for i in time:
    cams_slice = cams.sel(time=slice(i + '-01-01T10:00:00.000000000',i + '-12-31T10:00:00.000000000'))
    cams_df = cams_slice.to_dataframe()
    cams_df = cams_df.reset_index()
    cams_df = cams_df.drop('bnds',axis=1).drop('time_bnds',axis=1).rename(columns={'no2':'cams'})
    cams_df['cams'] = cams_df['cams']*((0.029/0.046)*(1e9))
    #remove unwanted column
    cams_df = cams_df[['latitude','longitude','time','cams']]
    #rename columns
    cams_df = cams_df.rename(columns = {'longitude':'lon','latitude':'lat','time':'date'})
    
    #Convert longitude
    cams_lon = (np.array(cams_df['lon']))
    j = 0
    for k in cams_lon:
        if k >= 180:
            cams_lon[j] = k - 360
        j+=1

    cams_df['lon'] = cams_lon

    cams_df['date'] = pd.to_datetime(cams_df['date']).dt.date
    
    cams_df = cams_df.drop_duplicates()
    
    cams_df.to_csv('/data0/shr/bne/data/nox/base_models/daily/formatted/cams/cams_no2_' + i + '_daily.csv',index=False)
