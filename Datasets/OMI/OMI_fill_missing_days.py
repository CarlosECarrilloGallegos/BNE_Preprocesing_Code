import glob
import xarray as xr
import numpy as np
import h5py

## Specifically for 2016, which is missing entire days from the dataset

omi_may29 = h5py.File('/data0/shr/bne/data/raw/nox/omi/Daily/2016/OMSNO2_0.1x0.1_20160529_Col4_V4.h5','r')
omi_jun10 = h5py.File('/data0/shr/bne/data/raw/nox/omi/Daily/2016/OMSNO2_0.1x0.1_20160610_Col4_V4.h5','r')

omi_fill = (omi_may29 + omi_jun10)/2.0

omi_jun13 = xr.open_dataset('/data0/shr/bne/data/raw/nox/omi/Daily/2016/OMSNO2_0.1x0.1_20160613_Col4_V4.h5',phony_dims='sort')

omi_fill2 = (omi_jun10 + omi_jun13)/2.0


## Convert to h5 from nc

#do for each missing day (fill value is the same for missing days between may 29 and jun 10).
with h5py.File('/data0/shr/bne/data/raw/nox/omi/Daily/2016/OMSNO2_0.1x0.1_20160612_Col4_V4_filled.h5', 'w') as f:
    for var_name, var in omi_fill.variables.items():
            var_data = var.values
            f.create_dataset(var_name, data=var_data)


