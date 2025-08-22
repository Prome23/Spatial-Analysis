# src/weights.py
import geopandas as gpd
from libpysal.weights import Queen, KNN

def queen_weights(gdf: gpd.GeoDataFrame):
    w = Queen.from_dataframe(gdf)
    w.transform = 'R'
    return w
