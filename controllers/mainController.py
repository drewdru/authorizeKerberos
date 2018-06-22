#!./env/bin/python
# -*- coding: utf-8 -*-
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '../..'))

from PyQt5.QtCore import QObject, pyqtSlot, QDir, QCoreApplication
from PyQt5.QtQml import QJSValue

class MainController(QObject):
    """ Controller for main view """
    def __init__(self, appDir=None):
        QObject.__init__(self)
        self.appDir = QDir.currentPath() if appDir is None else appDir
        self.callback = []

    @pyqtSlot(str)
    def log(self, s):
        """ PyConsole
            @param s: The string
        """
        print(s)