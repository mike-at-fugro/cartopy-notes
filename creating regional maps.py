"""
    Creating Regional Maps using Cartopy

"""
import warnings
import matplotlib.pyplot as plt
import numpy as np
from cartopy import crs as ccrs, feature as cfeature

# Suppress warnings when downloading data files
warnings.filterwarnings("ignore")

"""
    create global map
"""
proj_PC = ccrs.PlateCarree()
fig = plt.figure(figsize=(11,8.5))
ax = plt.subplot(1,1,1, projection=proj_PC)
ax.set_title("Plate Carree Map")

#set grid lines
gl = ax.gridlines(draw_labels=True, linewidth=2, color="gray", alpha=0.5, linestyle="--")

"""
    set_extent() restricts map coverage
        - enter lon/lat limits
"""
#define limits
lonW = -140
lonE = -40
latS = 15
latN = 65

ax.set_extent([lonW,lonE,latS,latN], crs=proj_PC)

"""
    adding features
    
    resolution - higher resolution, less detail (10m, 50m, 110m)
"""
res = "110m"
ax.coastlines(resolution=res, color="black")
ax.add_feature(cfeature.STATES, linewidth=0.3, edgecolor='brown')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='blue')

plt.show()

#Stereographic version NEXT