import xarray as xr
import pandas as pd
import numpy as np
import glob
import scipy
import datetime


#equates
time = ['2002','2003','2004','2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019']

for j in time:
    
    csvs = sorted(glob.glob('/data0/shr/bne/data/raw/multi/equates/'+j +'/*.csv'))
    equates_year = []

    for i in csvs:
        equates_init = pd.read_csv(i,skiprows=[3]).reset_index()
        new_header = equates_init.iloc[0]
        equates = equates_init[1:]
        equates.columns = new_header
        equates = equates[['longitude','latitude','date','PM25_AVG']]
    
        equates_year.append(equates)
    
    equates_final = pd.concat(equates_year)
    
    equates_final = equates_final.rename(columns={'longitude':'lon','latitude':'lat','PM25_AVG':'equates'})
    
    equates_final = equates_final[['lat','lon','date','equates']]
    
    equates_final = equates_final.reset_index()[['lat','lon','date','equates']]
    
    equates_final['date'] = pd.to_datetime(equates_final['date'])
    
    equates_final.to_csv('/data0/shr/bne/data/pm25/daily/base_models/formatted/equates/equates_pm25_' + j + '_daily.csv', index=False)
    
