#!./env/bin/python
# -*- coding: utf-8 -*-
import sys
import os
import dependencies_gui
dependencies_gui.update_packages()

from PyQt5.QtQml import QQmlEngine
from PyQt5.QtCore import QUrl, QDir 
# from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import QQuickView
from PyQt5.QtGui import QGuiApplication, QIcon

from controllers.mainController import MainController

def main():
    # Create main app
    myApp = QGuiApplication(sys.argv)
    # myApp.setWindowIcon(QIcon('./images/icon.png'))

    # Create a View and set its properties
    appView = QQuickView()
    appView.setMinimumHeight(640)
    appView.setMinimumWidth(1024)
    appView.setTitle('Authorize Kerberos')

    engine = appView.engine()
    engine.quit.connect(myApp.quit)
    context = engine.rootContext()

    # add paths
    appDir = 'file:///' + QDir.currentPath()
    context.setContextProperty('appDir', appDir)

    # add controllers
    mainController = MainController()
    context.setContextProperty('PyConsole', mainController)
    context.setContextProperty('mainController', mainController)

    # Show the View
    appView.setSource(QUrl('./qml/main.qml'))
    appView.showMaximized()

    # Execute the Application and Exit
    myApp.exec_()
    sys.exit()

if __name__ == '__main__':
    main()