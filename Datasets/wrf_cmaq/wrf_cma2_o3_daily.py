import xarray as xr
import pandas as pd
import numpy as np
import glob
import scipy
import datetime

    
#wrf_cmaq
time = ['2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2015','2016','2017','2018']

for i in time:
    filelist = sorted(glob.glob('/data0/shr/bne/data/raw/multi/wrf_cmaq/*' + i + '*MDA8_O3*.nc'))
    wrf_cmaq = xr.open_mfdataset(filelist, concat_dim = 'None', combine = 'nested')
    wrf_df = wrf_cmaq.to_dataframe()
    
    wrf_df = wrf_df.reset_index()
    wrf_df = wrf_df.drop('None',axis=1).drop('Time',axis=1).drop('south_north',axis=1).drop('west_east',axis=1).rename(columns={'MDA8_O3_daily':'pred_WRF-CMAQ'})
    #reorganize
    wrf = wrf_df[['latitude','longitude','time','pred_WRF-CMAQ']]
    wrf = wrf.rename(columns={'time':'date','pred_WRF-CMAQ':'wrf_cmaq','longitude':'lon','latitude':'lat'})
    wrf['date'] = wrf['date'].astype(str).str.replace('b','').replace('\'','')
    wrf['date'] = pd.to_datetime(wrf['date'])
    
    wrf.to_csv('/data0/shr/bne/data/o3/base_models/daily/formatted/wrf_cmaq/wrf_cmaq_o3_'+i+'_daily_mda8.csv',index=False)
