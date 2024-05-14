import xarray as xr
import pandas as pd
import numpy as np
import glob
import scipy
import datetime
import gc

#OMI
print('prepping omi')   
time = ['2010',
        '2011','2012','2013','2014','2015'] #'2009','2017','2018','2019','2020' to be done later

for i in time:
    filelist = sorted(glob.glob('/data0/shr/bne/data/raw/nox/omi/Daily/' +i + '/*.h5'))
    omi_v4 = xr.open_mfdataset(filelist, concat_dim = 'None', combine = 'nested',phony_dims='sort')
    omi_v4_df = omi_v4.to_dataframe()
    gc.collect()
    omi_v4_df_conus = omi_v4_df.query('Latitude >24 and Latitude <50 and Longitude > -125 and Longitude < -66')
    omi_v4_df_conus = omi_v4_df_conus.reset_index()
    omi_v4_df_conus = omi_v4_df_conus.drop('GMI_SurfNO2',axis=1).drop('GMI_SurfNO2_2pm',axis=1).drop('phony_dim_0',axis=1).drop('phony_dim_1',axis=1).drop('OMI_SurfNO2_2pm',axis=1).rename(columns={'OMI_SurfNO2':'pred_OMIv4', 'None':'date'})
    omi_v4_df_conus = omi_v4_df_conus.rename(columns={'Latitude':'lat','Longitude':'lon','pred_OMIv4':'omi'})
    omi_v4_df_conus = omi_v4_df_conus[['lat','lon','date','omi']]
    omi_v4_df_conus['date'] = pd.to_datetime((omi_v4_df_conus['date']), unit='D', origin=i)
    omi_v4_df_conus.to_csv('/data0/shr/bne/data/raw/nox/omi/omi_no2_'+i+'_daily.csv',index=False)
    

