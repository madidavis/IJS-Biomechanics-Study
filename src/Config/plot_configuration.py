#################################################################################################################################
#     @file     :    plot_configuration.py  
#
#     @brief    :    Variables for Data Visualisation Styling
#
#     @authors  :    Madi Davis (madelind@andrew.cmu.edu) 
#################################################################################################################################
# ------------------------------------------------------------------------------------------------------------------------------#
# --- INCLUDES --- #
# ------------------------------------------------------------------------------------------------------------------------------#
##  @brief  :   Libraries for Data Visualisation
import matplotlib.pyplot as plt
import matplotlib

# ------------------------------------------------------------------------------------------------------------------------------#
# --- VARIABLE DEFINITIONS --- #
# ------------------------------------------------------------------------------------------------------------------------------#
# --- SIZING & LAYOUT --- #
##  @brief  :   Figure Size & Aspect Ratio
FIGURE_SIZE = (8,5)


# --- FONT -------------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Font Size
TITLE_SIZE = 14
AXES_SIZE = 12
LABEL_SIZE = 10

##  @brief  :   General Font Properties
plot_font= {'family' : 'sans-serif',
            'weight' : 'normal',
            'size'   : AXES_SIZE}

matplotlib.rc('font', **plot_font)


# --- COLOUR CODES ---------------------------------------------------------------------------------------------------------- #
##  @brief  :   Colours Specifying Trial Types
TRIAL_COLOURS = {
    ##  @brief  :   Colours Specifying Trial Types
    "INTACT"      : [0.2, 0.73, 0.93],    ## CYAN
    'INTACT_IJS'  : [0, 0.6, 0.53],       ## TEAL
    'DISRUPT'     : [0.8, 0.02, 0.067],   ## RED
    'DISRUPT_IJS' : [0.93, 0.467, 0.2]    ## ORANGE
}

##  @brief  :   Colours Specifying Data Input Types
INPUT_DATA_COLOURS = {
    'INCLINOMETER'  : (0/255,119/255, 187/255), ## CYAN
    'ROTATION'      : (51/255, 187/255, 238/255),  ## INDIGO
    'SP'            : (51/255, 34/255, 136/255),   ## BLUE
    'TRACKING'      : (204/255, 5/255, 17/255)    ## RED
}

##  @brief  :   Colours Specifying Tracking Markers
MARKER_DATA_COLOURS = [
    [51/255, 34/255, 136/255],  ## BLUE
    [0.2, 0.73, 0.93],          ## CYAN
    [0, 0.6, 0.53],             ## TEAL
    [0.93, 0.467, 0.2],          ## ORANGE
    [204/255, 5/255, 17/255]    ## RED

]

##  @brief  :   Additional Plot Format Colours
SHADED_COLOUR = (221/255, 221/255, 221/255)       ## PALE GREY
V_INTERCEPT_COLOUR = (187/255, 187/255, 187/255)  ## GREY
H_INTERCEPT_COLOUR = (204/255, 5/255, 17/255)      ## RED
H_INTERCEPT_COLOUR_LIGHT = (238/255,51/255, 119/255, 0.2)


# --- STYLING -------------------------------------------------------------------------------------------------------------- #
##  @brief  :   Plot Line Style
INTERCEPT_LINESTYLE = 'dashdot'
MARKER_LINESTYLE = "dashed"

##  @brief  :   Plot marker/dot Style
MARKER_DOT_STYLE = "d"