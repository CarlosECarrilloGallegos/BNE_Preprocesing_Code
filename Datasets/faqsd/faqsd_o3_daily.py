import xarray as xr
import pandas as pd
import numpy as np
import glob
import scipy
import datetime

#faqsd
time = ['2002','2003','2004','2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2017','2019','2018']
for i in time:
    faqsd = pd.read_csv('/data0/shr/bne/data/raw/o3/faqsd/' + i +'/rsigserver?data%2FFAQSD%2Foutputs%2F'+i + '_ozone_daily_8hour_maximum.txt')
    faqsd = faqsd[['Date','Longitude','Latitude','ozone_daily_8hour_maximum(ppb)']]
    faqsd = faqsd.rename(columns={'Date':'date','Longitude':'lon','Latitude':'lat','ozone_daily_8hour_maximum(ppb)':'faqsd'})
    faqsd = faqsd[['lat','lon','date','faqsd']]
    faqsd['date'] = pd.to_datetime(faqsd['date'])
    faqsd.to_csv('/data0/shr/bne/data/o3/base_models/daily/formatted/faqsd/faqsd_o3_' + i + '_daily_mda8.csv',index=False)
    
#faqsd2   
time = ['2015','2016']
for i in time:
    faqsd = pd.read_csv('/data0/shr/bne/data/raw/o3/faqsd/' + i +'/rsigserver?data%2FFAQSD%2Foutputs%2F'+i + '_ozone_daily_8hour_maximum.txt')
    faqsd = faqsd[['Date','Longitude','Latitude','Prediction']]
    faqsd = faqsd.rename(columns={'Date':'date','Longitude':'lon','Latitude':'lat','Prediction':'faqsd'})
    faqsd = faqsd[['lat','lon','date','faqsd']]
    faqsd['date'] = pd.to_datetime(faqsd['date'])
    faqsd.to_csv('/data0/shr/bne/data/o3/base_models/daily/formatted/faqsd/faqsd_o3_' + i + '_daily_mda8.csv',index=False)
