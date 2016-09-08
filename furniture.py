from __future__ import division
#import matplotlib
import pylab
import time
import sys
import random
import re
import csv
import math
import numpy as np
from psychopy import visual,logging,event,core, monitors
from python_experiment_functions import *
from furniture_room import *

def main():
    fullscreen = False
    background_color = [0,0,0]
    win, scrwidth, scrheight = window_creation(fullscreen, background_color)

    al = furniture_room(background_color,win)

    response_screen(win, scrwidth, scrheight,"test", "press q", ['q'])


    sys.exit()



if __name__ == "__main__":
    main()
