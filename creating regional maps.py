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
lims = [lonW,lonE,latS,latN]

ax.set_extent(lims, crs=proj_PC)

"""
    adding features
    
    resolution - higher resolution, less detail (10m, 50m, 110m)
"""
res = "110m"
ax.coastlines(resolution=res, color="black")
ax.add_feature(cfeature.STATES, linewidth=0.3, edgecolor='brown')
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='blue')

plt.show()


"""
    Stereographic Projection - displays polar regions more accurately

"""
#define central longitude and latitude
cLon = (lonW + lonE) / 2
cLat = (latN + latS) / 2

proj_Stereo = ccrs.Stereographic(central_longitude=cLon, central_latitude=cLat)

fig2 = fig
ax2 = plt.subplot(1, 1, 1, projection=proj_Stereo)
ax2.set_title("Stereographic")
gl2 = ax2.gridlines(draw_labels=True, linewidth=2, color='gray', alpha=0.5, linestyle='--')

ax2.set_extent(lims, crs=proj_PC)
ax2.coastlines(resolution=res, color='black')
ax2.add_feature(cfeature.STATES, linewidth=0.3, edgecolor='brown')
ax2.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='blue')
plt.show()


"""
    Lambert Conformal Projection

"""
proj_Lcc = ccrs.LambertConformal(central_longitude=cLon, central_latitude=cLat)

fig3 = fig
ax3 = plt.subplot(1, 1, 1, projection=proj_Lcc)
ax3.set_title('Lambert Conformal')
gl3 = ax3.gridlines(draw_labels=True, linewidth=2, color='gray', alpha=0.5, linestyle='--')
ax3.set_extent(lims, crs=proj_PC)
ax3.coastlines(resolution=res, color='black')
ax3.add_feature(cfeature.STATES, linewidth=0.3, edgecolor='brown')
ax3.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='blue')
plt.show()