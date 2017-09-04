'''
Created on Dec 19, 2016

@author: Smit Kamal & Peter Mackenzie-Helnwein
'''
from IDs import *

import wx

from math import asin, pi
import numpy as np

import matplotlib
matplotlib.use('WXAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

from PolarPanel import *
        
class PolarPanel2(PolarPanel):
    
    
    def __init__(self,parent,id=-1):
        
        PolarPanel.__init__(self,parent,id)
            
    def SetLimits(self):
        self.ax.set_xlim(-180, 180)
        self.ax.set_ylim(0, 95)
        
    def SetGrid(self):
        # major ticks every 20, minor ticks every 5   
                                           
        major_ticks = np.arange(0, 2*np.pi, np.pi/6.) 
        self.ax.set_xticks(major_ticks)              
                                                   
        major_ticks = np.arange(0, 91, 30) 
        self.ax.set_yticks(major_ticks)                                                       
        
        # and a corresponding grid  
        self.ax.grid(which='both')                                                                 
        
        # or if you want differnet settings for the grids:                               
        self.ax.grid(which='minor', alpha=0.2)                                                
        self.ax.grid(which='major', alpha=0.5) 
        
    def SetData(self, x, y, r, theta, val, area=[]):
        r2 = [180.0/pi*s for s in map(asin, r)]
        PolarPanel.SetData(self, x, y, r2, theta, val, area)
