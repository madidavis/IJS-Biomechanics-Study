#################################################################################################################################
#     @file     :    dataframe_config.py  
#
#     @brief    :    Variables & Constants for Dataframes 
#
#     @authors  :    Madi Davis (madelind@andrew.cmu.edu) 
#################################################################################################################################

# ----------------------------------------------------------------------------------------------------------------------------- #
# --- INCLUDES --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Libraries for File I/O & Parsing
import os
import sys
import glob
import json
import csv

##  @brief  :   Libraries for Stats & Analysis
import numpy as np
import pandas as pd
import math


# ----------------------------------------------------------------------------------------------------------------------------- #
# --- DATAFRAME IDX CONSTANTS --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Define Enum Values for sensors to Index into Data Arrays & DF Numerically
TIME = 0
LIGAMENT_DISTANCE = 1
ROTATION = 2
SP = 3
BLANK = 3 
DELTA_LENGTH_FLEX = 4
DELTA_LENGTH_EX = 5
DELTA_LENGTH_90 = 6
LUCL_STRAIN_FLEX = 7
LUCL_STRAIN_EX = 8
LUCL_STRAIN_90 = 9
DELTA_VARUS = 10
VARUS_CHANGE_PER = 11

# ----------------------------------------------------------------------------------------------------------------------------- #
# --- SENSOR DATAFRAME --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
# --- HEADERS FOR RAW DATA  --------------------------------------------------------------------------------------------------- #
##  @brief  :   Define Headers SENSOR Dataframe Headers
##                -> time = relative time from start of recording (sec)
##                -> inc_raw = Raw Data from Inclinometer Sensor
##                -> rot_raw = Raw Data from Rotational Sensor
##                -> sp_raw = Raw Data from Potentiometer
SENSOR_data_headers = ["time", "inc_raw", "rot_raw", "sp_raw"]

##  @brief  :   Dictionary to map LJM Output CSV to SENSOR Dataframe Headers
map_SENSOR_headers = {
    "B"   :   "time",
    "C"   :   "inc_raw",
    "I"   :   "rot_raw",
    "J"   :   "sp_raw"
}

# --- HEADERS FOR PROCESSED SENSOR DATA  -------------------------------------------------------------------------------------- #
##  @brief  :   Full List of DataFrame Column Headers for Raw and Processed Sensor Data
##              -> DELTA_LENGTH_FLEX = change in length from full flexion
##              -> DELTA_LENGTH_EX = change in length from full extension
##              -> DELTA_LENGTH_90 = Change in length from 90 degree rotational angle
##                                   measured from start of last cycle
##              -> LUCL_STRAIN_FLEX = LUCL strain wrt full flexion
##              -> LUCL_STRAIN_EX = LUCL strain wrt full extension
##              -> LUCL_STRAIN_90 = LUCL strain wrt 90 degrees
##              -> DELTA_VARUS = difference in inclinometer value from 90 degrees of intact trial
##              -> VARUS_CHANGE_PER = Percentage of inclinometer value from 90 degrees of intact trial
HEADERS = ["time", "inc_raw", "rot_raw", "sp_raw", 'DELTA_LENGTH_FLEX',
           'DELTA_LENGTH_EX', 'DELTA_LENGTH_90', 'LUCL_STRAIN_FLEX',
           'LUCL_STRAIN_EX', 'LUCL_STRAIN_90', 'DELTA_VARUS',
           'VARUS_CHANGE_PER']


# ----------------------------------------------------------------------------------------------------------------------------- #
# --- MARKER DATAFRAME --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Marker Data Frame Headers for Raw and Processed Data
##              -> TIME = relative time from tracking recording
##              -> LIGAMENT DISTANCE = change in LUCL distance
##              -> ROTATION = FLEX / X ROTATION (From Sensor)
##              -> BLANK = Empty column to align IDX values with Sensor data
##              -> DELTA_LENGTH_FLEX = change in length from full flexion
##              -> DELTA_LENGTH_EX = change in length from full extension
##              -> DELTA_LENGTH_90 = Change in length from 90 degree rotational angle
##                                   measured from start of last cycle
##              -> LUCL_STRAIN_FLEX = LUCL strain wrt full flexion
##              -> LUCL_STRAIN_EX = LUCL strain wrt full extension
##              -> LUCL_STRAIN_90 = LUCL strain wrt 90 degrees
MARKER_data_headers = ["TIME", "LIGAMENT_DISTANCE", "ROTATION", 
                       "N/A", "DELTA_LENGTH_FLEX","DELTA_LENGTH_EX",
                       "DELTA_LENGTH_90", "LUCL_STRAIN_FLEX", "LUCL_STRAIN_EX",
                         "LUCL_STRAIN_90"]


# ----------------------------------------------------------------------------------------------------------------------------- #
# --- EXPORT DATAFRAMES --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
# --- STATS ANALYSIS DATAFRAME  ----------------------------------------------------------------------------------------------- #
##  @brief  :  Export Dataframe Headers
export_headers = ['ID', 'TRIAL',
                  'VALUE__VARUS', 'VALUE__VARUS_CHANGE','VALUE__LUCL_SP', 'VALUE__LUCL_MARKER', 'VALUE__FLEX_EX',
                  'MEAN__VARUS', 'MIN__VARUS', 'MAX__VARUS', 'STD__VARUS', 'STDERR__VARUS',
                  'MEAN__VARUS_CHANGE', 'MIN__VARUS_CHANGE', 'MAX__VARUS_CHANGE', 'STD__VARUS_CHANGE', 'STDERR__VARUS_CHANGE',
                  'MEAN__LUCL_SP', 'MAX__LUCL_SP','STD__LUCL_SP', 'STDERR__LUCL_SP', 
                  'MEAN__LUCL_MARKER', 'MAX__LUCL_MARKER','STD__LUCL_MARKER','STDERR__LUCL_MARKER',
                  ]


##  @brief  :  Strings for Dataframe Row Flex-Ex Rotation Values
flex_ex_angles = ['FLEX__VARUS', 'EX__VARUS', 'MID_FLEX__VARUS', 'MID_EX__VARUS',
                 'DEG_0__VARUS', 'DEG_15__VARUS','DEG_30__VARUS', 'DEG_45__VARUS', 'DEG_60__VARUS', 'DEG_75__VARUS', 'DEG_90__VARUS', 'DEG_105__VARUS',
                 'DEG_120__VARUS', 'DEG_135__VARUS', 'DEG_150__VARUS', 'DEG_165__VARUS', 'DEG_180__VARUS', 'DEG_195__VARUS']


# --- BLAND ALTMAN ANALYSIS DATFRAME  ----------------------------------------------------------------------------------------- #
##  @brief  :  Bland Altman Dataframe Headers
bland_altman_headers = ['ID', 'TRIAL', 'ROTATION', 'SP', 'MARKER']