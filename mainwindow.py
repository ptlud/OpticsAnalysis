# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:28:06 2015

@author: JCWillia

"""


#Importing the pyqt library for gui operations
#from PyQt4 import uic
from PyQt4.QtGui import *

## To compile the .ui file to a .py prior to importing it here, run this line in the CMD terminal in the directory containing .ui version of the GUI from Qt Design. 
# pyuic4 moistureConversionGUI.ui -o moistureConversionGUI.py 
# Now we would import the ui file like any other python class
import mainWindow_UI

## Direct import method from .ui
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

# create the class MainWindow which will run the GUI
class MainWindow(QMainWindow):
    
    # initial method that only runs once upon creation of the class object
    def __init__(self, parent = None):
        QMainWindow.__init__(self, parent)

        # (Personal preference) importing the compiled .py GUI file from the ui file into the MainWindow Class
        self.win = mainWindow_UI.QtGui.QMainWindow()
        self.uiplot = mainWindow_UI.Ui_MainWindow()
        self.uiplot.setupUi(self.win)
        
        self.uiplot.actionOptic_Input_Data.triggered.connect(self.initializeTableInput)

    def initializeTableInput(self):
        
    def importMethod(self):
        print("import button clicked!")
        
        self.filepath = str(QFileDialog.getOpenFileName())
        self.wb = Workbook(self.filepath)     
        
        self.data = Range('Sheet1','A2', asarray=True).table.value
        
#        print self.data
        
        for m in np.arange(0,len(self.data)):
            self.dataTable.insertRow(self.dataTable.rowCount())
                        
            for n in np.arange(0,len(self.colnames)-1):            
                newitem = QTableWidgetItem(str(self.data[m,n]))                
                self.dataTable.setItem(m,n,newitem)
                
        # Enable convert button
        self.convertPushButton.setEnabled(True)
        
        self.plotPushButton.setEnabled(False)
    def convertMethod(self):
        print("convert button clicked!")
        self.dewPoint = spray.Dew_point_func(self.data[:,1],self.data[:,0])
        self.dewPoint = self.dewPoint[:,np.newaxis]
        
        self.data = np.hstack((self.data, self.dewPoint))
        
        for m in np.arange(0,len(self.data)):  
            self.dataTable.setItem(m,2,QTableWidgetItem(str(self.data[m,2])))
        
        self.plotPushButton.setEnabled(True)
        
    def plotMethod(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        
        surf = ax.plot_trisurf(self.data[:,0], self.data[:,1], self.data[:,2], cmap=cm.jet, linewidth=0.2)
        fig.colorbar(surf, shrink=0.5, aspect=5,label = 'Dew Point [C]')     
        ax.set_xlabel('Temperature [C]')
        ax.set_ylabel('Relative Humidity [%]')
        ax.set_zlabel('Dew Point [C]')
        ax.view_init(elev=10., azim=-135)
        plt.show()
        
    def savexlsMethod(self):
        print('Saving excel File')
        self.saveNameExcel = os.path.splitext(str(self.filepath).split("/")[-1])[0]

        wbOut = Workbook()
        
        Range('A1').value = ['Tempature [C]','Relative Humidity [%]','Dew Point [C]']
        Range('A2').value = self.data
              
        wbOut.save()

    def savepltMethod(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        surf = ax.plot_trisurf(self.data[:,0], self.data[:,1], self.data[:,2], cmap=cm.jet, linewidth=0.2)
        fig.colorbar(surf, shrink=0.5, aspect=5,label = 'Dew Point [C]')     
        ax.set_xlabel('Temperature [C]')
        ax.set_ylabel('Relative Humidity [%]')
        ax.set_zlabel('Dew Point [C]')
        ax.view_init(elev=10., azim=-135)
        savefig('OuputImage.png')
