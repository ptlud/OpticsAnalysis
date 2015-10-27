# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 16:13:47 2015

@author: ludingpd
"""
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import numpy as np

#data = {}
#data = {'Surface':['1','2','3'], 'Radius':['4','5','6'], 'Thickness':['7','8','9']}
 
def initSurfStruct(numSurfaces):                   # Initialize lens surface structure

    surfData = {}                   # Initialize the dictionary/struct
    
    surfData['num'] = 0
    surfData['radius'] = 0.0
    surfData['thick'] = 0.0
    surfData['glass'] = 'Air'
    surfData['semi'] = 0.0
    surfData['conic'] = 0.0

    surfData = np.repeat(np.array(surfData),numSurfaces) 
    for i in range(numSurfaces):
        surfData[i]['num'] = i
    
    return surfData
    

def initSysStruct():
    sysData = {}
    
    sysData['stopSurf'] = 1
    sysData['wave'] = np.zeros(1)
    sysData['weight'] = np.zeros(1)
    sysData['fieldType'] = 'ObjHeight'
    sysData['fieldX'] = np.zeros(1)
    sysData['fieldY'] = np.zeros(1)
    sysData['aperType'] = 'EPD'
    sysData['vigX'] = np.ones(1)
    sysData['vigY'] = np.ones(1)
    
    return sysData
    
    
class MyTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.resize(800, 300)
        self.setWindowTitle('Lens Data Editor')
        self.data = data
        self.setmydata()
#        self.resizeColumnsToContents()
        self.resizeRowsToContents()
        
        self.insertButton = QPushButton('Insert',self)
        self.insertButton.clicked.connect(self.insertSurf)
        self.insertButton.move(50,220)
        
        self.deleteButton = QPushButton('Delete',self)
        self.deleteButton.clicked.connect(self.deleteSurf)
        self.deleteButton.move(150,220)

    def setmydata(self):
        horizHeaders = ['Surface','Radius','Thickness', 'Glass','Semi-Diameter','Conic']
        vertHeaders = ['Obj','1','2','STO','4','Img']
                
        for n, key in enumerate(sorted(self.data.keys())):
#            self.setColumnWidth(n,20)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                self.setItem(m, n, newitem)
                
        self.setHorizontalHeaderLabels(horizHeaders)
        self.setVerticalHeaderLabels(vertHeaders)
    
    def insertSurf(self):
        rowPosition = self.rowCount()
        print 'Insert', rowPosition
        self.insertRow(rowPosition)

        self.selectRow(rowPosition)
        
    def deleteSurf(self):
        print 'Delete'
        self.removeRow(2)
        self.selectRow(2)
 
 
def main(args):
    surfData = initSurfStruct(3)       # Initialize surface dict array
    sysData = initSysStruct()           # Initialize system dict
    
    app = QApplication(args)
    table = MyTable(surfData)
    table.show()
    sys.exit(app.exec_())
 
 
if __name__=="__main__":
    main(sys.argv)