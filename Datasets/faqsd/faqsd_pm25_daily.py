import xarray as xr
import pandas as pd
import numpy as np
import glob
import scipy
import datetime

#faqsd
time = ['2002','2003','2004','2005','2006','2007','2008','2009',
        '2010','2011','2012','2013','2014','2017','2018','2019']
#For 2015,2016, change 'pm25_daily_average(ug/m3)' to 'Prediction')
for i in time:
    faqsd = pd.read_csv('/data0/shr/bne/data/raw/pm25/faqsd/' + i +'/rsigserver?data%2FFAQSD%2Foutputs%2F'+i + '_pm25_daily_average.txt')
    faqsd = faqsd[['Date','Longitude','Latitude','pm25_daily_average(ug/m3)']]
    faqsd = faqsd.rename(columns={'Date':'date','Longitude':'lon','Latitude':'lat','pm25_daily_average(ug/m3)':'faqsd'})
    faqsd = faqsd[['lat','lon','date','faqsd']]
    faqsd['date'] = pd.to_datetime(faqsd['date'])
    faqsd.to_csv('/data0/shr/bne/data/pm25/base_models/daily/formatted/faqsd/faqsd_pm25_' + i + '_daily.csv',index=False)
    
   
time = ['2015','2016']
for i in time:
    faqsd = pd.read_csv('/data0/shr/bne/data/raw/pm25/faqsd/' + i +'/rsigserver?data%2FFAQSD%2Foutputs%2F'+i + '_pm25_daily_average.txt')
    faqsd = faqsd[['Date','Longitude','Latitude','Prediction']]
    faqsd = faqsd.rename(columns={'Date':'date','Longitude':'lon','Latitude':'lat','Prediction':'faqsd'})
    faqsd = faqsd[['lat','lon','date','faqsd']]
    faqsd['date'] = pd.to_datetime(faqsd['date'])
    faqsd.to_csv('/data0/shr/bne/data/pm25/base_models/daily/formatted/faqsd/faqsd_pm25_' + i + '_daily.csv',index=False)
    
