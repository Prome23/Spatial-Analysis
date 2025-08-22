# src/models.py
import numpy as np
from spreg import ML_Lag

def spatial_lag(y, X, w, names_y, names_x):
    model = ML_Lag(y, X, w, name_y=names_y, name_x=names_x)
    return model
