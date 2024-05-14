## Demonstrateds for 2013; other years in: /data0/shr/bne/data/pm25/base_models/daily/formatted/liu/Liu_Missing_data_check.py

import pandas as pd
import numpy as np
import geopandas
import math

liu_2013 = pd.read_csv('liu_pm25_2013_daily.csv')

liu_2013_count = liu_2013.groupby(['date']).aggregate('count').reset_index()

liu_10_10 = liu_2013[liu_2013['date']=='2013-10-10']
liu_10_09 = liu_2013[liu_2013['date']=='2013-10-09']
liu_10_11 = liu_2013[liu_2013['date']=='2013-10-11']
liu_12_22 = liu_2013[liu_2013['date']=='2013-12-22']
liu_12_21 = liu_2013[liu_2013['date']=='2013-12-21']
liu_12_23 = liu_2013[liu_2013['date']=='2013-12-23']


liu_10_10_geo = geopandas.GeoDataFrame(liu_10_10, geometry = geopandas.points_from_xy(liu_10_10.lon,liu_10_10.lat),crs="EPSG:4326"
)

liu_10_10_new = geopandas.GeoDataFrame(liu_10_09, geometry = geopandas.points_from_xy(liu_10_09.lon,liu_10_09.lat),crs="EPSG:4326"
)
liu_12_22_geo = geopandas.GeoDataFrame(liu_12_22, geometry = geopandas.points_from_xy(liu_12_22.lon,liu_12_22.lat),crs="EPSG:4326"
)

liu_12_22_new = geopandas.GeoDataFrame(liu_12_23, geometry = geopandas.points_from_xy(liu_12_23.lon,liu_12_23.lat),crs="EPSG:4326"
)


liu_10_fin = liu_10_10_new.sjoin(liu_10_10_geo, how='left')
liu_22_fin = liu_12_22_new.sjoin(liu_12_22_geo, how='left')

liu_fill_10 = np.array(liu_10_09['liu']) + np.array(liu_10_11['liu'])/2
liu_fill_22 = np.array(liu_12_21['liu']) + np.array(liu_12_23['liu'])/2

for i in np.arange(0,len(liu_10_fin['liu_right']),1):
    if math.isnan(np.array(liu_10_fin['liu_right'])[i]):
        liu_10_fin['liu_right'][i] = liu_fill_10[i]
        liu_10_fin['date_right'][i] = np.array(liu_10_10_geo['date'])[0]
        
for i in np.arange(0,len(liu_22_fin['liu_right']),1):
    if math.isnan(np.array(liu_22_fin['liu_right'])[i]):
        liu_22_fin['liu_right'][i] = liu_fill_22[i]
        liu_22_fin['date_right'][i] = np.array(liu_12_22_geo['date'])[0]


liu_10_actual_fin = liu_10_fin[['lat_left','lon_left','date_right','liu_right']]
liu_10_actual_fin = liu_10_actual_fin.rename(columns={"lat_left":"lat","lon_left":"lon","date_right":"date","liu_right":"liu"})

liu_22_actual_fin = liu_22_fin[['lat_left','lon_left','date_right','liu_right']]
liu_22_actual_fin = liu_22_actual_fin.rename(columns={"lat_left":"lat","lon_left":"lon","date_right":"date","liu_right":"liu"})

liu_2013[liu_2013['date']=='2013-10-10'] = liu_10_actual_fin
liu_2013[liu_2013['date']=='2013-12-22'] = liu_22_actual_fin

liu_2013 = pd.concat([liu_2013,liu_10_actual_fin,liu_22_actual_fin])
liu_2013 = liu_2013.dropna()
liu_2013 = liu_2013.sort_values(by=['date'])

liu_2013.to_csv('liu_pm25_2013_daily_test.csv',index=False)
