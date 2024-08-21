"""
    Plotting Data

"""
import warnings
import matplotlib.pyplot as plt
import numpy as np
from cartopy import crs as ccrs, feature as cfeature

# Suppress warnings when downloading data files
warnings.filterwarnings("ignore")

"""
    creating a lat-lon grid and defining some data on it
"""
lon, lat = np.mgrid[-180:181, -90:91]
data = 2 * np.sin(3 * np.deg2rad(lon)) + 3 * np.cos(4 * np.deg2rad(lat))

plt.contourf(lon, lat, data)
plt.colorbar()
plt.show()

"""
    Using a Cartesian grid is the equivalent to PlateCarree projection

    Once map is created, data values can be plotted as a contour map.
    Use transform() contour plotting method to specify projection type in current use.
    This will transform the specified projection type to the type specified in the subplot() method.

    example: plot using Mollweide projection to see how shapes change under a transformation
"""
proj_Moll = ccrs.Mollweide(central_longitude=0)

fig = plt.figure(figsize=(11, 8.5))
ax = plt.subplot(1,1,1, projection=proj_Moll)

ax.coastlines()

data_plot = ax.contourf(lon, lat, data, transform=ccrs.PlateCarree())

plt.colorbar(data_plot, orientation="horizontal")

plt.show()