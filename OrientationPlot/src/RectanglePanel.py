'''
Created on Dec 19, 2016

@author: Smit Kamal & Peter Mackenzie-Helnwein
'''
from IDs import *

import wx
#import os
import matplotlib
matplotlib.use('WXAgg')

from matplotlib.figure import Figure
import numpy as np
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

        
class RectanglePanel(wx.Panel):
    
    
    def __init__(self,parent,id=-1):
        
        wx.Panel.__init__(self,parent,id)
        #self.maw=PARENT
        self.Reset()
        
        self.fig = Figure(figsize=(2.0, 1.0), dpi=100)
        self.canvas = FigCanvas(self, -1, self.fig)
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        #self.toolbar.Realize()
        self.initAxes()
        self.SetLimits()
        self.SetGrid()
        
        sizerCv = wx.BoxSizer(wx.VERTICAL)
        sizerCv.Add(self.canvas, 1, wx.EXPAND)
        sizerCv.Add(self.toolbar, 0, wx.EXPAND)
        self.SetSizer(sizerCv)
        
    def initAxes(self):
        self.fig.clf(keep_observers=False)
        self.ax = self.fig.add_subplot(111, axisbg='#FFFFFF')
        self.SetLimits()
        self.SetGrid()
       
    def Clear(self):
        self.ax.cla()
        self.SetLimits()
        self.SetGrid()
        self.canvas.draw()
        
    def SetLimits(self):
        self.ax.set_xlim(-10, 370)
        #self.ax.set_ylim(-95, 95)
        self.ax.set_ylim(-5, 95)
        
    def SetGrid(self):
        # major ticks every 20, minor ticks every 5   
                                           
        major_ticks = np.arange(0, 361, 45)                                              
        minor_ticks = np.arange(0, 361, 15)                                               
        
        self.ax.set_xticks(major_ticks)                                                       
        self.ax.set_xticks(minor_ticks, minor=True)
                                                   
        #major_ticks = np.arange(-90, 91, 30)                                              
        #minor_ticks = np.arange(-90, 91, 10)                                               
        
        major_ticks = np.arange(-0, 91, 30)                                              
        minor_ticks = np.arange( 0, 91, 10)                                               
        
        self.ax.set_yticks(major_ticks)                                                       
        self.ax.set_yticks(minor_ticks, minor=True)                                           
        
        # and a corresponding grid  
        self.ax.grid(which='both')                                                            
        
        # or if you want differnet settings for the grids:                               
        self.ax.grid(which='minor', alpha=0.2)                                                
        self.ax.grid(which='major', alpha=0.5)                                                

        
    def SetData(self, x, y, r, theta, val, area=[]):
        if area == []:
            area = val
        self.dataX   = x
        self.dataY   = y
        self.dataR   = r
        self.dataTh  = theta
        self.dataArea = [ 10. * i for i in area ]
        self.dataVal = val
        self.initAxes()
        self.c = self.ax.scatter(self.dataX, self.dataY, c=self.dataVal, s=self.dataArea, linewidth=0)
        self.fig.colorbar(self.c)
        self.SetLimits()
        self.SetGrid()
        self.canvas.draw()
        
    def GetData(self):
        return (self.dataX[:], self.dataY[:], self.dataR[:], self.dataTh[:], self.dataVal[:], self.dataArea[:])
    
    def Reset(self):
        self.dataR    = []
        self.dataTh   = []
        self.dataVal  = []
        self.dataArea = []
