# src/features.py
"""Feature engineering & joins (stubs)."""
import geopandas as gpd
import pandas as pd

def load_processed(path: str) -> gpd.GeoDataFrame:
    return gpd.read_file(path)
