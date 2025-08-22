# src/io_fetch.py
"""Data acquisition helpers (stubs).
Add functions to download and cache raw datasets (EPA AirToxScreen, EIA plants, ACS).
"""
from pathlib import Path

RAW = Path("data/raw")

def ensure_data_dir():
    RAW.mkdir(parents=True, exist_ok=True)
