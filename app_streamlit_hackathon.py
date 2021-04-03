# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:29:42 2021

@author: GUPTAS2Q
"""
import pandas as pd
import numpy as np
import re
import streamlit as st
from datetime import datetime
from PIL import Image
import io
#import plotly.graph_objs as go
import matplotlib.pyplot as plt
#from plotly.subplots import make_subplots
#import plotly
import datetime
import SessionState
from SessionState import get
from app_streamlit_helper_functions_hackathon import *

st.set_option('deprecation.showfileUploaderEncoding', False)

def login_password():
    title = st.empty()
    title.title("Welcome to Novartis DS&D Data Science Hackathon Challenge")
    subtitle = st.empty()
    subtitle.header("Please enter your login details to proceed")
    login = st.empty()
    login.subheader("LOGIN")
    
    login_id = st.empty()
    login_id.text_input("Name")
    login_password = st.empty()
    
    try:
        if login_password.text_input("Password", type= "password") == "password" and login_id is not None:
            logid = login_id
            title.empty()
            subtitle.empty()
            login.empty()
            login_id.empty()
            login_password.empty()
            return "Correct Password", logid
        else:
            st.error("Incorrect Details")
    except:
        pass
   
    
def Competition(): 
    
    st.title("Welcome to Novartis DS&D Data Science Hackathon Challenge")
    st.header("Download the datasets & read the rules,regulations here!")
    
    col1, col2 = st.beta_columns(2)
    with col1:
        st.subheader("House Prices - Advanced Regression Techniques")
        
        st.write("""
                 Ask a home buyer to describe their dream house, and they probably won't begin with the height of the basement ceiling or the proximity to an east-west railroad.
                 But this playground competition's dataset proves that much more influences price negotiations than the number of bedrooms or a white-picket fence.

                With 79 explanatory variables describing (almost) every aspect of residential homes in Ames, Iowa, this competition challenges you to predict the final price of each home.
                
                **Goal**     
                It is your job to predict the sales price for each house. For each Id in the test set, you must predict the value of the SalePrice variable. 
                
                **Practice Skills**
                 - Creative feature engineering 
                 - Advanced regression techniques like random forest and gradient boosting
                """)
    
        
    with col2:
        st.subheader("Data")
        st.write("""
                  - train.csv - the training set
                  - test.csv - the test set
                  - data_description.txt - full description of each column, originally prepared by Dean De Cock but lightly edited to match the column names used here
                  - sample_submission.csv - a benchmark submission from a linear regression on year and month of sale, lot square footage, and number of bedrooms
                 """
                 )
        
#        st.write("""
#                 **Data fields**
#                Here's a brief version of what you'll find in the data description file.
#                """)
#                
        with st.beta_expander("+ Data Fields"):
                st.write('''
                         - SalePrice - the property's sale price in dollars. This is the target variable that you're trying to predict.
                         - MSSubClass: The building class
                         - MSZoning: The general zoning classification
                         - LotFrontage: Linear feet of street connected to property
                         - LotArea: Lot size in square feet
                         - Street: Type of road access
                         - Alley: Type of alley access
                         - LotShape: General shape of property
                         - LandContour: Flatness of the property
                         - Utilities: Type of utilities available
                         - LotConfig: Lot configuration
                         - LandSlope: Slope of property
                         - Neighborhood: Physical locations within Ames city limits
                         - Condition1: Proximity to main road or railroad
                         - Condition2: Proximity to main road or railroad (if a second is present)
                         - BldgType: Type of dwelling
                         - HouseStyle: Style of dwelling
                         - OverallQual: Overall material and finish quality
                         - OverallCond: Overall condition rating
                         - YearBuilt: Original construction date
                         - YearRemodAdd: Remodel date
                         - RoofStyle: Type of roof
                         - RoofMatl: Roof material
                         - Exterior1st: Exterior covering on house
                         - Exterior2nd: Exterior covering on house (if more than one material)
                         - MasVnrType: Masonry veneer type
                         - MasVnrArea: Masonry veneer area in square feet
                         - ExterQual: Exterior material quality
                         - ExterCond: Present condition of the material on the exterior
                         - Foundation: Type of foundation
                         - BsmtQual: Height of the basement
                         - BsmtCond: General condition of the basement
                         - BsmtExposure: Walkout or garden level basement walls
                         - BsmtFinType1: Quality of basement finished area
                         - BsmtFinSF1: Type 1 finished square feet
                         - BsmtFinType2: Quality of second finished area (if present)
                         - BsmtFinSF2: Type 2 finished square feet
                         - BsmtUnfSF: Unfinished square feet of basement area
                         - TotalBsmtSF: Total square feet of basement area
                         - Heating: Type of heating
                         - HeatingQC: Heating quality and condition
                         - CentralAir: Central air conditioning
                         - Electrical: Electrical system
                         - 1stFlrSF: First Floor square feet
                         - 2ndFlrSF: Second floor square feet
                         - LowQualFinSF: Low quality finished square feet (all floors)
                         - GrLivArea: Above grade (ground) living area square feet
                         - BsmtFullBath: Basement full bathrooms
                         - BsmtHalfBath: Basement half bathrooms
                         - FullBath: Full bathrooms above grade
                         - HalfBath: Half baths above grade
                         - Bedroom: Number of bedrooms above basement level
                         - Kitchen: Number of kitchens
                         - KitchenQual: Kitchen quality
                         - TotRmsAbvGrd: Total rooms above grade (does not include bathrooms)
                         - Functional: Home functionality rating
                         - Fireplaces: Number of fireplaces
                         - FireplaceQu: Fireplace quality
                         - GarageType: Garage location
                         - GarageYrBlt: Year garage was built
                         - GarageFinish: Interior finish of the garage
                         - GarageCars: Size of garage in car capacity
                         - GarageArea: Size of garage in square feet
                         - GarageQual: Garage quality
                         - GarageCond: Garage condition
                         - PavedDrive: Paved driveway
                         - WoodDeckSF: Wood deck area in square feet
                         - OpenPorchSF: Open porch area in square feet
                         - EnclosedPorch: Enclosed porch area in square feet
                         - 3SsnPorch: Three season porch area in square feet
                         - ScreenPorch: Screen porch area in square feet
                         - PoolArea: Pool area in square feet
                         - PoolQC: Pool quality
                         - Fence: Fence quality
                         - MiscFeature: Miscellaneous feature not covered in other categories
                         - MiscVal: $Value of miscellaneous feature
                         - MoSold: Month Sold
                         - YrSold: Year Sold
                         - SaleType: Type of sale
                         - SaleCondition: Condition of sale 
                        ''')
                
        
    st.write("----")
        
    col1, col2 = st.beta_columns(2)
        
    with col1:
        st.write("""
                     **Competition Timeline**
                      - Start Date: 8/31/2021
                      - End Date: 9/30/2021
                        
                        We ask that you respect the spirit of the competition and do not cheat. Hand-labeling is forbidden.
                    """)
        
    
    with col2:
        st.write("""
                 **Evaluation Criteria**                
                 Submissions are evaluated on [Root-Mean-Squared-Error (RMSE)](https://en.wikipedia.org/wiki/Root-mean-square_deviation) between the logarithm of the predicted value and the logarithm of the observed sales 
                 price. (Taking logs means that errors in predicting expensive houses and cheap houses will affect the result equally.)
                 
                 **Submission File Format**      
                 The file should contain a header and have the following format:   
                    """)
        st.code("""
Id,SalePrice
1461,169000.1
1462,187724.1233
1463,175221   
                 """, "python")
    
        st.write("""
                 **Upload your submission**   
                 """)
        data_upload1 = st.file_uploader("Please upload your submission to evaluate...", type="csv", encoding = None)
        try:
            data_upload = st.file_uploader("Please upload your submissi to evaluate...", type="csv", encoding = None)
            file_name = data_upload.name.split("_")[1].split(".csv")[0]
            data_upload = pd.read_csv(io.TextIOWrapper(data_upload), sep = ",")
            rmse_result = RMSE(predData = data_upload, idvar = "Id", predvar="SalePrice",
                               filename = file_name)
            st.write("""
                    **RMSE result:**
                    """)
            st.info(rmse_result)
            timenow = str(datetime.datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p"))
            
            #Addig latest RMSE
            tempLeaderBoard = pd.DataFrame()
            tempLeaderBoard.loc[0,"Name"] = file_name
            tempLeaderBoard.loc[0,"Date"] = str(timenow)
            tempLeaderBoard.loc[0,"RMSE"] = rmse_result
            
            leaderBoard_final = pd.read_csv("extra_files//LeaderBoard//leaderboard.csv")
            leaderBoard_final = pd.concat([leaderBoard_final,tempLeaderBoard], axis=0)
            data_upload.to_csv("extra_files//predData//predData_" + file_name + "_" + timenow + ".csv")
            leaderBoard_final.to_csv("extra_files//LeaderBoard//leaderboard.csv", index=False)
        except:
            pass
                 
        
        
def Leaderboard():
    st.title("Competition Leaderboard - Public")
    
    leaderBoard = pd.read_csv("extra_files//LeaderBoard//leaderboard.csv")
    leaderBoard = leaderBoard.sort_values("RMSE").reset_index(drop=True)
    
    st.subheader("This leaderboard is calculated with all of the test data")
    st.table(leaderBoard)
    
    
    
    
 
def post_login():
   
    pages = {
        "Competition": Competition,
        "Leaderboard": Leaderboard,
    }
        
    page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))
 
    if page == "Competition":
        pages["Competition"]()
    elif page == "Leaderboard":
        pages["Leaderboard"]()
    
   
def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )
    
def main():
    _max_width_()   
    st.sidebar.image("extra_files//novartis_logo_pos_rgb.png", width = 260)
    post_login()        
    return

    
session_state = get(password='')

if session_state.password != 'pwd123':
    title = st.empty()
    title.title("Welcome to Novartis DS&D Data Science Hackathon Challenge")
    subtitle = st.empty()
    subtitle.header("Please enter your login details to proceed")
    login = st.empty()
    login.subheader("LOGIN")
    login_id = st.empty()
    login_id.text_input("Name")
   
    pwd_placeholder = st.empty()
    pwd = pwd_placeholder.text_input("Password:", value="", type="password")
    session_state.password = pwd
    if session_state.password == 'pwd123':
        pwd_placeholder.empty()
        title.empty()
        subtitle.empty()
        login.empty()
        login_id.empty()
        main()
    elif session_state.password != '':
        st.error("the password you entered is incorrect")
else:
    main()

