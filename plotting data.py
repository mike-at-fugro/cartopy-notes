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