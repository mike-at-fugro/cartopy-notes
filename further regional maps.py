"""
    Regional map over the Lake District

    in the region:
        top left = 54.469115, -3.162289
        bottom right = 54.172760, -2.692309

        substitute top left: 55.066450, -3.843861

    looks too small for any features :(

"""
import warnings
import matplotlib.pyplot as plt
import numpy as np
from cartopy import crs as ccrs, feature as cfeature

# Suppress warnings when downloading data files
warnings.filterwarnings("ignore")

#define limits
lonW = -3.843861
lonE = -2.692309
latS = 54.172760
latN = 55.066450
cLon = (lonW+lonE)/2
cLat = (latN+latS)/2

proj_PC = ccrs.PlateCarree()
proj_Lambert_LD = ccrs.LambertConformal(central_latitude=cLat, central_longitude=cLon)

fig = plt.figure(figsize=(15,10))
ax = plt.subplot(1,1,1, projection=proj_Lambert_LD)
ax.set_extent([lonW, lonE, latS, latN], crs=proj_PC)
ax.set_title("It's the M@ther F[]k!n' Lakes Boiiiii")

#features
ax.set_facecolor(cfeature.COLORS['water'])
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle='--')
ax.add_feature(cfeature.LAKES, linewidth = 0.5, edgecolor="blue", alpha=0.5)
ax.add_feature(cfeature.RIVERS, linewidth = 0.5, edgecolor="blue")

plt.show()


"""
    Stinky New York

    low resolution

"""
latN = 45.2
latS = 40.2
lonW = -80.0
lonE = -71.5
cLat = (latN + latS) / 2
cLon = (lonW + lonE) / 2
projLccNY = ccrs.LambertConformal(central_longitude=cLon, central_latitude=cLat)
fig = plt.figure(figsize=(15, 10))
ax = plt.subplot(1, 1, 1, projection=projLccNY)
ax.set_extent([lonW, lonE, latS, latN], crs=proj_PC)
ax.set_facecolor(cfeature.COLORS['water'])
ax.add_feature(cfeature.LAND)
ax.add_feature(cfeature.COASTLINE)
ax.add_feature(cfeature.BORDERS, linestyle='--')
ax.add_feature(cfeature.LAKES, alpha=0.5)
ax.add_feature(cfeature.STATES)
ax.add_feature(cfeature.RIVERS)
ax.set_title('New York and Vicinity')
plt.show()