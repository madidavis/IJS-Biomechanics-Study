#################################################################################################################################
#     @file     :    filepaths.py  
#
#     @brief    :    Paths to Data & Results in Project
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

# ----------------------------------------------------------------------------------------------------------------------------- #
# --- FILEPATH STRINGS --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Path to Root Project Folder
ROOT = "/content/drive/MyDrive/Practicum"


# --- RAW DATA ---------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Path to Collected Experimental Data Folder
DATA_DIR = os.path.join(ROOT, "Data")


# --- RESULTS ----------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Path to Results Folder
RESULTS_DIR = os.path.join(ROOT, "Results")

##  @brief  :   Path to Generated Plots
PLOT_DIR = os.path.join(RESULTS_DIR, "Plots")


# --- CODE ------------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Path to Collected Experimental Data Folder
CODE_DIR = os.path.join(ROOT, "src")

##  @brief  :   Path to Configuration Files
CONFIG_DIR = os.path.join(CODE_DIR, "Config")

##  @brief  :   Path to Script Files
SCRIPT_DIR = os.path.join(CODE_DIR, "Scripts")

##  @brief  :   Path to Utilities Files
UTILITIES_DIR = os.path.join(CODE_DIR, "Utilities")