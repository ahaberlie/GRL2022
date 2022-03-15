# Supporting data and code for:

# Intermediate and Extreme Warming Scenarios Modify Future Thunderstorm Activity

# Requirements

The best way to get this package working is to first install miniconda.

Thn, install a python environment with conda-forge and geopandas as follows:

```
conda create -n grl22 -c conda-forge python=3.9 geopandas
```

then

```
conda activate grl22
conda install -c conda-forge xarray cartopy geopandas scipy numpy matplotlib jupyter notebook nb_conda_kernels
```

The biggest headache is getting geopandas to play nice with the other packages.  This approach has been tested in a Windows machine. YMMV.

Next, install this package

```
cd [location/of/base/directory/package]
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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1990-1991</th>
      <th>1991-1992</th>
      <th>1992-1993</th>
      <th>1993-1994</th>
      <th>1994-1995</th>
      <th>1995-1996</th>
      <th>1996-1997</th>
      <th>1997-1998</th>
      <th>1998-1999</th>
      <th>1999-2000</th>
      <th>2000-2001</th>
      <th>2001-2002</th>
      <th>2002-2003</th>
      <th>2003-2004</th>
      <th>2004-2005</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1992-01-01</th>
      <td>0.151925</td>
      <td>0.015609</td>
      <td>0.140479</td>
      <td>0.273673</td>
      <td>0.054110</td>
      <td>0.047867</td>
      <td>0.166493</td>
      <td>0.299688</td>
      <td>0.020812</td>
      <td>0.043704</td>
      <td>0.026015</td>
      <td>0.040583</td>
      <td>0.342352</td>
      <td>0.240375</td>
      <td>0.007284</td>
    </tr>
    <tr>
      <th>1992-01-02</th>
      <td>0.156087</td>
      <td>0.137357</td>
      <td>0.012487</td>
      <td>0.072841</td>
      <td>0.031217</td>
      <td>0.026015</td>
      <td>0.124870</td>
      <td>0.337149</td>
      <td>0.015609</td>
      <td>0.158169</td>
      <td>0.044745</td>
      <td>0.207076</td>
      <td>0.109261</td>
      <td>0.218522</td>
      <td>0.035380</td>
    </tr>
    <tr>
      <th>1992-01-03</th>
      <td>0.105099</td>
      <td>0.363163</td>
      <td>0.026015</td>
      <td>0.068678</td>
      <td>0.024974</td>
      <td>0.016649</td>
      <td>0.095734</td>
      <td>0.197711</td>
      <td>0.048907</td>
      <td>0.299688</td>
      <td>0.062435</td>
      <td>0.315297</td>
      <td>0.065557</td>
      <td>0.280957</td>
      <td>0.178980</td>
    </tr>
    <tr>
      <th>1992-01-04</th>
      <td>0.002081</td>
      <td>0.424558</td>
      <td>0.059313</td>
      <td>0.084287</td>
      <td>0.020812</td>
      <td>0.006243</td>
      <td>0.130073</td>
      <td>0.186264</td>
      <td>0.010406</td>
      <td>0.057232</td>
      <td>0.084287</td>
      <td>0.143600</td>
      <td>0.008325</td>
      <td>0.106139</td>
      <td>0.053070</td>
    </tr>
    <tr>
      <th>1992-01-05</th>
      <td>0.021852</td>
      <td>0.181061</td>
      <td>0.157128</td>
      <td>0.143600</td>
      <td>0.037461</td>
      <td>0.030177</td>
      <td>0.080125</td>
      <td>0.141519</td>
      <td>0.002081</td>
      <td>0.167534</td>
      <td>0.039542</td>
      <td>0.120708</td>
      <td>0.044745</td>
      <td>0.144641</td>
      <td>0.065557</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1992-12-27</th>
      <td>0.026015</td>
      <td>0.065557</td>
      <td>0.127992</td>
      <td>0.038502</td>
      <td>0.041623</td>
      <td>0.045786</td>
      <td>0.395421</td>
      <td>0.152966</td>
      <td>0.097815</td>
      <td>0.171696</td>
      <td>0.013528</td>
      <td>0.015609</td>
      <td>0.097815</td>
      <td>0.080125</td>
      <td>0.109261</td>
    </tr>
    <tr>
      <th>1992-12-28</th>
      <td>0.000000</td>
      <td>0.033299</td>
      <td>0.110302</td>
      <td>0.116545</td>
      <td>0.120708</td>
      <td>0.061394</td>
      <td>0.276795</td>
      <td>0.019771</td>
      <td>0.018730</td>
      <td>0.156087</td>
      <td>0.002081</td>
      <td>0.020812</td>
      <td>0.048907</td>
      <td>0.029136</td>
      <td>0.098855</td>
    </tr>
    <tr>
      <th>1992-12-29</th>
      <td>0.038502</td>
      <td>0.014568</td>
      <td>0.152966</td>
      <td>0.111342</td>
      <td>0.200832</td>
      <td>0.078044</td>
      <td>0.251821</td>
      <td>0.116545</td>
      <td>0.038502</td>
      <td>0.235172</td>
      <td>0.014568</td>
      <td>0.059313</td>
      <td>0.233091</td>
      <td>0.024974</td>
      <td>0.042664</td>
    </tr>
    <tr>
      <th>1992-12-30</th>
      <td>0.142560</td>
      <td>0.010406</td>
      <td>0.187305</td>
      <td>0.112383</td>
      <td>0.264308</td>
      <td>0.152966</td>
      <td>0.181061</td>
      <td>0.160250</td>
      <td>0.087409</td>
      <td>0.517170</td>
      <td>0.005203</td>
      <td>0.048907</td>
      <td>0.343392</td>
      <td>0.098855</td>
      <td>0.112383</td>
    </tr>
    <tr>
      <th>1992-12-31</th>
      <td>0.189386</td>
      <td>0.000000</td>
      <td>0.222685</td>
      <td>0.246618</td>
      <td>0.156087</td>
      <td>0.298647</td>
      <td>0.122789</td>
      <td>0.251821</td>
      <td>0.033299</td>
      <td>0.218522</td>
      <td>0.003122</td>
      <td>0.067638</td>
      <td>0.292404</td>
      <td>0.209157</td>
      <td>0.079084</td>
    </tr>
  </tbody>
</table>
<p>366 rows × 15 columns</p>
</div>



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




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1990-1991</th>
      <th>1991-1992</th>
      <th>1992-1993</th>
      <th>1993-1994</th>
      <th>1994-1995</th>
      <th>1995-1996</th>
      <th>1996-1997</th>
      <th>1997-1998</th>
      <th>1998-1999</th>
      <th>1999-2000</th>
      <th>2000-2001</th>
      <th>2001-2002</th>
      <th>2002-2003</th>
      <th>2003-2004</th>
      <th>2004-2005</th>
      <th>mean</th>
      <th>median</th>
      <th>p25</th>
      <th>p75</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1992-01-01</th>
      <td>0.151925</td>
      <td>0.015609</td>
      <td>0.140479</td>
      <td>0.273673</td>
      <td>0.054110</td>
      <td>0.047867</td>
      <td>0.166493</td>
      <td>0.299688</td>
      <td>0.020812</td>
      <td>0.043704</td>
      <td>0.026015</td>
      <td>0.040583</td>
      <td>0.342352</td>
      <td>0.240375</td>
      <td>0.007284</td>
      <td>0.124731</td>
      <td>0.054110</td>
      <td>0.033299</td>
      <td>0.203434</td>
    </tr>
    <tr>
      <th>1992-01-02</th>
      <td>0.308012</td>
      <td>0.152966</td>
      <td>0.152966</td>
      <td>0.346514</td>
      <td>0.085328</td>
      <td>0.073881</td>
      <td>0.291363</td>
      <td>0.636837</td>
      <td>0.036420</td>
      <td>0.201873</td>
      <td>0.070760</td>
      <td>0.247659</td>
      <td>0.451613</td>
      <td>0.458897</td>
      <td>0.042664</td>
      <td>0.237183</td>
      <td>0.201873</td>
      <td>0.079605</td>
      <td>0.327263</td>
    </tr>
    <tr>
      <th>1992-01-03</th>
      <td>0.413111</td>
      <td>0.516129</td>
      <td>0.178980</td>
      <td>0.415193</td>
      <td>0.110302</td>
      <td>0.090531</td>
      <td>0.387097</td>
      <td>0.834547</td>
      <td>0.085328</td>
      <td>0.501561</td>
      <td>0.133195</td>
      <td>0.562955</td>
      <td>0.517170</td>
      <td>0.739854</td>
      <td>0.221644</td>
      <td>0.380506</td>
      <td>0.413111</td>
      <td>0.156087</td>
      <td>0.516649</td>
    </tr>
    <tr>
      <th>1992-01-04</th>
      <td>0.415193</td>
      <td>0.940687</td>
      <td>0.238293</td>
      <td>0.499480</td>
      <td>0.131113</td>
      <td>0.096774</td>
      <td>0.517170</td>
      <td>1.020812</td>
      <td>0.095734</td>
      <td>0.558793</td>
      <td>0.217482</td>
      <td>0.706556</td>
      <td>0.525494</td>
      <td>0.845994</td>
      <td>0.274714</td>
      <td>0.472286</td>
      <td>0.499480</td>
      <td>0.227888</td>
      <td>0.632674</td>
    </tr>
    <tr>
      <th>1992-01-05</th>
      <td>0.437045</td>
      <td>1.121748</td>
      <td>0.395421</td>
      <td>0.643080</td>
      <td>0.168574</td>
      <td>0.126951</td>
      <td>0.597294</td>
      <td>1.162331</td>
      <td>0.097815</td>
      <td>0.726327</td>
      <td>0.257024</td>
      <td>0.827263</td>
      <td>0.570239</td>
      <td>0.990635</td>
      <td>0.340271</td>
      <td>0.564135</td>
      <td>0.570239</td>
      <td>0.298647</td>
      <td>0.776795</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1992-12-27</th>
      <td>94.283039</td>
      <td>99.340271</td>
      <td>102.962539</td>
      <td>96.881374</td>
      <td>99.693028</td>
      <td>105.947971</td>
      <td>102.700312</td>
      <td>100.857440</td>
      <td>99.411030</td>
      <td>105.077003</td>
      <td>96.142560</td>
      <td>98.802289</td>
      <td>98.115505</td>
      <td>100.800208</td>
      <td>94.002081</td>
      <td>99.667777</td>
      <td>99.411030</td>
      <td>97.498439</td>
      <td>101.778876</td>
    </tr>
    <tr>
      <th>1992-12-28</th>
      <td>94.283039</td>
      <td>99.373569</td>
      <td>103.072841</td>
      <td>96.997919</td>
      <td>99.813736</td>
      <td>106.009365</td>
      <td>102.977107</td>
      <td>100.877211</td>
      <td>99.429761</td>
      <td>105.233091</td>
      <td>96.144641</td>
      <td>98.823101</td>
      <td>98.164412</td>
      <td>100.829344</td>
      <td>94.100937</td>
      <td>99.742005</td>
      <td>99.429761</td>
      <td>97.581165</td>
      <td>101.927159</td>
    </tr>
    <tr>
      <th>1992-12-29</th>
      <td>94.321540</td>
      <td>99.388137</td>
      <td>103.225806</td>
      <td>97.109261</td>
      <td>100.014568</td>
      <td>106.087409</td>
      <td>103.228928</td>
      <td>100.993757</td>
      <td>99.468262</td>
      <td>105.468262</td>
      <td>96.159209</td>
      <td>98.882414</td>
      <td>98.397503</td>
      <td>100.854318</td>
      <td>94.143600</td>
      <td>99.849532</td>
      <td>99.468262</td>
      <td>97.753382</td>
      <td>102.109781</td>
    </tr>
    <tr>
      <th>1992-12-30</th>
      <td>94.464100</td>
      <td>99.398543</td>
      <td>103.413111</td>
      <td>97.221644</td>
      <td>100.278876</td>
      <td>106.240375</td>
      <td>103.409990</td>
      <td>101.154006</td>
      <td>99.555671</td>
      <td>105.985432</td>
      <td>96.164412</td>
      <td>98.931322</td>
      <td>98.740895</td>
      <td>100.953174</td>
      <td>94.255983</td>
      <td>100.011169</td>
      <td>99.555671</td>
      <td>97.981270</td>
      <td>102.281998</td>
    </tr>
    <tr>
      <th>1992-12-31</th>
      <td>94.653486</td>
      <td>99.398543</td>
      <td>103.635796</td>
      <td>97.468262</td>
      <td>100.434964</td>
      <td>106.539022</td>
      <td>103.532778</td>
      <td>101.405827</td>
      <td>99.588970</td>
      <td>106.203954</td>
      <td>96.167534</td>
      <td>98.998959</td>
      <td>99.033299</td>
      <td>101.162331</td>
      <td>94.335068</td>
      <td>100.170586</td>
      <td>99.588970</td>
      <td>98.233611</td>
      <td>102.469303</td>
    </tr>
  </tbody>
</table>
<p>366 rows × 19 columns</p>
</div>



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




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block !important;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt;
Dimensions:       (time: 1, y: 38, x: 59)
Coordinates:
  * y             (y) float64 -1.308e+06 -1.228e+06 ... 1.572e+06 1.652e+06
  * x             (x) float64 -2.322e+06 -2.242e+06 ... 2.238e+06 2.318e+06
  * time          (time) datetime64[ns] 2000-06-01
Data variables:
    40_dbz_count  (time, y, x) float64 0.0 0.0 0.0 0.0 ... 36.0 33.0 34.0 30.0
    50_dbz_count  (time, y, x) float64 0.0 0.0 0.0 0.0 ... 11.0 7.0 12.0 11.0
    60_dbz_count  (time, y, x) float64 0.0 0.0 0.0 0.0 0.0 ... 1.0 0.0 0.0 0.0
Attributes: (12/17)
    TITLE:                        OUTPUT FROM WRF V4.1.2 MODEL
    WEST-EAST_GRID_DIMENSION:    1400
    SOUTH-NORTH_GRID_DIMENSION:  900
    DX:                          3750.0
    DY:                          3750.0
    DT:                          20.0
    ...                          ...
    STAND_LON:                   -97.5
    POLE_LAT:                    90.0
    POLE_LON:                    0.0
    MAP_PROJ:                    1
    MAP_PROJ_CHAR:               Lambert Conformal
    description:                 Mean JJA 40/50/60 dBZ grid days Retrospectiv...</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-a64cf2f8-b6ec-4ac6-9656-30f239e5c15c' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-a64cf2f8-b6ec-4ac6-9656-30f239e5c15c' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>time</span>: 1</li><li><span class='xr-has-index'>y</span>: 38</li><li><span class='xr-has-index'>x</span>: 59</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-e590b254-3c40-49b2-9f31-b9885247448c' class='xr-section-summary-in' type='checkbox'  checked><label for='section-e590b254-3c40-49b2-9f31-b9885247448c' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>y</span></div><div class='xr-var-dims'>(y)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>-1.308e+06 -1.228e+06 ... 1.652e+06</div><input id='attrs-fe531e51-e98e-4075-bed4-8729a3d5baf2' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-fe531e51-e98e-4075-bed4-8729a3d5baf2' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-a900baf0-d814-44d7-b131-ffe589bb8b18' class='xr-var-data-in' type='checkbox'><label for='data-a900baf0-d814-44d7-b131-ffe589bb8b18' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([-1307714.541637, -1227714.541637, -1147714.541637, -1067714.541637,
        -987714.541637,  -907714.541637,  -827714.541637,  -747714.541637,
        -667714.541637,  -587714.541637,  -507714.541637,  -427714.541637,
        -347714.541637,  -267714.541637,  -187714.541637,  -107714.541637,
         -27714.541637,    52285.458363,   132285.458363,   212285.458363,
         292285.458363,   372285.458363,   452285.458363,   532285.458363,
         612285.458363,   692285.458363,   772285.458363,   852285.458363,
         932285.458363,  1012285.458363,  1092285.458363,  1172285.458363,
        1252285.458363,  1332285.458363,  1412285.458363,  1492285.458363,
        1572285.458363,  1652285.458363])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>x</span></div><div class='xr-var-dims'>(x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>-2.322e+06 -2.242e+06 ... 2.318e+06</div><input id='attrs-0eecad2f-2455-4a90-acaa-1435c49a895a' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-0eecad2f-2455-4a90-acaa-1435c49a895a' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-13e5a808-6c65-4e4d-956e-4239e2fa0d12' class='xr-var-data-in' type='checkbox'><label for='data-13e5a808-6c65-4e4d-956e-4239e2fa0d12' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([-2.321582e+06, -2.241582e+06, -2.161582e+06, -2.081582e+06,
       -2.001582e+06, -1.921582e+06, -1.841582e+06, -1.761582e+06,
       -1.681582e+06, -1.601582e+06, -1.521582e+06, -1.441582e+06,
       -1.361582e+06, -1.281582e+06, -1.201582e+06, -1.121582e+06,
       -1.041582e+06, -9.615823e+05, -8.815823e+05, -8.015823e+05,
       -7.215823e+05, -6.415823e+05, -5.615823e+05, -4.815823e+05,
       -4.015823e+05, -3.215823e+05, -2.415823e+05, -1.615823e+05,
       -8.158228e+04, -1.582276e+03,  7.841772e+04,  1.584177e+05,
        2.384177e+05,  3.184177e+05,  3.984177e+05,  4.784177e+05,
        5.584177e+05,  6.384177e+05,  7.184177e+05,  7.984177e+05,
        8.784177e+05,  9.584177e+05,  1.038418e+06,  1.118418e+06,
        1.198418e+06,  1.278418e+06,  1.358418e+06,  1.438418e+06,
        1.518418e+06,  1.598418e+06,  1.678418e+06,  1.758418e+06,
        1.838418e+06,  1.918418e+06,  1.998418e+06,  2.078418e+06,
        2.158418e+06,  2.238418e+06,  2.318418e+06])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>2000-06-01</div><input id='attrs-a180ab4b-4842-488f-8b1b-b6e907e208c1' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-a180ab4b-4842-488f-8b1b-b6e907e208c1' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-aa545e37-cf43-43be-b975-d3329d377f65' class='xr-var-data-in' type='checkbox'><label for='data-aa545e37-cf43-43be-b975-d3329d377f65' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;2000-06-01T00:00:00.000000000&#x27;], dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-f32801e3-2a82-45e9-8817-173f10933fdf' class='xr-section-summary-in' type='checkbox'  checked><label for='section-f32801e3-2a82-45e9-8817-173f10933fdf' class='xr-section-summary' >Data variables: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>40_dbz_count</span></div><div class='xr-var-dims'>(time, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-df36e307-4ce1-4143-b2cd-a572b40ad5c3' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-df36e307-4ce1-4143-b2cd-a572b40ad5c3' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-3b6423d4-9f3a-4b61-a1d3-72c5fb0f28a8' class='xr-var-data-in' type='checkbox'><label for='data-3b6423d4-9f3a-4b61-a1d3-72c5fb0f28a8' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([[[ 0.,  0., ..., 10.,  1.],
        [ 0.,  0., ..., 14.,  2.],
        ...,
        [ 0.,  1., ..., 34., 32.],
        [ 2.,  3., ..., 34., 30.]]])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>50_dbz_count</span></div><div class='xr-var-dims'>(time, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-150cf721-907c-4731-a161-9dc4e6b93fc2' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-150cf721-907c-4731-a161-9dc4e6b93fc2' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-09a5275d-e81e-46c3-b890-602d2bb8ec20' class='xr-var-data-in' type='checkbox'><label for='data-09a5275d-e81e-46c3-b890-602d2bb8ec20' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([[[ 0.,  0., ...,  2.,  0.],
        [ 0.,  0., ...,  5.,  0.],
        ...,
        [ 0.,  0., ..., 11.,  9.],
        [ 0.,  0., ..., 12., 11.]]])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>60_dbz_count</span></div><div class='xr-var-dims'>(time, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-3197e8ce-f0b7-4c7e-948b-56a55a6e2003' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-3197e8ce-f0b7-4c7e-948b-56a55a6e2003' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-93edbcc2-8d45-49b9-8890-f446bb90851b' class='xr-var-data-in' type='checkbox'><label for='data-93edbcc2-8d45-49b9-8890-f446bb90851b' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([[[0., 0., ..., 0., 0.],
        [0., 0., ..., 0., 0.],
        ...,
        [0., 0., ..., 0., 0.],
        [0., 0., ..., 0., 0.]]])</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-4a0423e4-62b9-4c72-8c0d-11079ddce04a' class='xr-section-summary-in' type='checkbox'  ><label for='section-4a0423e4-62b9-4c72-8c0d-11079ddce04a' class='xr-section-summary' >Attributes: <span>(17)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>TITLE :</span></dt><dd> OUTPUT FROM WRF V4.1.2 MODEL</dd><dt><span>WEST-EAST_GRID_DIMENSION :</span></dt><dd>1400</dd><dt><span>SOUTH-NORTH_GRID_DIMENSION :</span></dt><dd>900</dd><dt><span>DX :</span></dt><dd>3750.0</dd><dt><span>DY :</span></dt><dd>3750.0</dd><dt><span>DT :</span></dt><dd>20.0</dd><dt><span>CEN_LAT :</span></dt><dd>38.500004</dd><dt><span>CEN_LON :</span></dt><dd>-97.5</dd><dt><span>TRUELAT1 :</span></dt><dd>38.5</dd><dt><span>TRUELAT2 :</span></dt><dd>38.5</dd><dt><span>MOAD_CEN_LAT :</span></dt><dd>38.500004</dd><dt><span>STAND_LON :</span></dt><dd>-97.5</dd><dt><span>POLE_LAT :</span></dt><dd>90.0</dd><dt><span>POLE_LON :</span></dt><dd>0.0</dd><dt><span>MAP_PROJ :</span></dt><dd>1</dd><dt><span>MAP_PROJ_CHAR :</span></dt><dd>Lambert Conformal</dd><dt><span>description :</span></dt><dd>Mean JJA 40/50/60 dBZ grid days Retrospective (1990-2005)</dd></dl></div></li></ul></div></div>



# Often we will want to read in several files associated with each simulation:

#### Example: read in all HIST data using dask


```python
ds = xr.open_mfdataset("../data/days/HIST_*_*_grid_days.nc", combine='by_coords')

ds
```




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block !important;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt;
Dimensions:       (time: 60, y: 38, x: 59)
Coordinates:
  * y             (y) float64 -1.308e+06 -1.228e+06 ... 1.572e+06 1.652e+06
  * x             (x) float64 -2.322e+06 -2.242e+06 ... 2.238e+06 2.318e+06
  * time          (time) datetime64[ns] 1990-10-01 1990-12-01 ... 2005-06-01
Data variables:
    40_dbz_count  (time, y, x) float64 dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;
    50_dbz_count  (time, y, x) float64 dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;
    60_dbz_count  (time, y, x) float64 dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;
Attributes: (12/17)
    TITLE:                        OUTPUT FROM WRF V4.1.2 MODEL
    WEST-EAST_GRID_DIMENSION:    1400
    SOUTH-NORTH_GRID_DIMENSION:  900
    DX:                          3750.0
    DY:                          3750.0
    DT:                          20.0
    ...                          ...
    STAND_LON:                   -97.5
    POLE_LAT:                    90.0
    POLE_LON:                    0.0
    MAP_PROJ:                    1
    MAP_PROJ_CHAR:               Lambert Conformal
    description:                 Mean SON 40/50/60 dBZ grid days Retrospectiv...</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-4da13605-d82e-4657-a230-9626b336745e' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-4da13605-d82e-4657-a230-9626b336745e' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>time</span>: 60</li><li><span class='xr-has-index'>y</span>: 38</li><li><span class='xr-has-index'>x</span>: 59</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-44e01fb2-4526-4bfe-8fba-10c3c5ef1acd' class='xr-section-summary-in' type='checkbox'  checked><label for='section-44e01fb2-4526-4bfe-8fba-10c3c5ef1acd' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>y</span></div><div class='xr-var-dims'>(y)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>-1.308e+06 -1.228e+06 ... 1.652e+06</div><input id='attrs-e9d8d104-ad68-45d0-a5c4-7c368a2fdbcc' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-e9d8d104-ad68-45d0-a5c4-7c368a2fdbcc' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-2bdd0112-0650-4f14-9bf5-dc67a0f44a50' class='xr-var-data-in' type='checkbox'><label for='data-2bdd0112-0650-4f14-9bf5-dc67a0f44a50' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([-1307714.541637, -1227714.541637, -1147714.541637, -1067714.541637,
        -987714.541637,  -907714.541637,  -827714.541637,  -747714.541637,
        -667714.541637,  -587714.541637,  -507714.541637,  -427714.541637,
        -347714.541637,  -267714.541637,  -187714.541637,  -107714.541637,
         -27714.541637,    52285.458363,   132285.458363,   212285.458363,
         292285.458363,   372285.458363,   452285.458363,   532285.458363,
         612285.458363,   692285.458363,   772285.458363,   852285.458363,
         932285.458363,  1012285.458363,  1092285.458363,  1172285.458363,
        1252285.458363,  1332285.458363,  1412285.458363,  1492285.458363,
        1572285.458363,  1652285.458363])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>x</span></div><div class='xr-var-dims'>(x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>-2.322e+06 -2.242e+06 ... 2.318e+06</div><input id='attrs-82bd65d5-0479-4c58-a743-46ab3dd60c3f' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-82bd65d5-0479-4c58-a743-46ab3dd60c3f' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-d98d707c-196b-4803-9e7c-1b9bdb298fde' class='xr-var-data-in' type='checkbox'><label for='data-d98d707c-196b-4803-9e7c-1b9bdb298fde' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([-2.321582e+06, -2.241582e+06, -2.161582e+06, -2.081582e+06,
       -2.001582e+06, -1.921582e+06, -1.841582e+06, -1.761582e+06,
       -1.681582e+06, -1.601582e+06, -1.521582e+06, -1.441582e+06,
       -1.361582e+06, -1.281582e+06, -1.201582e+06, -1.121582e+06,
       -1.041582e+06, -9.615823e+05, -8.815823e+05, -8.015823e+05,
       -7.215823e+05, -6.415823e+05, -5.615823e+05, -4.815823e+05,
       -4.015823e+05, -3.215823e+05, -2.415823e+05, -1.615823e+05,
       -8.158228e+04, -1.582276e+03,  7.841772e+04,  1.584177e+05,
        2.384177e+05,  3.184177e+05,  3.984177e+05,  4.784177e+05,
        5.584177e+05,  6.384177e+05,  7.184177e+05,  7.984177e+05,
        8.784177e+05,  9.584177e+05,  1.038418e+06,  1.118418e+06,
        1.198418e+06,  1.278418e+06,  1.358418e+06,  1.438418e+06,
        1.518418e+06,  1.598418e+06,  1.678418e+06,  1.758418e+06,
        1.838418e+06,  1.918418e+06,  1.998418e+06,  2.078418e+06,
        2.158418e+06,  2.238418e+06,  2.318418e+06])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>time</span></div><div class='xr-var-dims'>(time)</div><div class='xr-var-dtype'>datetime64[ns]</div><div class='xr-var-preview xr-preview'>1990-10-01 ... 2005-06-01</div><input id='attrs-38c64372-8ba4-4966-a623-e62b1a953779' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-38c64372-8ba4-4966-a623-e62b1a953779' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-3a9b2544-aaac-4f4f-9842-c5629b5eda8b' class='xr-var-data-in' type='checkbox'><label for='data-3a9b2544-aaac-4f4f-9842-c5629b5eda8b' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;1990-10-01T00:00:00.000000000&#x27;, &#x27;1990-12-01T00:00:00.000000000&#x27;,
       &#x27;1991-03-01T00:00:00.000000000&#x27;, &#x27;1991-06-01T00:00:00.000000000&#x27;,
       &#x27;1991-10-01T00:00:00.000000000&#x27;, &#x27;1991-12-01T00:00:00.000000000&#x27;,
       &#x27;1992-03-01T00:00:00.000000000&#x27;, &#x27;1992-06-01T00:00:00.000000000&#x27;,
       &#x27;1992-10-01T00:00:00.000000000&#x27;, &#x27;1992-12-01T00:00:00.000000000&#x27;,
       &#x27;1993-03-01T00:00:00.000000000&#x27;, &#x27;1993-06-01T00:00:00.000000000&#x27;,
       &#x27;1993-10-01T00:00:00.000000000&#x27;, &#x27;1993-12-01T00:00:00.000000000&#x27;,
       &#x27;1994-03-01T00:00:00.000000000&#x27;, &#x27;1994-06-01T00:00:00.000000000&#x27;,
       &#x27;1994-10-01T00:00:00.000000000&#x27;, &#x27;1994-12-01T00:00:00.000000000&#x27;,
       &#x27;1995-03-01T00:00:00.000000000&#x27;, &#x27;1995-06-01T00:00:00.000000000&#x27;,
       &#x27;1995-10-01T00:00:00.000000000&#x27;, &#x27;1995-12-01T00:00:00.000000000&#x27;,
       &#x27;1996-03-01T00:00:00.000000000&#x27;, &#x27;1996-06-01T00:00:00.000000000&#x27;,
       &#x27;1996-10-01T00:00:00.000000000&#x27;, &#x27;1996-12-01T00:00:00.000000000&#x27;,
       &#x27;1997-03-01T00:00:00.000000000&#x27;, &#x27;1997-06-01T00:00:00.000000000&#x27;,
       &#x27;1997-10-01T00:00:00.000000000&#x27;, &#x27;1997-12-01T00:00:00.000000000&#x27;,
       &#x27;1998-03-01T00:00:00.000000000&#x27;, &#x27;1998-06-01T00:00:00.000000000&#x27;,
       &#x27;1998-10-01T00:00:00.000000000&#x27;, &#x27;1998-12-01T00:00:00.000000000&#x27;,
       &#x27;1999-03-01T00:00:00.000000000&#x27;, &#x27;1999-06-01T00:00:00.000000000&#x27;,
       &#x27;1999-10-01T00:00:00.000000000&#x27;, &#x27;1999-12-01T00:00:00.000000000&#x27;,
       &#x27;2000-03-01T00:00:00.000000000&#x27;, &#x27;2000-06-01T00:00:00.000000000&#x27;,
       &#x27;2000-10-01T00:00:00.000000000&#x27;, &#x27;2000-12-01T00:00:00.000000000&#x27;,
       &#x27;2001-03-01T00:00:00.000000000&#x27;, &#x27;2001-06-01T00:00:00.000000000&#x27;,
       &#x27;2001-10-01T00:00:00.000000000&#x27;, &#x27;2001-12-01T00:00:00.000000000&#x27;,
       &#x27;2002-03-01T00:00:00.000000000&#x27;, &#x27;2002-06-01T00:00:00.000000000&#x27;,
       &#x27;2002-10-01T00:00:00.000000000&#x27;, &#x27;2002-12-01T00:00:00.000000000&#x27;,
       &#x27;2003-03-01T00:00:00.000000000&#x27;, &#x27;2003-06-01T00:00:00.000000000&#x27;,
       &#x27;2003-10-01T00:00:00.000000000&#x27;, &#x27;2003-12-01T00:00:00.000000000&#x27;,
       &#x27;2004-03-01T00:00:00.000000000&#x27;, &#x27;2004-06-01T00:00:00.000000000&#x27;,
       &#x27;2004-10-01T00:00:00.000000000&#x27;, &#x27;2004-12-01T00:00:00.000000000&#x27;,
       &#x27;2005-03-01T00:00:00.000000000&#x27;, &#x27;2005-06-01T00:00:00.000000000&#x27;],
      dtype=&#x27;datetime64[ns]&#x27;)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-d0aca672-a214-4c70-a6ae-23c08219d490' class='xr-section-summary-in' type='checkbox'  checked><label for='section-d0aca672-a214-4c70-a6ae-23c08219d490' class='xr-section-summary' >Data variables: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>40_dbz_count</span></div><div class='xr-var-dims'>(time, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;</div><input id='attrs-a039d10f-c29c-4e98-b82c-d3091395b2eb' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-a039d10f-c29c-4e98-b82c-d3091395b2eb' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-37ea2813-45b4-4963-b59e-f8f0699ec904' class='xr-var-data-in' type='checkbox'><label for='data-37ea2813-45b4-4963-b59e-f8f0699ec904' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 1.03 MiB </td>
                        <td> 17.52 kiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (60, 38, 59) </td>
                        <td> (1, 38, 59) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 180 Tasks </td>
                        <td> 60 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="248" height="196" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="76" x2="80" y2="146" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="76" style="stroke-width:2" />
  <line x1="13" y1="3" x2="13" y2="79" />
  <line x1="17" y1="7" x2="17" y2="83" />
  <line x1="20" y1="10" x2="20" y2="86" />
  <line x1="24" y1="14" x2="24" y2="90" />
  <line x1="27" y1="17" x2="27" y2="93" />
  <line x1="31" y1="21" x2="31" y2="97" />
  <line x1="35" y1="25" x2="35" y2="101" />
  <line x1="39" y1="29" x2="39" y2="105" />
  <line x1="42" y1="32" x2="42" y2="108" />
  <line x1="46" y1="36" x2="46" y2="112" />
  <line x1="50" y1="40" x2="50" y2="116" />
  <line x1="53" y1="43" x2="53" y2="119" />
  <line x1="58" y1="48" x2="58" y2="124" />
  <line x1="61" y1="51" x2="61" y2="127" />
  <line x1="65" y1="55" x2="65" y2="131" />
  <line x1="68" y1="58" x2="68" y2="134" />
  <line x1="72" y1="62" x2="72" y2="138" />
  <line x1="75" y1="65" x2="75" y2="141" />
  <line x1="80" y1="70" x2="80" y2="146" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 80.58823529411765,70.58823529411765 80.58823529411765,146.58823529411765 10.0,76.0" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="128" y2="0" style="stroke-width:2" />
  <line x1="13" y1="3" x2="131" y2="3" />
  <line x1="17" y1="7" x2="135" y2="7" />
  <line x1="20" y1="10" x2="138" y2="10" />
  <line x1="24" y1="14" x2="142" y2="14" />
  <line x1="27" y1="17" x2="145" y2="17" />
  <line x1="31" y1="21" x2="149" y2="21" />
  <line x1="35" y1="25" x2="153" y2="25" />
  <line x1="39" y1="29" x2="157" y2="29" />
  <line x1="42" y1="32" x2="160" y2="32" />
  <line x1="46" y1="36" x2="164" y2="36" />
  <line x1="50" y1="40" x2="168" y2="40" />
  <line x1="53" y1="43" x2="171" y2="43" />
  <line x1="58" y1="48" x2="176" y2="48" />
  <line x1="61" y1="51" x2="179" y2="51" />
  <line x1="65" y1="55" x2="183" y2="55" />
  <line x1="68" y1="58" x2="186" y2="58" />
  <line x1="72" y1="62" x2="190" y2="62" />
  <line x1="75" y1="65" x2="193" y2="65" />
  <line x1="80" y1="70" x2="198" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="128" y1="0" x2="198" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 128.0,0.0 198.58823529411765,70.58823529411765 80.58823529411765,70.58823529411765" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="198" y2="70" style="stroke-width:2" />
  <line x1="80" y1="146" x2="198" y2="146" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="146" style="stroke-width:2" />
  <line x1="198" y1="70" x2="198" y2="146" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.58823529411765,70.58823529411765 198.58823529411765,70.58823529411765 198.58823529411765,146.58823529411765 80.58823529411765,146.58823529411765" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="139.588235" y="166.588235" font-size="1.0rem" font-weight="100" text-anchor="middle" >59</text>
  <text x="218.588235" y="108.588235" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,218.588235,108.588235)">38</text>
  <text x="35.294118" y="131.294118" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,131.294118)">60</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>50_dbz_count</span></div><div class='xr-var-dims'>(time, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;</div><input id='attrs-3010f113-9962-4ce1-89a6-5326be858e66' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-3010f113-9962-4ce1-89a6-5326be858e66' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-50eedb1d-dae1-4d96-9042-baf852c042aa' class='xr-var-data-in' type='checkbox'><label for='data-50eedb1d-dae1-4d96-9042-baf852c042aa' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 1.03 MiB </td>
                        <td> 17.52 kiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (60, 38, 59) </td>
                        <td> (1, 38, 59) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 180 Tasks </td>
                        <td> 60 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="248" height="196" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="76" x2="80" y2="146" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="76" style="stroke-width:2" />
  <line x1="13" y1="3" x2="13" y2="79" />
  <line x1="17" y1="7" x2="17" y2="83" />
  <line x1="20" y1="10" x2="20" y2="86" />
  <line x1="24" y1="14" x2="24" y2="90" />
  <line x1="27" y1="17" x2="27" y2="93" />
  <line x1="31" y1="21" x2="31" y2="97" />
  <line x1="35" y1="25" x2="35" y2="101" />
  <line x1="39" y1="29" x2="39" y2="105" />
  <line x1="42" y1="32" x2="42" y2="108" />
  <line x1="46" y1="36" x2="46" y2="112" />
  <line x1="50" y1="40" x2="50" y2="116" />
  <line x1="53" y1="43" x2="53" y2="119" />
  <line x1="58" y1="48" x2="58" y2="124" />
  <line x1="61" y1="51" x2="61" y2="127" />
  <line x1="65" y1="55" x2="65" y2="131" />
  <line x1="68" y1="58" x2="68" y2="134" />
  <line x1="72" y1="62" x2="72" y2="138" />
  <line x1="75" y1="65" x2="75" y2="141" />
  <line x1="80" y1="70" x2="80" y2="146" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 80.58823529411765,70.58823529411765 80.58823529411765,146.58823529411765 10.0,76.0" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="128" y2="0" style="stroke-width:2" />
  <line x1="13" y1="3" x2="131" y2="3" />
  <line x1="17" y1="7" x2="135" y2="7" />
  <line x1="20" y1="10" x2="138" y2="10" />
  <line x1="24" y1="14" x2="142" y2="14" />
  <line x1="27" y1="17" x2="145" y2="17" />
  <line x1="31" y1="21" x2="149" y2="21" />
  <line x1="35" y1="25" x2="153" y2="25" />
  <line x1="39" y1="29" x2="157" y2="29" />
  <line x1="42" y1="32" x2="160" y2="32" />
  <line x1="46" y1="36" x2="164" y2="36" />
  <line x1="50" y1="40" x2="168" y2="40" />
  <line x1="53" y1="43" x2="171" y2="43" />
  <line x1="58" y1="48" x2="176" y2="48" />
  <line x1="61" y1="51" x2="179" y2="51" />
  <line x1="65" y1="55" x2="183" y2="55" />
  <line x1="68" y1="58" x2="186" y2="58" />
  <line x1="72" y1="62" x2="190" y2="62" />
  <line x1="75" y1="65" x2="193" y2="65" />
  <line x1="80" y1="70" x2="198" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="128" y1="0" x2="198" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 128.0,0.0 198.58823529411765,70.58823529411765 80.58823529411765,70.58823529411765" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="198" y2="70" style="stroke-width:2" />
  <line x1="80" y1="146" x2="198" y2="146" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="146" style="stroke-width:2" />
  <line x1="198" y1="70" x2="198" y2="146" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.58823529411765,70.58823529411765 198.58823529411765,70.58823529411765 198.58823529411765,146.58823529411765 80.58823529411765,146.58823529411765" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="139.588235" y="166.588235" font-size="1.0rem" font-weight="100" text-anchor="middle" >59</text>
  <text x="218.588235" y="108.588235" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,218.588235,108.588235)">38</text>
  <text x="35.294118" y="131.294118" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,131.294118)">60</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>60_dbz_count</span></div><div class='xr-var-dims'>(time, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;</div><input id='attrs-43533f68-15c2-4d16-9166-e2dd239f0c57' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-43533f68-15c2-4d16-9166-e2dd239f0c57' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-65d3fd19-a80d-4ea7-9c63-98c815607a09' class='xr-var-data-in' type='checkbox'><label for='data-65d3fd19-a80d-4ea7-9c63-98c815607a09' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 1.03 MiB </td>
                        <td> 17.52 kiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (60, 38, 59) </td>
                        <td> (1, 38, 59) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 180 Tasks </td>
                        <td> 60 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="248" height="196" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="10" y1="76" x2="80" y2="146" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="76" style="stroke-width:2" />
  <line x1="13" y1="3" x2="13" y2="79" />
  <line x1="17" y1="7" x2="17" y2="83" />
  <line x1="20" y1="10" x2="20" y2="86" />
  <line x1="24" y1="14" x2="24" y2="90" />
  <line x1="27" y1="17" x2="27" y2="93" />
  <line x1="31" y1="21" x2="31" y2="97" />
  <line x1="35" y1="25" x2="35" y2="101" />
  <line x1="39" y1="29" x2="39" y2="105" />
  <line x1="42" y1="32" x2="42" y2="108" />
  <line x1="46" y1="36" x2="46" y2="112" />
  <line x1="50" y1="40" x2="50" y2="116" />
  <line x1="53" y1="43" x2="53" y2="119" />
  <line x1="58" y1="48" x2="58" y2="124" />
  <line x1="61" y1="51" x2="61" y2="127" />
  <line x1="65" y1="55" x2="65" y2="131" />
  <line x1="68" y1="58" x2="68" y2="134" />
  <line x1="72" y1="62" x2="72" y2="138" />
  <line x1="75" y1="65" x2="75" y2="141" />
  <line x1="80" y1="70" x2="80" y2="146" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 80.58823529411765,70.58823529411765 80.58823529411765,146.58823529411765 10.0,76.0" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="128" y2="0" style="stroke-width:2" />
  <line x1="13" y1="3" x2="131" y2="3" />
  <line x1="17" y1="7" x2="135" y2="7" />
  <line x1="20" y1="10" x2="138" y2="10" />
  <line x1="24" y1="14" x2="142" y2="14" />
  <line x1="27" y1="17" x2="145" y2="17" />
  <line x1="31" y1="21" x2="149" y2="21" />
  <line x1="35" y1="25" x2="153" y2="25" />
  <line x1="39" y1="29" x2="157" y2="29" />
  <line x1="42" y1="32" x2="160" y2="32" />
  <line x1="46" y1="36" x2="164" y2="36" />
  <line x1="50" y1="40" x2="168" y2="40" />
  <line x1="53" y1="43" x2="171" y2="43" />
  <line x1="58" y1="48" x2="176" y2="48" />
  <line x1="61" y1="51" x2="179" y2="51" />
  <line x1="65" y1="55" x2="183" y2="55" />
  <line x1="68" y1="58" x2="186" y2="58" />
  <line x1="72" y1="62" x2="190" y2="62" />
  <line x1="75" y1="65" x2="193" y2="65" />
  <line x1="80" y1="70" x2="198" y2="70" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="80" y2="70" style="stroke-width:2" />
  <line x1="128" y1="0" x2="198" y2="70" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 128.0,0.0 198.58823529411765,70.58823529411765 80.58823529411765,70.58823529411765" style="fill:#8B4903A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="80" y1="70" x2="198" y2="70" style="stroke-width:2" />
  <line x1="80" y1="146" x2="198" y2="146" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="80" y1="70" x2="80" y2="146" style="stroke-width:2" />
  <line x1="198" y1="70" x2="198" y2="146" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="80.58823529411765,70.58823529411765 198.58823529411765,70.58823529411765 198.58823529411765,146.58823529411765 80.58823529411765,146.58823529411765" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="139.588235" y="166.588235" font-size="1.0rem" font-weight="100" text-anchor="middle" >59</text>
  <text x="218.588235" y="108.588235" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,218.588235,108.588235)">38</text>
  <text x="35.294118" y="131.294118" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,35.294118,131.294118)">60</text>
</svg>
        </td>
    </tr>
</table></div></li></ul></div></li><li class='xr-section-item'><input id='section-55064107-d013-444b-93ca-83062d0f9e8a' class='xr-section-summary-in' type='checkbox'  ><label for='section-55064107-d013-444b-93ca-83062d0f9e8a' class='xr-section-summary' >Attributes: <span>(17)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>TITLE :</span></dt><dd> OUTPUT FROM WRF V4.1.2 MODEL</dd><dt><span>WEST-EAST_GRID_DIMENSION :</span></dt><dd>1400</dd><dt><span>SOUTH-NORTH_GRID_DIMENSION :</span></dt><dd>900</dd><dt><span>DX :</span></dt><dd>3750.0</dd><dt><span>DY :</span></dt><dd>3750.0</dd><dt><span>DT :</span></dt><dd>20.0</dd><dt><span>CEN_LAT :</span></dt><dd>38.500004</dd><dt><span>CEN_LON :</span></dt><dd>-97.5</dd><dt><span>TRUELAT1 :</span></dt><dd>38.5</dd><dt><span>TRUELAT2 :</span></dt><dd>38.5</dd><dt><span>MOAD_CEN_LAT :</span></dt><dd>38.500004</dd><dt><span>STAND_LON :</span></dt><dd>-97.5</dd><dt><span>POLE_LAT :</span></dt><dd>90.0</dd><dt><span>POLE_LON :</span></dt><dd>0.0</dd><dt><span>MAP_PROJ :</span></dt><dd>1</dd><dt><span>MAP_PROJ_CHAR :</span></dt><dd>Lambert Conformal</dd><dt><span>description :</span></dt><dd>Mean SON 40/50/60 dBZ grid days Retrospective (1990-2005)</dd></dl></div></li></ul></div></div>



# We can then calculate seasonal statistics:


```python
dseason = ds.groupby('time.season').mean('time')

dseason
```




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block !important;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt;
Dimensions:       (season: 4, y: 38, x: 59)
Coordinates:
  * y             (y) float64 -1.308e+06 -1.228e+06 ... 1.572e+06 1.652e+06
  * x             (x) float64 -2.322e+06 -2.242e+06 ... 2.238e+06 2.318e+06
  * season        (season) object &#x27;DJF&#x27; &#x27;JJA&#x27; &#x27;MAM&#x27; &#x27;SON&#x27;
Data variables:
    40_dbz_count  (season, y, x) float64 dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;
    50_dbz_count  (season, y, x) float64 dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;
    60_dbz_count  (season, y, x) float64 dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-16d10aa6-d1a2-4aaf-ab77-d87a08a5e6fe' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-16d10aa6-d1a2-4aaf-ab77-d87a08a5e6fe' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>season</span>: 4</li><li><span class='xr-has-index'>y</span>: 38</li><li><span class='xr-has-index'>x</span>: 59</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-14c19e99-7511-40e7-a70e-c49c6f53c56e' class='xr-section-summary-in' type='checkbox'  checked><label for='section-14c19e99-7511-40e7-a70e-c49c6f53c56e' class='xr-section-summary' >Coordinates: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>y</span></div><div class='xr-var-dims'>(y)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>-1.308e+06 -1.228e+06 ... 1.652e+06</div><input id='attrs-641ade34-825e-49dc-b3f2-17e6bfc97b8c' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-641ade34-825e-49dc-b3f2-17e6bfc97b8c' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-1efbb972-a6f4-45f8-8b70-0a569ad7178f' class='xr-var-data-in' type='checkbox'><label for='data-1efbb972-a6f4-45f8-8b70-0a569ad7178f' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([-1307714.541637, -1227714.541637, -1147714.541637, -1067714.541637,
        -987714.541637,  -907714.541637,  -827714.541637,  -747714.541637,
        -667714.541637,  -587714.541637,  -507714.541637,  -427714.541637,
        -347714.541637,  -267714.541637,  -187714.541637,  -107714.541637,
         -27714.541637,    52285.458363,   132285.458363,   212285.458363,
         292285.458363,   372285.458363,   452285.458363,   532285.458363,
         612285.458363,   692285.458363,   772285.458363,   852285.458363,
         932285.458363,  1012285.458363,  1092285.458363,  1172285.458363,
        1252285.458363,  1332285.458363,  1412285.458363,  1492285.458363,
        1572285.458363,  1652285.458363])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>x</span></div><div class='xr-var-dims'>(x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>-2.322e+06 -2.242e+06 ... 2.318e+06</div><input id='attrs-9bc99aba-7cfc-43f7-987c-b87f9ec35767' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-9bc99aba-7cfc-43f7-987c-b87f9ec35767' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-23ca7b95-3d09-49ae-9b7f-b54243d397ed' class='xr-var-data-in' type='checkbox'><label for='data-23ca7b95-3d09-49ae-9b7f-b54243d397ed' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([-2.321582e+06, -2.241582e+06, -2.161582e+06, -2.081582e+06,
       -2.001582e+06, -1.921582e+06, -1.841582e+06, -1.761582e+06,
       -1.681582e+06, -1.601582e+06, -1.521582e+06, -1.441582e+06,
       -1.361582e+06, -1.281582e+06, -1.201582e+06, -1.121582e+06,
       -1.041582e+06, -9.615823e+05, -8.815823e+05, -8.015823e+05,
       -7.215823e+05, -6.415823e+05, -5.615823e+05, -4.815823e+05,
       -4.015823e+05, -3.215823e+05, -2.415823e+05, -1.615823e+05,
       -8.158228e+04, -1.582276e+03,  7.841772e+04,  1.584177e+05,
        2.384177e+05,  3.184177e+05,  3.984177e+05,  4.784177e+05,
        5.584177e+05,  6.384177e+05,  7.184177e+05,  7.984177e+05,
        8.784177e+05,  9.584177e+05,  1.038418e+06,  1.118418e+06,
        1.198418e+06,  1.278418e+06,  1.358418e+06,  1.438418e+06,
        1.518418e+06,  1.598418e+06,  1.678418e+06,  1.758418e+06,
        1.838418e+06,  1.918418e+06,  1.998418e+06,  2.078418e+06,
        2.158418e+06,  2.238418e+06,  2.318418e+06])</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>season</span></div><div class='xr-var-dims'>(season)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>&#x27;DJF&#x27; &#x27;JJA&#x27; &#x27;MAM&#x27; &#x27;SON&#x27;</div><input id='attrs-64d6b658-063b-45ad-b514-0ec5dbeaf350' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-64d6b658-063b-45ad-b514-0ec5dbeaf350' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-f8521d14-4427-4acc-9023-7321a115445e' class='xr-var-data-in' type='checkbox'><label for='data-f8521d14-4427-4acc-9023-7321a115445e' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;DJF&#x27;, &#x27;JJA&#x27;, &#x27;MAM&#x27;, &#x27;SON&#x27;], dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-f06ecbc6-e448-420a-8b16-3b62124da787' class='xr-section-summary-in' type='checkbox'  checked><label for='section-f06ecbc6-e448-420a-8b16-3b62124da787' class='xr-section-summary' >Data variables: <span>(3)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>40_dbz_count</span></div><div class='xr-var-dims'>(season, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;</div><input id='attrs-d01929e8-4f5b-407f-b087-f00bbb264d80' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-d01929e8-4f5b-407f-b087-f00bbb264d80' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-505b4efd-b89d-4190-847a-0802e2ddc403' class='xr-var-data-in' type='checkbox'><label for='data-505b4efd-b89d-4190-847a-0802e2ddc403' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 70.06 kiB </td>
                        <td> 17.52 kiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (4, 38, 59) </td>
                        <td> (1, 38, 59) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 448 Tasks </td>
                        <td> 4 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="201" height="148" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="31" y2="21" style="stroke-width:2" />
  <line x1="10" y1="77" x2="31" y2="98" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="77" style="stroke-width:2" />
  <line x1="15" y1="5" x2="15" y2="82" />
  <line x1="20" y1="10" x2="20" y2="87" />
  <line x1="26" y1="16" x2="26" y2="93" />
  <line x1="31" y1="21" x2="31" y2="98" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 31.381452134199485,21.381452134199485 31.381452134199485,98.66958772741984 10.0,77.28813559322035" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="130" y2="0" style="stroke-width:2" />
  <line x1="15" y1="5" x2="135" y2="5" />
  <line x1="20" y1="10" x2="140" y2="10" />
  <line x1="26" y1="16" x2="146" y2="16" />
  <line x1="31" y1="21" x2="151" y2="21" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="31" y2="21" style="stroke-width:2" />
  <line x1="130" y1="0" x2="151" y2="21" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 130.0,0.0 151.3814521341995,21.381452134199485 31.381452134199485,21.381452134199485" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="31" y1="21" x2="151" y2="21" style="stroke-width:2" />
  <line x1="31" y1="98" x2="151" y2="98" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="31" y1="21" x2="31" y2="98" style="stroke-width:2" />
  <line x1="151" y1="21" x2="151" y2="98" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="31.381452134199485,21.381452134199485 151.3814521341995,21.381452134199485 151.3814521341995,98.66958772741984 31.381452134199485,98.66958772741984" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="91.381452" y="118.669588" font-size="1.0rem" font-weight="100" text-anchor="middle" >59</text>
  <text x="171.381452" y="60.025520" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,171.381452,60.025520)">38</text>
  <text x="10.690726" y="107.978862" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,10.690726,107.978862)">4</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>50_dbz_count</span></div><div class='xr-var-dims'>(season, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;</div><input id='attrs-1252d0f8-abde-4d9e-a93c-10edb4390234' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-1252d0f8-abde-4d9e-a93c-10edb4390234' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-83bee5a9-f82f-437e-ba36-f092d482734a' class='xr-var-data-in' type='checkbox'><label for='data-83bee5a9-f82f-437e-ba36-f092d482734a' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 70.06 kiB </td>
                        <td> 17.52 kiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (4, 38, 59) </td>
                        <td> (1, 38, 59) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 448 Tasks </td>
                        <td> 4 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="201" height="148" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="31" y2="21" style="stroke-width:2" />
  <line x1="10" y1="77" x2="31" y2="98" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="77" style="stroke-width:2" />
  <line x1="15" y1="5" x2="15" y2="82" />
  <line x1="20" y1="10" x2="20" y2="87" />
  <line x1="26" y1="16" x2="26" y2="93" />
  <line x1="31" y1="21" x2="31" y2="98" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 31.381452134199485,21.381452134199485 31.381452134199485,98.66958772741984 10.0,77.28813559322035" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="130" y2="0" style="stroke-width:2" />
  <line x1="15" y1="5" x2="135" y2="5" />
  <line x1="20" y1="10" x2="140" y2="10" />
  <line x1="26" y1="16" x2="146" y2="16" />
  <line x1="31" y1="21" x2="151" y2="21" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="31" y2="21" style="stroke-width:2" />
  <line x1="130" y1="0" x2="151" y2="21" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 130.0,0.0 151.3814521341995,21.381452134199485 31.381452134199485,21.381452134199485" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="31" y1="21" x2="151" y2="21" style="stroke-width:2" />
  <line x1="31" y1="98" x2="151" y2="98" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="31" y1="21" x2="31" y2="98" style="stroke-width:2" />
  <line x1="151" y1="21" x2="151" y2="98" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="31.381452134199485,21.381452134199485 151.3814521341995,21.381452134199485 151.3814521341995,98.66958772741984 31.381452134199485,98.66958772741984" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="91.381452" y="118.669588" font-size="1.0rem" font-weight="100" text-anchor="middle" >59</text>
  <text x="171.381452" y="60.025520" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,171.381452,60.025520)">38</text>
  <text x="10.690726" y="107.978862" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,10.690726,107.978862)">4</text>
</svg>
        </td>
    </tr>
</table></div></li><li class='xr-var-item'><div class='xr-var-name'><span>60_dbz_count</span></div><div class='xr-var-dims'>(season, y, x)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>dask.array&lt;chunksize=(1, 38, 59), meta=np.ndarray&gt;</div><input id='attrs-584833b8-66c3-4af5-93a9-d0ada0b1f27b' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-584833b8-66c3-4af5-93a9-d0ada0b1f27b' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-c55384f2-4a0e-4ea1-9ae8-b318d45baca3' class='xr-var-data-in' type='checkbox'><label for='data-c55384f2-4a0e-4ea1-9ae8-b318d45baca3' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><table>
    <tr>
        <td>
            <table>
                <thead>
                    <tr>
                        <td> </td>
                        <th> Array </th>
                        <th> Chunk </th>
                    </tr>
                </thead>
                <tbody>

                    <tr>
                        <th> Bytes </th>
                        <td> 70.06 kiB </td>
                        <td> 17.52 kiB </td>
                    </tr>

                    <tr>
                        <th> Shape </th>
                        <td> (4, 38, 59) </td>
                        <td> (1, 38, 59) </td>
                    </tr>
                    <tr>
                        <th> Count </th>
                        <td> 448 Tasks </td>
                        <td> 4 Chunks </td>
                    </tr>
                    <tr>
                    <th> Type </th>
                    <td> float64 </td>
                    <td> numpy.ndarray </td>
                    </tr>
                </tbody>
            </table>
        </td>
        <td>
        <svg width="201" height="148" style="stroke:rgb(0,0,0);stroke-width:1" >

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="31" y2="21" style="stroke-width:2" />
  <line x1="10" y1="77" x2="31" y2="98" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="10" y2="77" style="stroke-width:2" />
  <line x1="15" y1="5" x2="15" y2="82" />
  <line x1="20" y1="10" x2="20" y2="87" />
  <line x1="26" y1="16" x2="26" y2="93" />
  <line x1="31" y1="21" x2="31" y2="98" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 31.381452134199485,21.381452134199485 31.381452134199485,98.66958772741984 10.0,77.28813559322035" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="10" y1="0" x2="130" y2="0" style="stroke-width:2" />
  <line x1="15" y1="5" x2="135" y2="5" />
  <line x1="20" y1="10" x2="140" y2="10" />
  <line x1="26" y1="16" x2="146" y2="16" />
  <line x1="31" y1="21" x2="151" y2="21" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="10" y1="0" x2="31" y2="21" style="stroke-width:2" />
  <line x1="130" y1="0" x2="151" y2="21" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="10.0,0.0 130.0,0.0 151.3814521341995,21.381452134199485 31.381452134199485,21.381452134199485" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Horizontal lines -->
  <line x1="31" y1="21" x2="151" y2="21" style="stroke-width:2" />
  <line x1="31" y1="98" x2="151" y2="98" style="stroke-width:2" />

  <!-- Vertical lines -->
  <line x1="31" y1="21" x2="31" y2="98" style="stroke-width:2" />
  <line x1="151" y1="21" x2="151" y2="98" style="stroke-width:2" />

  <!-- Colored Rectangle -->
  <polygon points="31.381452134199485,21.381452134199485 151.3814521341995,21.381452134199485 151.3814521341995,98.66958772741984 31.381452134199485,98.66958772741984" style="fill:#ECB172A0;stroke-width:0"/>

  <!-- Text -->
  <text x="91.381452" y="118.669588" font-size="1.0rem" font-weight="100" text-anchor="middle" >59</text>
  <text x="171.381452" y="60.025520" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(0,171.381452,60.025520)">38</text>
  <text x="10.690726" y="107.978862" font-size="1.0rem" font-weight="100" text-anchor="middle" transform="rotate(45,10.690726,107.978862)">4</text>
</svg>
        </td>
    </tr>
</table></div></li></ul></div></li><li class='xr-section-item'><input id='section-1b0f295c-d239-4159-8a6d-5837696843eb' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-1b0f295c-d239-4159-8a6d-5837696843eb' class='xr-section-summary'  title='Expand/collapse section'>Attributes: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'></dl></div></li></ul></div></div>



# Geographic data

### These data define the grids used for CAPE/CIN


```python
import xarray as xr

ds = xr.open_dataset("../data/geog/geog_sim.nc")

ds
```




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block !important;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt;
Dimensions:  (Time: 1, south_north: 899, west_east: 1399)
Dimensions without coordinates: Time, south_north, west_east
Data variables:
    CLONG    (Time, south_north, west_east) float32 ...
    CLAT     (Time, south_north, west_east) float32 ...
Attributes: (12/55)
    TITLE:                           OUTPUT FROM GEOGRID V4.1
    SIMULATION_START_DATE:           0000-00-00_00:00:00
    WEST-EAST_GRID_DIMENSION:        1400
    SOUTH-NORTH_GRID_DIMENSION:      900
    BOTTOM-TOP_GRID_DIMENSION:       0
    WEST-EAST_PATCH_START_UNSTAG:    1
    ...                              ...
    FLAG_FRC_URB2D:                  1
    FLAG_IMPERV:                     1
    FLAG_CANFRA:                     1
    FLAG_EROD:                       1
    FLAG_CLAYFRAC:                   1
    FLAG_SANDFRAC:                   1</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-0e57c91c-9761-457e-977d-448d2e1038c7' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-0e57c91c-9761-457e-977d-448d2e1038c7' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span>Time</span>: 1</li><li><span>south_north</span>: 899</li><li><span>west_east</span>: 1399</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-9fee432b-62e5-4e05-bed7-765a7264548c' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-9fee432b-62e5-4e05-bed7-765a7264548c' class='xr-section-summary'  title='Expand/collapse section'>Coordinates: <span>(0)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'></ul></div></li><li class='xr-section-item'><input id='section-ce4eaef1-8555-409c-8cf2-11709370c513' class='xr-section-summary-in' type='checkbox'  checked><label for='section-ce4eaef1-8555-409c-8cf2-11709370c513' class='xr-section-summary' >Data variables: <span>(2)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>CLONG</span></div><div class='xr-var-dims'>(Time, south_north, west_east)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-a78fbe95-8e43-4e45-b26e-f01a40b5fd01' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-a78fbe95-8e43-4e45-b26e-f01a40b5fd01' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-88ed3a66-b33b-4ee2-b514-b5cb1276a585' class='xr-var-data-in' type='checkbox'><label for='data-88ed3a66-b33b-4ee2-b514-b5cb1276a585' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>FieldType :</span></dt><dd>104</dd><dt><span>MemoryOrder :</span></dt><dd>XY </dd><dt><span>units :</span></dt><dd>degrees longitude</dd><dt><span>description :</span></dt><dd>Computational longitude on mass grid</dd><dt><span>stagger :</span></dt><dd>M</dd><dt><span>sr_x :</span></dt><dd>1</dd><dt><span>sr_y :</span></dt><dd>1</dd></dl></div><div class='xr-var-data'><pre>[1257701 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>CLAT</span></div><div class='xr-var-dims'>(Time, south_north, west_east)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-b739bd22-5212-4c86-b218-002108a3c5db' class='xr-var-attrs-in' type='checkbox' ><label for='attrs-b739bd22-5212-4c86-b218-002108a3c5db' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-6cfb85aa-567b-4eb5-a321-a04326a2b2d8' class='xr-var-data-in' type='checkbox'><label for='data-6cfb85aa-567b-4eb5-a321-a04326a2b2d8' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'><dt><span>FieldType :</span></dt><dd>104</dd><dt><span>MemoryOrder :</span></dt><dd>XY </dd><dt><span>units :</span></dt><dd>degrees latitude</dd><dt><span>description :</span></dt><dd>Computational latitude on mass grid</dd><dt><span>stagger :</span></dt><dd>M</dd><dt><span>sr_x :</span></dt><dd>1</dd><dt><span>sr_y :</span></dt><dd>1</dd></dl></div><div class='xr-var-data'><pre>[1257701 values with dtype=float32]</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-3332a642-8c6f-4cf0-88a0-c6d58fb0f463' class='xr-section-summary-in' type='checkbox'  ><label for='section-3332a642-8c6f-4cf0-88a0-c6d58fb0f463' class='xr-section-summary' >Attributes: <span>(55)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>TITLE :</span></dt><dd>OUTPUT FROM GEOGRID V4.1</dd><dt><span>SIMULATION_START_DATE :</span></dt><dd>0000-00-00_00:00:00</dd><dt><span>WEST-EAST_GRID_DIMENSION :</span></dt><dd>1400</dd><dt><span>SOUTH-NORTH_GRID_DIMENSION :</span></dt><dd>900</dd><dt><span>BOTTOM-TOP_GRID_DIMENSION :</span></dt><dd>0</dd><dt><span>WEST-EAST_PATCH_START_UNSTAG :</span></dt><dd>1</dd><dt><span>WEST-EAST_PATCH_END_UNSTAG :</span></dt><dd>1399</dd><dt><span>WEST-EAST_PATCH_START_STAG :</span></dt><dd>1</dd><dt><span>WEST-EAST_PATCH_END_STAG :</span></dt><dd>1400</dd><dt><span>SOUTH-NORTH_PATCH_START_UNSTAG :</span></dt><dd>1</dd><dt><span>SOUTH-NORTH_PATCH_END_UNSTAG :</span></dt><dd>899</dd><dt><span>SOUTH-NORTH_PATCH_START_STAG :</span></dt><dd>1</dd><dt><span>SOUTH-NORTH_PATCH_END_STAG :</span></dt><dd>900</dd><dt><span>GRIDTYPE :</span></dt><dd>C</dd><dt><span>DX :</span></dt><dd>3750.0</dd><dt><span>DY :</span></dt><dd>3750.0</dd><dt><span>DYN_OPT :</span></dt><dd>2</dd><dt><span>CEN_LAT :</span></dt><dd>38.500004</dd><dt><span>CEN_LON :</span></dt><dd>-97.5</dd><dt><span>TRUELAT1 :</span></dt><dd>38.5</dd><dt><span>TRUELAT2 :</span></dt><dd>38.5</dd><dt><span>MOAD_CEN_LAT :</span></dt><dd>38.500004</dd><dt><span>STAND_LON :</span></dt><dd>-97.5</dd><dt><span>POLE_LAT :</span></dt><dd>90.0</dd><dt><span>POLE_LON :</span></dt><dd>0.0</dd><dt><span>corner_lats :</span></dt><dd>[20.509216 48.89253  48.89253  20.509216 20.505005 48.88618  48.88618
 20.505005 20.493675 48.90784  48.90784  20.493675 20.48948  48.901493
 48.901493 20.48948 ]</dd><dt><span>corner_lons :</span></dt><dd>[-121.81102  -133.66338   -61.33661   -73.188965 -121.82761  -133.68666
  -61.313354  -73.17239  -121.80653  -133.67303   -61.326965  -73.19348
 -121.82312  -133.69632   -61.30368   -73.17688 ]</dd><dt><span>MAP_PROJ :</span></dt><dd>1</dd><dt><span>MMINLU :</span></dt><dd>MODIFIED_IGBP_MODIS_NOAH</dd><dt><span>NUM_LAND_CAT :</span></dt><dd>21</dd><dt><span>ISWATER :</span></dt><dd>17</dd><dt><span>ISLAKE :</span></dt><dd>21</dd><dt><span>ISICE :</span></dt><dd>15</dd><dt><span>ISURBAN :</span></dt><dd>13</dd><dt><span>ISOILWATER :</span></dt><dd>14</dd><dt><span>grid_id :</span></dt><dd>1</dd><dt><span>parent_id :</span></dt><dd>1</dd><dt><span>i_parent_start :</span></dt><dd>1</dd><dt><span>j_parent_start :</span></dt><dd>1</dd><dt><span>i_parent_end :</span></dt><dd>1400</dd><dt><span>j_parent_end :</span></dt><dd>900</dd><dt><span>parent_grid_ratio :</span></dt><dd>1</dd><dt><span>sr_x :</span></dt><dd>1</dd><dt><span>sr_y :</span></dt><dd>1</dd><dt><span>FLAG_MF_XY :</span></dt><dd>1</dd><dt><span>FLAG_LAI12M :</span></dt><dd>1</dd><dt><span>FLAG_VAR_SSO :</span></dt><dd>1</dd><dt><span>FLAG_LAKE_DEPTH :</span></dt><dd>1</dd><dt><span>FLAG_URB_PARAM :</span></dt><dd>1</dd><dt><span>FLAG_FRC_URB2D :</span></dt><dd>1</dd><dt><span>FLAG_IMPERV :</span></dt><dd>1</dd><dt><span>FLAG_CANFRA :</span></dt><dd>1</dd><dt><span>FLAG_EROD :</span></dt><dd>1</dd><dt><span>FLAG_CLAYFRAC :</span></dt><dd>1</dd><dt><span>FLAG_SANDFRAC :</span></dt><dd>1</dd></dl></div></li></ul></div></div>



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




<div><svg style="position: absolute; width: 0; height: 0; overflow: hidden">
<defs>
<symbol id="icon-database" viewBox="0 0 32 32">
<path d="M16 0c-8.837 0-16 2.239-16 5v4c0 2.761 7.163 5 16 5s16-2.239 16-5v-4c0-2.761-7.163-5-16-5z"></path>
<path d="M16 17c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
<path d="M16 26c-8.837 0-16-2.239-16-5v6c0 2.761 7.163 5 16 5s16-2.239 16-5v-6c0 2.761-7.163 5-16 5z"></path>
</symbol>
<symbol id="icon-file-text2" viewBox="0 0 32 32">
<path d="M28.681 7.159c-0.694-0.947-1.662-2.053-2.724-3.116s-2.169-2.030-3.116-2.724c-1.612-1.182-2.393-1.319-2.841-1.319h-15.5c-1.378 0-2.5 1.121-2.5 2.5v27c0 1.378 1.122 2.5 2.5 2.5h23c1.378 0 2.5-1.122 2.5-2.5v-19.5c0-0.448-0.137-1.23-1.319-2.841zM24.543 5.457c0.959 0.959 1.712 1.825 2.268 2.543h-4.811v-4.811c0.718 0.556 1.584 1.309 2.543 2.268zM28 29.5c0 0.271-0.229 0.5-0.5 0.5h-23c-0.271 0-0.5-0.229-0.5-0.5v-27c0-0.271 0.229-0.5 0.5-0.5 0 0 15.499-0 15.5 0v7c0 0.552 0.448 1 1 1h7v19.5z"></path>
<path d="M23 26h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 22h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
<path d="M23 18h-14c-0.552 0-1-0.448-1-1s0.448-1 1-1h14c0.552 0 1 0.448 1 1s-0.448 1-1 1z"></path>
</symbol>
</defs>
</svg>
<style>/* CSS stylesheet for displaying xarray objects in jupyterlab.
 *
 */

:root {
  --xr-font-color0: var(--jp-content-font-color0, rgba(0, 0, 0, 1));
  --xr-font-color2: var(--jp-content-font-color2, rgba(0, 0, 0, 0.54));
  --xr-font-color3: var(--jp-content-font-color3, rgba(0, 0, 0, 0.38));
  --xr-border-color: var(--jp-border-color2, #e0e0e0);
  --xr-disabled-color: var(--jp-layout-color3, #bdbdbd);
  --xr-background-color: var(--jp-layout-color0, white);
  --xr-background-color-row-even: var(--jp-layout-color1, white);
  --xr-background-color-row-odd: var(--jp-layout-color2, #eeeeee);
}

html[theme=dark],
body.vscode-dark {
  --xr-font-color0: rgba(255, 255, 255, 1);
  --xr-font-color2: rgba(255, 255, 255, 0.54);
  --xr-font-color3: rgba(255, 255, 255, 0.38);
  --xr-border-color: #1F1F1F;
  --xr-disabled-color: #515151;
  --xr-background-color: #111111;
  --xr-background-color-row-even: #111111;
  --xr-background-color-row-odd: #313131;
}

.xr-wrap {
  display: block !important;
  min-width: 300px;
  max-width: 700px;
}

.xr-text-repr-fallback {
  /* fallback to plain text repr when CSS is not injected (untrusted notebook) */
  display: none;
}

.xr-header {
  padding-top: 6px;
  padding-bottom: 6px;
  margin-bottom: 4px;
  border-bottom: solid 1px var(--xr-border-color);
}

.xr-header > div,
.xr-header > ul {
  display: inline;
  margin-top: 0;
  margin-bottom: 0;
}

.xr-obj-type,
.xr-array-name {
  margin-left: 2px;
  margin-right: 10px;
}

.xr-obj-type {
  color: var(--xr-font-color2);
}

.xr-sections {
  padding-left: 0 !important;
  display: grid;
  grid-template-columns: 150px auto auto 1fr 20px 20px;
}

.xr-section-item {
  display: contents;
}

.xr-section-item input {
  display: none;
}

.xr-section-item input + label {
  color: var(--xr-disabled-color);
}

.xr-section-item input:enabled + label {
  cursor: pointer;
  color: var(--xr-font-color2);
}

.xr-section-item input:enabled + label:hover {
  color: var(--xr-font-color0);
}

.xr-section-summary {
  grid-column: 1;
  color: var(--xr-font-color2);
  font-weight: 500;
}

.xr-section-summary > span {
  display: inline-block;
  padding-left: 0.5em;
}

.xr-section-summary-in:disabled + label {
  color: var(--xr-font-color2);
}

.xr-section-summary-in + label:before {
  display: inline-block;
  content: '►';
  font-size: 11px;
  width: 15px;
  text-align: center;
}

.xr-section-summary-in:disabled + label:before {
  color: var(--xr-disabled-color);
}

.xr-section-summary-in:checked + label:before {
  content: '▼';
}

.xr-section-summary-in:checked + label > span {
  display: none;
}

.xr-section-summary,
.xr-section-inline-details {
  padding-top: 4px;
  padding-bottom: 4px;
}

.xr-section-inline-details {
  grid-column: 2 / -1;
}

.xr-section-details {
  display: none;
  grid-column: 1 / -1;
  margin-bottom: 5px;
}

.xr-section-summary-in:checked ~ .xr-section-details {
  display: contents;
}

.xr-array-wrap {
  grid-column: 1 / -1;
  display: grid;
  grid-template-columns: 20px auto;
}

.xr-array-wrap > label {
  grid-column: 1;
  vertical-align: top;
}

.xr-preview {
  color: var(--xr-font-color3);
}

.xr-array-preview,
.xr-array-data {
  padding: 0 5px !important;
  grid-column: 2;
}

.xr-array-data,
.xr-array-in:checked ~ .xr-array-preview {
  display: none;
}

.xr-array-in:checked ~ .xr-array-data,
.xr-array-preview {
  display: inline-block;
}

.xr-dim-list {
  display: inline-block !important;
  list-style: none;
  padding: 0 !important;
  margin: 0;
}

.xr-dim-list li {
  display: inline-block;
  padding: 0;
  margin: 0;
}

.xr-dim-list:before {
  content: '(';
}

.xr-dim-list:after {
  content: ')';
}

.xr-dim-list li:not(:last-child):after {
  content: ',';
  padding-right: 5px;
}

.xr-has-index {
  font-weight: bold;
}

.xr-var-list,
.xr-var-item {
  display: contents;
}

.xr-var-item > div,
.xr-var-item label,
.xr-var-item > .xr-var-name span {
  background-color: var(--xr-background-color-row-even);
  margin-bottom: 0;
}

.xr-var-item > .xr-var-name:hover span {
  padding-right: 5px;
}

.xr-var-list > li:nth-child(odd) > div,
.xr-var-list > li:nth-child(odd) > label,
.xr-var-list > li:nth-child(odd) > .xr-var-name span {
  background-color: var(--xr-background-color-row-odd);
}

.xr-var-name {
  grid-column: 1;
}

.xr-var-dims {
  grid-column: 2;
}

.xr-var-dtype {
  grid-column: 3;
  text-align: right;
  color: var(--xr-font-color2);
}

.xr-var-preview {
  grid-column: 4;
}

.xr-var-name,
.xr-var-dims,
.xr-var-dtype,
.xr-preview,
.xr-attrs dt {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  padding-right: 10px;
}

.xr-var-name:hover,
.xr-var-dims:hover,
.xr-var-dtype:hover,
.xr-attrs dt:hover {
  overflow: visible;
  width: auto;
  z-index: 1;
}

.xr-var-attrs,
.xr-var-data {
  display: none;
  background-color: var(--xr-background-color) !important;
  padding-bottom: 5px !important;
}

.xr-var-attrs-in:checked ~ .xr-var-attrs,
.xr-var-data-in:checked ~ .xr-var-data {
  display: block;
}

.xr-var-data > table {
  float: right;
}

.xr-var-name span,
.xr-var-data,
.xr-attrs {
  padding-left: 25px !important;
}

.xr-attrs,
.xr-var-attrs,
.xr-var-data {
  grid-column: 1 / -1;
}

dl.xr-attrs {
  padding: 0;
  margin: 0;
  display: grid;
  grid-template-columns: 125px auto;
}

.xr-attrs dt,
.xr-attrs dd {
  padding: 0;
  margin: 0;
  float: left;
  padding-right: 10px;
  width: auto;
}

.xr-attrs dt {
  font-weight: normal;
  grid-column: 1;
}

.xr-attrs dt:hover span {
  display: inline-block;
  background: var(--xr-background-color);
  padding-right: 10px;
}

.xr-attrs dd {
  grid-column: 2;
  white-space: pre-wrap;
  word-break: break-all;
}

.xr-icon-database,
.xr-icon-file-text2 {
  display: inline-block;
  vertical-align: middle;
  width: 1em;
  height: 1.5em !important;
  stroke-width: 0;
  stroke: currentColor;
  fill: currentColor;
}
</style><pre class='xr-text-repr-fallback'>&lt;xarray.Dataset&gt;
Dimensions:       (season: 4, south_north: 899, west_east: 1399)
Coordinates:
  * season        (season) object &#x27;DJF&#x27; &#x27;JJA&#x27; &#x27;MAM&#x27; &#x27;SON&#x27;
Dimensions without coordinates: south_north, west_east
Data variables:
    AFWA_CAPE_MU  (season, south_north, west_east) float32 ...
    AFWA_CIN_MU   (season, south_north, west_east) float64 ...
Attributes: (12/17)
    TITLE:                        OUTPUT FROM WRF V4.1.2 MODEL
    WEST-EAST_GRID_DIMENSION:    1400
    SOUTH-NORTH_GRID_DIMENSION:  900
    DX:                          3750.0
    DY:                          3750.0
    DT:                          20.0
    ...                          ...
    STAND_LON:                   -97.5
    POLE_LAT:                    90.0
    POLE_LON:                    0.0
    MAP_PROJ:                    1
    MAP_PROJ_CHAR:               Lambert Conformal
    description:                 Mean seasonal MU CAPE and MU CIN, Retrospect...</pre><div class='xr-wrap' style='display:none'><div class='xr-header'><div class='xr-obj-type'>xarray.Dataset</div></div><ul class='xr-sections'><li class='xr-section-item'><input id='section-20e31277-6820-49d7-a9fe-118882cde7b0' class='xr-section-summary-in' type='checkbox' disabled ><label for='section-20e31277-6820-49d7-a9fe-118882cde7b0' class='xr-section-summary'  title='Expand/collapse section'>Dimensions:</label><div class='xr-section-inline-details'><ul class='xr-dim-list'><li><span class='xr-has-index'>season</span>: 4</li><li><span>south_north</span>: 899</li><li><span>west_east</span>: 1399</li></ul></div><div class='xr-section-details'></div></li><li class='xr-section-item'><input id='section-def44c41-aa24-4d6b-b26b-8e36f9c03d28' class='xr-section-summary-in' type='checkbox'  checked><label for='section-def44c41-aa24-4d6b-b26b-8e36f9c03d28' class='xr-section-summary' >Coordinates: <span>(1)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span class='xr-has-index'>season</span></div><div class='xr-var-dims'>(season)</div><div class='xr-var-dtype'>object</div><div class='xr-var-preview xr-preview'>&#x27;DJF&#x27; &#x27;JJA&#x27; &#x27;MAM&#x27; &#x27;SON&#x27;</div><input id='attrs-17934b14-efe0-47d5-bfa8-71b98902d12a' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-17934b14-efe0-47d5-bfa8-71b98902d12a' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-3104cba1-a021-4a68-92dc-56f89ded5737' class='xr-var-data-in' type='checkbox'><label for='data-3104cba1-a021-4a68-92dc-56f89ded5737' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>array([&#x27;DJF&#x27;, &#x27;JJA&#x27;, &#x27;MAM&#x27;, &#x27;SON&#x27;], dtype=object)</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-a8fad87f-140c-4eaa-980c-edda7227e9d0' class='xr-section-summary-in' type='checkbox'  checked><label for='section-a8fad87f-140c-4eaa-980c-edda7227e9d0' class='xr-section-summary' >Data variables: <span>(2)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><ul class='xr-var-list'><li class='xr-var-item'><div class='xr-var-name'><span>AFWA_CAPE_MU</span></div><div class='xr-var-dims'>(season, south_north, west_east)</div><div class='xr-var-dtype'>float32</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-16cc47af-ca18-4340-826b-713f7e64f766' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-16cc47af-ca18-4340-826b-713f7e64f766' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-dd72c858-8611-4f4c-a262-e231a1608e6e' class='xr-var-data-in' type='checkbox'><label for='data-dd72c858-8611-4f4c-a262-e231a1608e6e' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>[5030804 values with dtype=float32]</pre></div></li><li class='xr-var-item'><div class='xr-var-name'><span>AFWA_CIN_MU</span></div><div class='xr-var-dims'>(season, south_north, west_east)</div><div class='xr-var-dtype'>float64</div><div class='xr-var-preview xr-preview'>...</div><input id='attrs-e17873cd-22e5-4e52-96ab-438127ca4eb7' class='xr-var-attrs-in' type='checkbox' disabled><label for='attrs-e17873cd-22e5-4e52-96ab-438127ca4eb7' title='Show/Hide attributes'><svg class='icon xr-icon-file-text2'><use xlink:href='#icon-file-text2'></use></svg></label><input id='data-20d2278a-7d45-451c-bfbb-c3505b05391b' class='xr-var-data-in' type='checkbox'><label for='data-20d2278a-7d45-451c-bfbb-c3505b05391b' title='Show/Hide data repr'><svg class='icon xr-icon-database'><use xlink:href='#icon-database'></use></svg></label><div class='xr-var-attrs'><dl class='xr-attrs'></dl></div><div class='xr-var-data'><pre>[5030804 values with dtype=float64]</pre></div></li></ul></div></li><li class='xr-section-item'><input id='section-5b1b1237-d8d6-458f-8b40-6ed842c5d8ec' class='xr-section-summary-in' type='checkbox'  ><label for='section-5b1b1237-d8d6-458f-8b40-6ed842c5d8ec' class='xr-section-summary' >Attributes: <span>(17)</span></label><div class='xr-section-inline-details'></div><div class='xr-section-details'><dl class='xr-attrs'><dt><span>TITLE :</span></dt><dd> OUTPUT FROM WRF V4.1.2 MODEL</dd><dt><span>WEST-EAST_GRID_DIMENSION :</span></dt><dd>1400</dd><dt><span>SOUTH-NORTH_GRID_DIMENSION :</span></dt><dd>900</dd><dt><span>DX :</span></dt><dd>3750.0</dd><dt><span>DY :</span></dt><dd>3750.0</dd><dt><span>DT :</span></dt><dd>20.0</dd><dt><span>CEN_LAT :</span></dt><dd>38.500004</dd><dt><span>CEN_LON :</span></dt><dd>-97.5</dd><dt><span>TRUELAT1 :</span></dt><dd>38.5</dd><dt><span>TRUELAT2 :</span></dt><dd>38.5</dd><dt><span>MOAD_CEN_LAT :</span></dt><dd>38.500004</dd><dt><span>STAND_LON :</span></dt><dd>-97.5</dd><dt><span>POLE_LAT :</span></dt><dd>90.0</dd><dt><span>POLE_LON :</span></dt><dd>0.0</dd><dt><span>MAP_PROJ :</span></dt><dd>1</dd><dt><span>MAP_PROJ_CHAR :</span></dt><dd>Lambert Conformal</dd><dt><span>description :</span></dt><dd>Mean seasonal MU CAPE and MU CIN, Retrospective (1990-2005)</dd></dl></div></li></ul></div></div>




```python

```
