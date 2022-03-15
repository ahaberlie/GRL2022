import numpy as np
import geopandas as gpd

from shapely.geometry import Point, box
from scipy.interpolate import griddata
from scipy.stats import mannwhitneyu


def grid_significance(field1, field2):
    results = np.ones(shape=(field1.shape[1], field1.shape[2]), dtype=float)
    for i in range(field1.shape[1]):
        for j in range(field1.shape[2]):

            dist1 = field1[:, i, j]
            dist2 = field2[:, i, j]

            try:
                s, p = mannwhitneyu(dist1, dist2)
                results[i, j] = p
            except Exception as e:
                print(e)
                results[i, j] = np.nan

    return results

def generate_grids(extent, grid_spacing, proj_code, returnxy=False):
    r"""Generates a GeoDataFrame containing a uniform
    grid with dimensions of grid_spacing x grid_spaceing
    with the same bounds as 'extent'.  It is assumed that
    'extent' and 'grid_spacing' have the same crs as
    'proj_code'.  This will fail or produce unexpected
    results if that is not true.

    Parameters
    ----------
    extent: GeoDataFrame
        GeogDataFrame (from shapefile or similar) defining the
        spatial extent of the grid.
    grid_spacing: int
        Desired x and y dimensions of the grid.
    proj_code: str
        Either a predefined Proj code, or custom projection.
    returnxy: bool
        If true, return the grid cell centers used to generate
        the grid. Default is false.

    Returns
    -------
    grid: GeoDataFrame
        The generated grids.
    x_: ndarray (optional)
        X-coordinates of grid centers
    y_: ndarray (optional)
        Y-coordinates of grid centers
    """

    xmin, ymin, xmax, ymax = extent.total_bounds

    grid_cells = []

    x_ = np.arange(xmin, xmax + grid_spacing, grid_spacing)
    y_ = np.arange(ymin, ymax + grid_spacing, grid_spacing)

    for x0 in x_:

        for y0 in y_:
            x1 = x0 + grid_spacing

            y1 = y0 + grid_spacing

            grid_cells.append(box(x0, y0, x1, y1))

    grid = gpd.GeoDataFrame(grid_cells, columns=['geometry'], crs=proj_code)

    if returnxy:
        return grid, x_ + (grid_spacing / 2), y_ + (grid_spacing / 2)

    else:
        return grid


def generate_points(x, y, in_crs, out_crs):
    r"""Generates points from a given list of x and y
    coordinates, defines a projection as in_crs, and projects
    the points to out_crs

    Parameters
    ----------
    extent: GeoDataFrame
        GeogDataFrame (from shapefile or similar) defining the
        spatial extent of the grid.
    grid_spacing: int
        Desired x and y dimensions of the grid.
    proj_code: str
        Either a predefined Proj code, or custom projection.

    Returns
    -------
    points: GeoDataFrame
        The generated points.
    """

    geoms = [Point(x_, y_) for x_, y_ in zip(x, y)]

    points = gpd.GeoDataFrame(geoms, columns=['geometry'], crs=in_crs)

    points = points.to_crs(out_crs)

    return points


def generate_count(grid, point, no_match_nan=False):
    r"""Returns how many points are in each grid cell in
    the form of a new GeoDataFrame with a 'count' column.

    Parameters
    ----------
    grid: GeoDataFrame
        Grid on which to add a count
    points: GeoDataFrame
        Points to join to grid to get a count per grid
    no_match_nan: bool
        If true, NaN cells (no matches) set to 0.
        Default False

    Returns
    -------
    grid: GeoDataFrame
        A modified grid with a count column.
    """

    join_grid = gpd.sjoin(point, grid)

    count = join_grid.groupby('index_right').count()

    count['count'] = count['geometry']
    count = count[['count']]

    grid_ = grid.join(count)

    if len(join_grid) > 0:

        if no_match_nan:
            grid_.fillna(0, inplace=True)

    else:

        grid_['count'] = 0

    return grid_


def generate_raster(xc, yc, gdf, from_crs=None, to_crs=None):
    gx, gy = np.meshgrid(xc, yc)

    to_pts = np.stack([gx.ravel(), gy.ravel()], axis=1)

    geom_x = gdf.geometry.centroid.x
    geom_y = gdf.geometry.centroid.y

    from_pts = np.array(list(zip(geom_x, geom_y)))

    out = griddata(from_pts, gdf['count'].values, to_pts, method='nearest')

    out = out.reshape(gx.shape)

    if not from_crs is None or to_crs is None:

        gridx, gridy = transform_points(to_pts[:, 0], to_pts[:, 1], from_crs, to_crs)

        gridx = gridx.reshape(gx.shape)
        gridy = gridy.reshape(gx.shape)

        return out, gridx, gridy

    else:

        return out


def transform_points(x_, y_, from_crs, to_crs):
    pts = [Point(x, y) for x, y in zip(x_, y_)]

    gdf_ = gpd.GeoDataFrame(pts, columns=['geometry'], crs=from_crs)

    gdf_ = gdf_.to_crs(to_crs)

    gx, gy = gdf_.geometry.x.values, gdf_.geometry.y.values

    return gx, gy


def get_grid_mesh(x, y):

    gx, gy = np.meshgrid(x, y)

    shapex = gx.shape

    pts = np.stack([gx.ravel(), gy.ravel()], axis=1)

    gx, gy = transform_points(pts[:, 0], pts[:, 1], from_crs='ESRI:102003', to_crs='EPSG:4269')

    gx = gx.reshape(shapex)
    gy = gy.reshape(shapex)

    return gx, gy


def generate_regions(all_grids):

    city_loc = {'ama': (-101.8313, 35.2220),
                'mph': (-90.0490, 35.3),
                'mnp': (-93.2650, 44.7)}

    sel_grids = {}

    for city, point in city_loc.items():
        pt = gpd.GeoDataFrame(data=[Point(point)], columns=['geometry'], crs='EPSG:4269')
        pt = pt.to_crs("ESRI:102003")
        pt.geometry = pt.geometry.buffer(130000)

        sel_grids[city] = gpd.sjoin(all_grids, pt, predicate='intersects')

    sel_grids['ama'] = sel_grids['ama'].to_crs("EPSG:4269")
    sel_grids['mph'] = sel_grids['mph'].to_crs("EPSG:4269")
    sel_grids['mnp'] = sel_grids['mnp'].to_crs("EPSG:4269")

    return sel_grids
