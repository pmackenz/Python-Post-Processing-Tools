'''
Created on Dec 19, 2016

@author: Smit Kamal & Peter Mackenzie-Helnwein
'''
from IDs import *


import matplotlib.pyplot as plt
from math import asin, pi
import numpy as np


        
class RectPlot(object):
    
    
    def __init__(self,ID=-1):
        
        
        #self.maw=PARENT
        self.Reset()
        
        self.fig = plt.figure(figsize=(8.0,5.0), dpi=300, tight_layout=True)
        
        #self.toolbar.Realize()
        self.initAxes()
        self.SetLimits()
        self.SetGrid()

        
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
        self.ax.set_xlim(0,24.0)
        #self.ax.set_ylim(-95, 95)
        #self.ax.set_ylim(-5, 95)
        
    def SetGrid(self):

        self.ax.grid(True,which='major',axis='both')
        self.ax.xticks([0,6,12,18,24],["00:00","6:00","12:00","18:00","24:00"])
                                                
    def SetData(self, x, y, r, theta, val,dia,time, area=[]):
        if area == []:
            area = val
        self.dataX   = x
        self.dataY   = y
        self.dataR   = r
        self.dataTh  = theta
        self.dataArea = [ 10. * i for i in area ]
        self.dataVal = val
        self.initAxes()
        self.c = self.ax.scatter(self.dataX, self.dataY, c=self.dataVal, s=self.dataArea, linewidth=0,alpha=0.75)
        self.ax.set_title('{} cm diameter boulder at {} hours'.format(dia,time),y=1.07)
        cbr=self.fig.colorbar(self.c,pad=0.1,shrink=0.8)
        cbr.set_label('    MPa')
        plt.xlabel('longitude (degrees from north)')
        plt.ylabel('latitude (degrees)')
        self.SetLimits()
        self.SetGrid()
        #plt.show()
        
    
    def Reset(self):
        self.dataR    = []
        self.dataTh   = []
        self.dataVal  = []
        self.dataArea = []
        
    def saveplot(self,dia,inc):
        self.fig.savefig('{}_R_{}.pdf'.format(dia,inc))
        self.fig.savefig('{}_R_{}.png'.format(dia,inc))
        
