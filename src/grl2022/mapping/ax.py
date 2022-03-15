import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.ticker as mticker
import cartopy.io.shapereader as shpreader
import cartopy.feature as cfeature
import string
letters = string.ascii_lowercase

projection = ccrs.LambertConformal(central_longitude=-96, central_latitude=37.5, standard_parallels=(29.5, 45.5))

extents = {'ECONUS': [-108, -73.5, 22, 49]}

long_range = {'ECONUS': [-110, -100, -90, -80, -70]}


def draw_geography(ax):
        
    countries_shp = shpreader.natural_earth(resolution='50m',
                                     category='cultural',
                                     name='admin_0_countries')
    
    for country, info in zip(shpreader.Reader(countries_shp).geometries(), 
                             shpreader.Reader(countries_shp).records()):
        if info.attributes['NAME_LONG'] != 'United States':

            ax.add_geometries([country], ccrs.PlateCarree(),
                             facecolor='Grey', edgecolor='k', zorder=6)
            
    lakes_shp = shpreader.natural_earth(resolution='50m',
                                     category='physical',
                                     name='lakes')
    
    for lake, info in zip(shpreader.Reader(lakes_shp).geometries(), 
                             shpreader.Reader(lakes_shp).records()):

        name = info.attributes['name']
        if name == 'Lake Superior' or name == 'Lake Michigan' or \
           name == 'Lake Huron' or name == 'Lake Erie' or name == 'Lake Ontario':
            
            ax.add_geometries([lake], ccrs.PlateCarree(),
                              facecolor='lightsteelblue', edgecolor='k', zorder=6)
            
    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'ocean', '50m', edgecolor='face', 
                                                facecolor='lightsteelblue'), zorder=6)

    ax.add_feature(cfeature.NaturalEarthFeature('physical', 'coastline', '50m', edgecolor='face', 
                                                facecolor='None'), zorder=6) 
    
    shapename = 'admin_1_states_provinces_lakes'
    states_shp = shpreader.natural_earth(resolution='50m',
                                     category='cultural', name=shapename)
                                     
    for state, info in zip(shpreader.Reader(states_shp).geometries(), shpreader.Reader(states_shp).records()):
        if info.attributes['admin'] == 'United States of America':

            ax.add_geometries([state], ccrs.PlateCarree(),
                              facecolor='grey', edgecolor='k')
            
    for state, info in zip(shpreader.Reader(states_shp).geometries(), shpreader.Reader(states_shp).records()):
        if info.attributes['admin'] == 'United States of America':

            ax.add_geometries([state], ccrs.PlateCarree(),
                              facecolor='None', edgecolor='k', zorder=6)

    return ax


def setup_map(row_idx, col_idx, rows, cols, extent='ECONUS', longitudes='ECONUS'):
    
    figure_idx = col_idx + (row_idx * 3)
    
    ax = plt.subplot(5, 3, figure_idx + 1, projection=projection)

    ax.set_extent(extents[extent])

    ax = draw_geography(ax)

    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, dms=True, x_inline=False, y_inline=False, zorder=10,
                      color='k', alpha=0.5)

    gl.top_labels = False

    gl.right_labels = False

    gl.xlocator = mticker.FixedLocator(long_range[longitudes])

    gl.xlabel_style = {'size': 20, 'color': 'k', 'rotation': 0.01}
    gl.ylabel_style = {'size': 20, 'color': 'k'}
    
    ax.annotate("{})".format(letters[figure_idx]), (-.06,1), xycoords='axes fraction',
                fontsize=26, bbox=dict(boxstyle='round', facecolor='w', alpha=1), 
                color='k', zorder=25)

    return ax