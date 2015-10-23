# -*- coding: utf-8 -*-
"""
Created on Mon Mar 09 10:20:35 2015

@author: JCWillia

"""

import sys

# import PyQt4 QtCore and QtGui modules
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from table import MainTable

if __name__ == '__main__':
     # create application
    app = QApplication(sys.argv)
    app.setApplicationName('Optics Input Table')
    
    # create widget
    win = MainTable()
    
    # set app icon    
    app_icon = QIcon()
    app_icon.addFile('icons/apollo_icon (16x16).jpg', QSize(16,16))
    app_icon.addFile('icons/apollo_icon (24x24).jpg', QSize(24,24))
    app_icon.addFile('icons/apollo_icon (32x32).jpg', QSize(32,32))
    app_icon.addFile('icons/apollo_icon (48x48).jpg', QSize(48,48))
    app_icon.addFile('icons/apollo_icon (256x255).jpg', QSize(256,255))
    app.setWindowIcon(app_icon)
    
    # connection
    QObject.connect(app, SIGNAL('lastWindowClosed()'), app, SLOT('quit()'))
    
    # execute application
    sys.exit(app.exec_())