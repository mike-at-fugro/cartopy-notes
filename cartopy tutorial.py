"""
    Cartopy
        - map projections and GeoAxes
        - exploring map projections
        - creating regional maps

"""
import warnings
import matplotlib.pyplot as plt
import numpy as np
from cartopy import crs as ccrs, feature as cfeature

# Suppress warnings when downloading data files
warnings.filterwarnings("ignore")

"""
    matplotlib figure: has Figure object, list of Axes objects (subplots)

    use cartopy.crs (Coordinate Reference System) to convert Axes to GeoAxes objects
        - allows us to georeference the subplot
"""

"""
    Creating a map with a specified projection

    - creating a geoaxes object using PlateCarree projection
        - Plate Carree (flat square): global lat-lon map projection with each point evenly spaced by degrees

"""
fig = plt.figure(figsize=(11,8.5))
ax = plt.subplot(1,1,1, projection=ccrs.PlateCarree(central_longitude=-75))
ax.set_title("A Geo-referenced subplot, Plate Carree projection")

"""
    looks empty but has been georeferenced using the map projection provided by crs

    adding in coastline shapefile via the GeoAxes method coastlines():
"""
ax.coastlines()
#plt.show()

"""
    Adding cartographic features

    - adding features from shapefiles via the features class, using add_feature()

"""
ax.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor="black")
ax.add_feature(cfeature.LAKES, linewidth = 0.5, edgecolor="blue")
ax.add_feature(cfeature.RIVERS, linewidth = 0.5, edgecolor="blue")
plt.show()


"""
    Using Different Projections

    Mollweide Projection - often used with global satellite mosaics
"""
#create projection object
proj_Moll = ccrs.Mollweide(central_longitude=0)

ax2 = plt.subplot(1,1,1, projection=proj_Moll)
ax2.set_title("Mollweide Projection")

ax2.coastlines()
ax2.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor="black")
ax2.add_feature(cfeature.LAKES, linewidth = 0.5, edgecolor="blue")
ax2.add_feature(cfeature.RIVERS, linewidth = 0.5, edgecolor="blue")

#add preset background to projection plot
ax2.stock_img()

plt.show()


"""
    Lambert Azimuthal Equal Area Projection
"""
proj_Lam = ccrs.LambertAzimuthalEqualArea(central_longitude=0.0, central_latitude=0.0)

ax3 = plt.subplot(1,1,1, projection=proj_Lam)
ax3.set_title("Lambert Azimuthal Equal Area Projection")
ax3.coastlines()
ax3.add_feature(cfeature.BORDERS, linewidth=0.5, edgecolor='blue')

plt.show()