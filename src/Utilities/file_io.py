#################################################################################################################################
#     @file     :    file_io.py  
#
#     @brief    :    Helpers for processing raw data and converting to pandas dataframes
#
#     @authors  :    Madi Davis (madelind@andrew.cmu.edu) 
#################################################################################################################################

# ------------------------------------------------------------------------------------------------------------------------------#
# --- INCLUDES --- #
# ------------------------------------------------------------------------------------------------------------------------------#
##  @brief  :   Libraries for File I/O & Parsing
import os
import sys
import glob
import json
import csv

##  @brief  :   Libraries for Stats & Analysis
import pandas as pd



# ------------------------------------------------------------------------------------------------------------------------------#
# --- HELPER FUNCTIONS --- #
# ------------------------------------------------------------------------------------------------------------------------------#
def load_csv_recording(file_name):
  """!  Load Individual Sensor or Tracking Recording as a Dataframe

        @param[in]  :   file_name = complete path to a file (string)
        @return     :   df = TRACKING or SENSOR data structured as a dataframe
  """
  df = None
  try:
    # If File Exists read into a dataframe
    df = pd.read_csv(file_name)
  except:
    print("Error - " + file_name + " doesn't exist")
  return df

def load_dat_recording(file_name):
  """!  Load Individual Sensor or Tracking Recording as a Dataframe

        @param[in]  :   file_name = complete path to a file (string)
        @return     :   df = TRACKING or SENSOR data structured as a dataframe
  """
  df = None
  try:
    # If File Exists read into a dataframe
    df = pd.read_csv(file_name, delimiter='\t')
  except:
    print("Error - " + file_name + " doesn't exist")
  return df