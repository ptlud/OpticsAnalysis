# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:28:06 2015

@author: JCWillia

"""


#Importing the pyqt library for gui operations
from PyQt4 import uic
from PyQt4.QtGui import *

## To compile the .ui file to a .py prior to importing it here, run this line in the CMD terminal in the directory containing .ui version of the GUI from Qt Design. 
# pyuic4 moistureConversionGUI.ui -o moistureConversionGUI.py 
## Now we would import the ui file like any other python class
#import moistureConversionGUI

# Direct import method from .ui
#(Ui_MainWindow, QMainWindow) = uic.loadUiType('moistureConversionGUI.ui')

#importing os library 
import os

# import xlwings for excel file handling
from xlwings import Range, Workbook

#Importing matplotlib tools for plotting the 3d surface
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
from pylab import savefig

#import numpy for array operations
import numpy as np

import inputTable_UI
# create the class MainWindow which will run the GUI
class MainTable(QWidget):
    
    # initial method that only runs once upon creation of the class object
    def __init__(self, parent = None):
        QWidget.__init__(self, parent)

        # (Personal preference) importing the compiled .py GUI file from the ui file into the MainWindow Class
        self.win = inputTable_UI.QtGui.QWidget()
        self.uiplot = inputTable_UI.Ui_Form()
        self.uiplot.setupUi(self.win)
        self.win.show()
        self.win.setWindowTitle('Optics Input Table')
        
        self.uiplot.insert_row.clicked.connect(self.addRows)
        self.uiplot.DeleteCurrentRow.clicked.connect(self.delRows)
        self.inputTable = self.uiplot.tableWidget
        
    def addRows(self):
        self.inputTable.insertRow(self.inputTable.rowCount())

    def delRows(self):
        self.inputTable.removeRow(self.inputTable.currentRow())    
