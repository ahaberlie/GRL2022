# Supporting data and code for:

# Intermediate and Extreme Warming Scenarios Modify Future Thunderstorm Activity

# Requirements

The best way to get this package working is to first install miniconda.

Then, install a python environment with conda-forge and geopandas as follows:

```
conda create -n grl22 -c conda-forge python=3.9 geopandas
```

then

```
conda activate grl22
conda install -c conda-forge dask netCDF4 xarray cartopy scipy numpy matplotlib jupyter notebook nb_conda_kernels
```

The biggest headache is getting geopandas to play nice with the other packages.  This approach has been tested in a Windows machine. YMMV.

Next, install this package

```
cd [location/of/base/GRL2022/package]
conda activate grl22 (if needed!)
pip install .
```

Once this is complete, you should run jupyter notebook and select the grl22 kernel.

# Instructions on how to access the derived data'

### You can run this using notebooks/Fig_0_Download_Data

# Download derived data

This will save the data in the existing data directory in the base package directory


```python
import tarfile
import urllib.request as urllib2

tgz = urllib2.urlopen("https://svrimg.niu.edu/grl_data/grl_data_22.tar.gz")
data = tarfile.open(fileobj=tgz, mode='r:gz')
data.extractall(path="../data")
```

# Boxplot data

### These are the data used to generate the boxplot data
### They are organized into three simulations

```
1. *_historical_*.csv (HIST)
2. *_future_4p5_*.csv (FUTR 4.5)
3. *_future_8p5_*.csv (FUTR 8.5)
```

### three dBZ thresholds

```
1. *_40dbz_*.csv (>= 40 dBZ)
2. *_50dbz_*.csv (>= 50 dBZ)
3. *_60dbz_*.csv (>= 60 dBZ)
```

### and four regions:

```
1. econus_*.csv (Eastern CONUS)
2. ama_*.csv (Amarillo)
3. mnp_*.csv (Minneapolis)
4. mph_*.csv (Memphis)
```


# Reading econus data for 40 dBZ / historical

### index column is the julian date
### other columns represent 'simulation years'

#### values are the mean count of 40 dBZ days in each region (max 1 for any given day)


```python
import pandas as pd

df = pd.read_csv("../data/boxplot/econus_historical_40dbz_days.csv", index_col=0, parse_dates=True)

df
```

# Cumulative data

### Exact same set up as boxplot data, but each year has a running count of days, except:

### three dBZ thresholds

```
1. *_40_cumu_dbz_*.csv (>= 40 dBZ)
2. *_50_cumu_dbz_*.csv (>= 50 dBZ)
3. *_60_cumu_dbz_*.csv (>= 60 dBZ)
```

### and the value is the sum of mean regional grid days up until that particular day of the year


```python
import pandas as pd

df = pd.read_csv("../data/cumul/econus_historical_40_cumu_dbz_days.csv", index_col=0, parse_dates=True)

df
```

# Grid days

### These are the netCDF files representing grid day counts for each season in each simulation year

### They are organized into three simulations

```
1. HIST_*.nc (HIST)
2. FUTR45_*.csv (FUTR 4.5)
3. FUTR85_*.csv (FUTR 8.5)
```

### three dBZ thresholds (which are saved as variables in the netCDF file)

```
1. '40_dbz_count' (>= 40 dBZ)
2. '50_dbz_count' (>= 50 dBZ)
3. '60_dbz_count' (>= 60 dBZ)
```

### the time dimension represents the start of the valid season


```python
import xarray as xr

ds = xr.open_dataset("../data/days/HIST_2000_JJA_grid_days.nc")

ds
```

# Often we will want to read in several files associated with each simulation:

#### Example: read in all HIST data using dask


```python
ds = xr.open_mfdataset("../data/days/HIST_*_*_grid_days.nc", combine='by_coords')

ds
```

# We can then calculate seasonal statistics:


```python
dseason = ds.groupby('time.season').mean('time')

dseason
```

# Geographic data

### These data define the grids used for CAPE/CIN


```python
import xarray as xr

ds = xr.open_dataset("../data/geog/geog_sim.nc")

ds
```

# Seasonal mean MU CAPE / MU CIN

### They are organized into three simulations

```
1. HIST_*.nc (HIST)
2. FUTR45_*.nc (FUTR 4.5)
3. FUTR85_*.nc (FUTR 8.5)
```

### Two variables are stored in each netCDF file

```
1. 'AFWA_CAPE_MU' (MU CAPE)
2. 'AFWA_CIN_MU' (MU CIN)
```

### the season dimension represents data for each season


```python
ds = xr.open_dataset("../data/thermo/HIST_seasonal_MUCAPE_MUCIN.nc")

ds
```

