#################################################################################################################################
#     @file     :    data_constants.py  
#
#     @brief    :    Constants for Sensor and Camera Tracking Data
#
#     @authors  :    Madi Davis (madelind@andrew.cmu.edu) 
#################################################################################################################################

# ----------------------------------------------------------------------------------------------------------------------------- #
# --- INCLUDES --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Libraries for Stats & Analysis
import numpy as np
import pandas as pd
import math
import decimal


# ----------------------------------------------------------------------------------------------------------------------------- #
# --- SENSOR DATA --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
# --- LABJACK T7 PROPERTIES --------------------------------------------------------------------------------------------------- #
##  @brief  :   LabJack T7 DAQ Sampling Rate (Hz)
LABJACK_SAMPLING_RATE = 100


# --- SENSOR FILTERING & SIGNAL VARIABLES ------------------------------------------------------------------------------------- #
##  @brief  :   New Reduced Sampling Rate for Sensor Data (Hz)
SAMPLING_RATE = 10


# --- SENSOR STATS  ---------------------------------------------------------------------------------------------------------- #
##  @brief  :   Variables Related to Flex/Ex Rotation Data from Rotation Sensor
ROTATION_INCR_SIZE = 15                                                            ##< Distance Between Flex/Ex Angles
ROTATION_INCR_RANGE = [0, 195]                                                     ##< Flex/Ex Range for Analysis
ROTATION_INCREMENTS = np.arange(start=ROTATION_INCR_RANGE[0],                      ##< List of Discrete Flex/Ex Angles for Stats
                                stop=ROTATION_INCR_RANGE[1],
                                step=ROTATION_INCR_SIZE)           



# ----------------------------------------------------------------------------------------------------------------------------- #
# --- MARKER DATA --- #
# ----------------------------------------------------------------------------------------------------------------------------- #
# --- MARKER CALIBRATION VARIABLES -------------------------------------------------------------------------------------------- #
##  @brief  :   List of Marker Names
marker_names = ["M1", "M2", "M3", "M4", "M5"]

##  @brief  :   Number of Ligament markers
num_markers = len(marker_names)

##  @brief  :   List of Marker Coordinate Dimensions
marker_dims = ["X", "Y", "Z"]

##  @brief  :   Number of Positional Dimensions
num_marker_dims = len(marker_dims)



# --- MARKER TIMESTAMPS ------------------------------------------------------------------------------------------------------- #
##  @brief  :   Marker Key Time Stamps
##              -> Manually Determined from Camera Tracking Data
##              -> idx 0 = time @ full_flex,  idx 1 = time @ full_ex
##              -> timestamps in ms
marker_timestaps = {
    'MD20031067'    : {
        'INTACT'      : [24600, 34100],
        'INTACT_IJS'  : [27200, 35300]
    },
    'MD20030643'    : {
        'INTACT'      : [36500, 53300],
        'INTACT_IJS'  : [71300, 83200]
    },
    'OH20102996_L'  : {
        'INTACT'      : [30600, 36100],
        'INTACT_IJS'  : [30200, 34300]
    },
    'OH20102996_R'  : {
        'INTACT'      : [55500, 67200],
        'INTACT_IJS'  : [20600, 28400]
    },
    'PA20031070_L'  : {
        'INTACT'      : [23400, 28100],
        'INTACT_IJS'  : [24400, 29100]
    },
    'PA20031070_R'  : {
        'INTACT'      : [15600, 20000],
        'INTACT_IJS'  : [18500, 23500]
    },
    'MD20030960_L' : {
        'INTACT'      : [23800, 28800],
        'INTACT_IJS'  : [29700, 35800]
    },
    'MD21101880_L'  : {
        'INTACT'      : [24200, 28300],
        'INTACT_IJS'  : [36700, 41700]
    }
}


# --- MARKER FILTERING & SIGNAL VARIABLES ------------------------------------------------------------------------------------- #
##  @brief  :   Low Pass Filter Properties for Marker Filtering
LPF_CUTOFF = 50                                                                    ##< Low Pass Filter Cutoff = 50Hz
LPF_ORDER = 5                                                                      ##< Low Pass Filter Order = 5
