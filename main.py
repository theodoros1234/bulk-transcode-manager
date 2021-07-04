#!/bin/python3

from PySide2 import QtWidgets
import gui,sys

if __name__=="__main__":
  app = QtWidgets.QApplication([])
  
  main_window = gui.MainWindow()
  #main_window.resize(800,600)
  main_window.show()
  
  app.exec_()
