library(dplyr)
library(readr)
library(data.table)
library(sf)

## js
years = c('2010','2011','2012','2013','2014','2015','2016')# Future add '2002','2003','2004','2005','2006','2007','2008','2009')
sitecode <- readRDS('/data0/shr/bne/data/raw/nox/js/USGridSite_NO2.rds')

#NE_lon_max = -65.00
#NE_lon_min = - 82.00
#NE_lat_max = 48.00
#NE_lat_min = 38.00

i = 1
for (x in years){
    filenames = intersect(list.files(path = '/data0/shr/bne/data/raw/nox/js',paste('PredictionStep2_NO2_USGrid_',years[[i]],sep = ""))
                          ,list.files(path = '/data0/shr/bne/data/raw/nox/js','rds'))
    
    for (y in filenames){
        day <- readRDS(paste('/data0/shr/bne/data/raw/nox/js/',y,sep=""))
        day <- data.frame(t(day))
        day <- cbind(sitecode,day)
        day = subset(day,select = -c(SiteCode))
        colnames(day)[3] = 'js'
        colnames(day)[1] = 'lon'
        colnames(day)[2] = 'lat'
        #day = subset(day, lon > NE_lon_min & lon < NE_lon_max & lat > NE_lat_min & lat < NE_lat_max)
        date_format = substr(y,28,35)
        date_hyphenated = paste(substr(date_format,1,4),'-',substr(date_format,5,6),'-' ,substr(date_format,7,8),sep = "")
        date_unhyphenated = paste(substr(date_format,1,4),substr(date_format,5,6),substr(date_format,7,8),sep = "")
        date = rep(date_hyphenated,nrow(day))
        day$date <- c(date)
        day = day[,c(2,1,4,3)]
        write.csv(day,paste('/data0/shr/bne/data/nox/base_models/daily/formatted/js/js_no2_',date_unhyphenated,
                          '_daily.csv',sep= ""))
    }
    
    
    i = i+1
    

}
