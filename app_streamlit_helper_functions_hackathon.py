# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 12:53:27 2020

@author: GUPTAS2Q
"""

import pandas as pd
import numpy as np
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.metrics import mean_squared_error

@st.cache
def RMSE(predData, idvar, predvar, filename):
    
    actData = pd.read_csv("extra_files\\actData\\actData.csv")
    predData = predData.sort_values(idvar)
    actData = actData.sort_values(idvar)
    rmse = mean_squared_error(actData[predvar], predData[predvar])
    return rmse

    
    
    
    
    