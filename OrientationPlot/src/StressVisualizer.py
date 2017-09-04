'''
Created on Nov 19, 2014

@author: Smit Kamal & Peter Mackenzie-Helnwein
'''

import wx
import os
from IDs import *

import matplotlib
matplotlib.use('WXAgg')

import numpy as np
from math import asin, cos, atan2, sqrt, pi

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigCanvas
from matplotlib.backends.backend_wx import NavigationToolbar2Wx


from PolarPanel1 import *
from PolarPanel2 import *
from RectanglePanel import *
# from AllPlots import *


class StressVisualizer(wx.Frame):
    '''
    classdoc
    
    variables:
    
    methods:
        def __init__(self, title='New Demo Application'):
        def graph1(self,evt):
        def graph2(self,evt):
        def graph3(self,evt):
        def graph4(self,evt):
        def onQuit(self, e):
        def onViewReset(self,e):
        def onViewFullScreen(self,e):
        def onViewMaximize(self,e):
        def onViewShrink(self,e):
        def onMotion(self, evt):
        def onMotion2(self, evt):
        def on_save_plot(self, event):
        def on_save_plot2(self, event):
        def OnOpen(self, e):
        def file_open(self):
        def Run(self,e):    
        def OnClear(self,e):
    '''

    def __init__(self, title='New Demo Application'):
        '''
        Constructor
        '''
        w,h = wx.GetDisplaySize()
        wx.Frame.__init__(self, None, -1, title, size=(max(w/2,640),max(h/2,480)))
        self.SetMinSize((640,480))
        
        
        # initialize state variables
        self.dirname = ''
        self.dpi=300        # what for?
        
        # setting up menue options
        filemenu = wx.Menu()
        filemenu.Append(ID_FILE1,"&New","Create a new file")
        filemenu.Append(ID_FILE2,"&Open","Open an existing file")
        filemenu.Append(ID_FILE3,"&Save","Save file")
        filemenu.Append(ID_FILE4,"Save &As","Save file as")
        filemenu.AppendSeparator()
        filemenu.Append(wx.ID_EXIT,"&Quit","Quit the Application")
        
        viewmenu = wx.Menu()
        viewmenu.Append(ID_VIEW1,"&Shrink","Reduce size to half")
        viewmenu.Append(ID_VIEW2,"&Maximize","Maximize window")
        viewmenu.Append(ID_VIEW3,"&Full screen","Switch to full screen mode")
        viewmenu.Append(ID_VIEW4,"&Reset","Reset View")
        
        menubar = wx.MenuBar()
        menubar.Append(filemenu,"&File")
        menubar.Append(viewmenu,"&View")
        self.SetMenuBar(menubar)
        
        # widgets
        self.panel1 = wx.Panel(self, ID_PANEL1, pos=(200,50),style=wx.SP_3D)
        self.panel1.SetBackgroundColour([0, 126, 126])
                                    
        self.txtbox=wx.TextCtrl(self.panel1, ID_TEXT1, style=wx.TE_MULTILINE|wx.TE_READONLY)
      
        self.button1 = wx.Button(self.panel1,ID_BUTTON1, label='Reset View')
        self.button4 = wx.Button(self.panel1, ID_BUTTON4, label='Load File')
        self.button5 = wx.Button(self.panel1, ID_BUTTON5, label='Run')
        self.button6 = wx.Button(self.panel1, ID_BUTTON6, label='Clear')
        self.button8 = wx.Button(self.panel1, ID_BUTTON8, label='Graph 1')
        self.button9 = wx.Button(self.panel1, ID_BUTTON9, label='Graph 2')
        self.button10= wx.Button(self.panel1, ID_BUTTON10,label='Graph 3')
        #self.button7 = wx.Button(self.panel1, ID_BUTTON7, label='Show All')
        self.buttonQ = wx.Button(self.panel1, wx.ID_EXIT)
        
        self.pp1=PolarPanel1(self, ID_PLOT1)
        self.pp2=PolarPanel2(self, ID_PLOT2)
        self.pp3=RectanglePanel(self, ID_PLOT3)
        #self.pp4=AllPlots(self, ID_PLOT4)
        
        #self.pp1=wx.Panel(self, ID_PLOT1)
        #self.pp2=wx.Panel(self, ID_PLOT2)
        #self.pp3=wx.Panel(self, ID_PLOT3)
        #self.pp4=wx.Panel(self, ID_PLOT4)
        self.pp1.SetBackgroundColour('#ff0000')
        self.pp2.SetBackgroundColour('#ffff00')
        self.pp3.SetBackgroundColour('#00ffff')
        #self.pp4.SetBackgroundColour('#ff00ff')
        
        # layout for panel1
        vsz = wx.BoxSizer(wx.VERTICAL)
        vsz.Add(self.button4,  1, wx.ALL|wx.ALIGN_CENTER, border=5)
        vsz.Add(self.button5,  1, wx.ALL|wx.ALIGN_CENTER, border=5)
        vsz.Add(self.button6,  1, wx.ALL|wx.ALIGN_CENTER, border=5)
        vsz.Add(wx.StaticLine(self.panel1, -1), 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 5)
        vsz.Add(self.button8,  1, wx.ALL|wx.ALIGN_CENTER, border=5)
        vsz.Add(self.button9,  1, wx.ALL|wx.ALIGN_CENTER, border=5)
        vsz.Add(self.button10, 1, wx.ALL|wx.ALIGN_CENTER, border=5)
        #vsz.Add(self.button7,  1, wx.ALL|wx.ALIGN_CENTER, border=5)
        vsz.Add(wx.StaticLine(self.panel1, -1), 0, wx.TOP|wx.BOTTOM|wx.EXPAND, 5)
        vsz.Add(self.button1,  1, wx.ALL|wx.ALIGN_CENTER, border=5)
        vsz.Add(self.txtbox,   5, wx.EXPAND)
        vsz.Add(self.buttonQ,  1, wx.ALL|wx.ALIGN_CENTER, border=5)
        
        self.panel1.SetSizer(vsz)
        
        # layout for plot panels
        vsz2 = wx.BoxSizer(wx.VERTICAL)
        vsz2.Add(self.pp1, 1, wx.EXPAND)
        vsz2.Add(self.pp2, 1, wx.EXPAND)
        vsz2.Add(self.pp3, 1, wx.EXPAND)
        #vsz2.Add(self.pp4, 1, wx.EXPAND)
        
        self.graph1(None)
        
        # layout of frame
        hsz = wx.BoxSizer(wx.HORIZONTAL)
        hsz.Add(self.panel1, 0, wx.EXPAND, border=3)
        hsz.Add(vsz2, 3, wx.EXPAND)
        
        self.SetSizer(hsz)
        
        # bindings
        #wx.EVT_BUTTON(self, ID_BUTTON7,  self.graph4)
        wx.EVT_BUTTON(self, ID_BUTTON9,  self.graph2)
        wx.EVT_BUTTON(self, ID_BUTTON10, self.graph3)
        wx.EVT_BUTTON(self, ID_BUTTON8,  self.graph1)
        
        wx.EVT_MENU(self, ID_VIEW1, self.onViewShrink)
        wx.EVT_MENU(self, ID_VIEW2, self.onViewMaximize)
        wx.EVT_MENU(self, ID_VIEW3, self.onViewFullScreen)
        wx.EVT_MENU(self, ID_VIEW4, self.onViewReset)
        wx.EVT_MENU(self, ID_FILE2, self.OnOpen)
        
        wx.EVT_BUTTON(self, ID_BUTTON1, self.onViewReset)
        wx.EVT_BUTTON(self, ID_BUTTON4, self.OnOpen)
        wx.EVT_BUTTON(self, ID_BUTTON5, self.OnRun)
        wx.EVT_BUTTON(self, ID_BUTTON6, self.OnClear)
        wx.EVT_BUTTON(self, wx.ID_EXIT, self.OnExit)
        
        self.onViewReset(None)
        self.Show(True)
        
    def OnExit(self, evt):
        self.Close()
      
    def graph1(self,evt):
        
        self.pp1.Show(True)
        self.pp2.Show(False)
        self.pp3.Show(False)
        #self.pp4.Show(False)
        
        self.Layout()
          
    def graph2(self,evt):
        
        self.pp1.Show(False)
        self.pp2.Show(True)
        self.pp3.Show(False)
        #self.pp4.Show(False)
        
        self.Layout()
        
    def graph3(self,evt):
        
        self.pp1.Show(False)
        self.pp2.Show(False)
        self.pp3.Show(True)
        #self.pp4.Show(False)
        
        self.Layout()
        
    def graph4(self,evt):
        
        self.pp1.Show(False)
        self.pp2.Show(False)
        self.pp3.Show(False)
        #self.pp4.Show(True)
        
        self.Layout()
        
    def onViewReset(self,e):
        self.ShowFullScreen(False)
        self.Maximize(False)
        w,h = wx.GetDisplaySize()
        self.SetSize((w/2,h/2))
        self.Centre()
        
    def onViewFullScreen(self,e):
        self.ShowFullScreen(True)
        
    def onViewMaximize(self,e):
        self.ShowFullScreen(False)
        self.Maximize(True)
        
    def onViewShrink(self,e):
        self.ShowFullScreen(False)
        msize = []
        for i in self.GetSize():
            msize.append(int(0.75*i))
        self.SetSize(msize)
    
    def onMotion(self, evt):
        inaxes = evt.inaxes
        xdata = evt.xdata
        ydata = evt.ydata
        try:
            self.statusbar.SetStatusText("%s, %s" % ((float(xdata)*180/np.pi), ydata))
        except TypeError:
            pass
    
    def onMotion2(self, evt):
        x = evt.x
        y = evt.y
        inaxes = evt.inaxes
        xdata = evt.xdata
        ydata = evt.ydata
        try:
            self.statusbar.SetStatusText("%s, %s" % ((xdata), ydata))
        except TypeError:
            pass
    
    def OnOpen(self, e):
        self.file_open()
        e.Skip()

    def file_open(self):  # 9
        
        self.Data = []
        self.OnClear()
        
        with wx.FileDialog(self, "Choose a file to open", self.dirname,
                           "", "*.*", wx.OPEN) as dlg:
            if dlg.ShowModal() == wx.ID_OK:
                
                selection = dlg.GetPath()
                self.SetTitle(selection)
                f=open(selection)
                
                hdr = f.readline()
                
                for line in f:
                    #print line
                    #items = line.rstrip('\n').split(',')
                    items = line.rstrip('\n').split('\t')
                    vals = map(float, items)
                    pos = np.array(vals[0:3])
                    dir = np.array(vals[3:6])
                    if dir[1] < 0:
                        dir = -dir
                    mag = vals[6]
                    # x is North
                    # y is UP
                    # Z is East
                    r = sqrt(dir[0]*dir[0] + dir[2]*dir[2])
                    if r > 1.000:
                        ln = np.linalg.norm(dir)
                        dir /= ln
                        r   /= ln
                    theta = atan2(-dir[0], dir[2])
                    if theta < 0.0:
                        theta += 2.*pi
                    
                    self.Data.append({'pos':pos, 'dir':dir, 'radius':r, 'theta':theta, 'val':mag})
                f.close()
                
        # this function needs to load a file and initialize data for the plot panels.
        x = []
        y = []
        r = []
        theta = []
        val = []
        
        for pt in self.Data:
            x.append(pt['theta']*180./pi)
            y.append(atan2(pt['dir'][1],pt['radius'])*180./pi)
            r.append(pt['radius'])
            theta.append(pt['theta'])
            val.append(pt['val'])
            
        # filter results
        maxVal = np.max(val)
        m = 10.
        area = [ ((1.+1./m)*v/maxVal)**m for v in val ]        
        
        # send data to various plots
        self.pp1.SetData(x, y, r, theta, val, area)
        self.pp2.SetData(x, y, r, theta, val, area)
        self.pp3.SetData(x, y, r, theta, val, area)
        #self.pp4.SetData(x, y, r, theta, val)
        
    
    def OnRun(self,e):
        
        # create some random data 
        N = 200
        phi = np.pi * (np.random.rand(N) - 0.5)
        #theta = 2 * np.pi * (np.random.rand(N) - 0.5)
        theta = 2 * np.pi * (np.random.rand(N) )
        area = 10* np.random.rand(N)**2
        r = [cos(s) for s in phi]
        x = 180. * theta / np.pi
        y = 180. * phi / np.pi
        
        # send data to various plots
        self.pp1.SetData(x, y, r, theta, area)
        self.pp2.SetData(x, y, r, theta, area)
        self.pp3.SetData(x, y, r, theta, area)
        #self.pp4.SetData(x, y, r, theta, area)
        
    def OnClear(self,e=""):
        self.pp1.Clear()
        self.pp2.Clear()
        self.pp3.Clear()
        #self.pp4.Clear()
        
        
        
if __name__ == "__main__":
    myApp = wx.App()
    myFrame = StressVisualizer()
    myApp.MainLoop()
        