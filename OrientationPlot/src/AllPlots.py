'''
Created on Dec 19, 2016

@author:  Smit Kamal & Peter Mackenzie-Helnwein
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

from PolarPanel1 import *
from PolarPanel2 import *
from RectanglePanel import *

class AllPlots(wx.Panel):
    
    def __init__(self,parent,id=-1):
        
        wx.Panel.__init__(self, parent,id)
        #self.maw=PARENT
        
        self.lpanel = PolarPanel1(self, -1)
        self.rpanel = PolarPanel2(self, -1)
        self.bpanel = RectanglePanel(self, -1)
        
        hsz = wx.BoxSizer(wx.HORIZONTAL)
        hsz.Add(self.lpanel, 1, wx.EXPAND)
        hsz.Add(self.rpanel, 1, wx.EXPAND)
        
        vsz = wx.BoxSizer(wx.VERTICAL)
        vsz.Add(hsz, 1, wx.EXPAND)
        vsz.Add(self.bpanel, 1, wx.EXPAND)
        self.SetSizer(vsz)
        
    
    def Clear(self):
        self.lpanel.Clear()
        self.rpanel.Clear()
        self.bpanel.Clear()
        
    def SetData(self, x, y, r, theta, val):
        self.lpanel.SetData(x, y, r, theta, val)
        self.rpanel.SetData(x, y, r, theta, val)
        self.bpanel.SetData(x, y, r, theta, val)
        
    def GetData(self):
        return self.lpanel.GetData()
    
    def Reset(self):
        self.lpanel.Reset()
        self.rpanel.Reset()
        self.bpanel.Reset()
        
        
        

