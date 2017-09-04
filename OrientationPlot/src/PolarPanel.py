'''
Created on Dec 19, 2016

@author:  Peter Mackenzie-Helnwein
'''
from IDs import *

import wx
import os
import matplotlib
#from apptools.help.help_plugin.action.demo_action import PARENT
matplotlib.use('WXAgg')

from matplotlib.figure import Figure
#from numpy import pi
#import numpy as np
#from math import asin

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx

        
class PolarPanel(wx.Panel):
    
    
    def __init__(self,parent,id=-1):
        
        wx.Panel.__init__(self,parent,id)
        #self.maw = PARENT
        
        buttonPDF = wx.Button(self, -1, label='Save PDF')
        buttonPNG = wx.Button(self, -1, label='Save PNG')
        self.fig = Figure(figsize=(1.0, 1.0), dpi=100)
        self.canvas = FigCanvas(self, -1, self.fig)
        
        self.initAxes()
        
        self.canvas.draw()
        
        hbx=wx.BoxSizer(wx.HORIZONTAL)
        hbx.Add(buttonPDF,1,wx.EXPAND)
        hbx.Add(buttonPNG,1,wx.EXPAND)
        
        vbx = wx.BoxSizer(wx.VERTICAL)
        vbx.Add(self.canvas, 1, wx.EXPAND)
        vbx.Add(hbx, 0, wx.EXPAND)
        self.SetSizer(vbx)
        
        # internal variables
        self.Reset()
        
        # bindings
        self.Bind(wx.EVT_BUTTON, self.OnBtnPDF, buttonPDF)
        self.Bind(wx.EVT_BUTTON, self.OnBtnPNG, buttonPNG)
        
    def initAxes(self):
        self.fig.clf(keep_observers=False)
        self.ax = self.fig.add_subplot(111,projection='polar')
        self.ax.set_theta_zero_location("N")
        self.ax.set_theta_direction(-1)
        self.SetLimits()
        self.SetGrid()
        
    def Clear(self):
        self.ax.cla()
        self.ax.set_theta_zero_location("N")
        self.ax.set_theta_direction(-1)
        self.SetLimits()
        self.SetGrid()
        self.canvas.draw()
        
    def SetLimits(self):
        # this will be overloaded in derived classes
        pass
    
    def SetGrid(self):
        # this will be overloaded in derived classes
        self.ax.grid(True)
        
    def SetData(self, x, y, r, theta, val, area=[]):
        if area == []:
            area = val
        self.dataX   = x
        self.dataY   = y
        self.dataR   = r
        self.dataTh  = theta
        self.dataVal = val
        self.dataArea = [ 10.*k for k in area ]
        self.initAxes()
        self.c = self.ax.scatter(self.dataTh, self.dataR, c=self.dataVal, s=self.dataArea, linewidth=0)
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
        
    def OnBtnPDF(self, evt):
        print "OnBtnPDF triggered for PolarPanel {}".format(self.GetId())
    
        file_choices = "PDF (*.pdf)|*.pdf"
        
        dlg = wx.FileDialog(
            self, 
            message     = "Save plot as PDF ...",
            defaultDir  = os.getcwd(),
            defaultFile = "plot.pdf",
            wildcard    = file_choices,
            style       = wx.SAVE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.canvas.print_figure(path, dpi=300)
            
    def OnBtnPNG(self, evt):
        print "OnBtnPNG triggered for PolarPanel {}".format(self.GetId())
        
        file_choices = "PNG (*.png)|*.png"
        
        dlg = wx.FileDialog(
            self, 
            message     = "Save plot as PNG ...",
            defaultDir  = os.getcwd(),
            defaultFile = "plot.png",
            wildcard    = file_choices,
            style       = wx.SAVE)
        
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            self.canvas.print_figure(path, dpi=300)
            

    
