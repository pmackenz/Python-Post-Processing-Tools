'''
Created on Dec 19, 2016

@author: Smit Kamal & Peter Mackenzie-Helnwein
'''
from IDs import *

import wx
#import os
import matplotlib
#from apptools.help.help_plugin.action.demo_action import PARENT
matplotlib.use('WXAgg')

from matplotlib.figure import Figure
#from numpy import pi
#import numpy as np
#from math import asin

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

from PolarPanel import *

        
class PolarPanel1(PolarPanel):
    
    
    def __init__(self,parent,id=-1):
        
        PolarPanel.__init__(self,parent,id)
        #self.maw = PARENT
        
    def SetLimits(self):
        self.ax.set_xlim(-180, 180)
        self.ax.set_ylim(0, 1.1)
        
    
    
