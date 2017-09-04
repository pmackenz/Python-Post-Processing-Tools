'''
Created on Nov 19, 2014

@author: Smit Kamal & Peter Mackenzie-Helnwein
'''
import wx

#from StressVisualizer_ver5 import *
from StressVisualizer import *

if __name__ == "__main__":
    myApp = wx.App()
    myFrame = StressVisualizer()
    myApp.MainLoop()