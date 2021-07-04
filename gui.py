from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import Qt

# Main window
class MainWindow(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()
    
    # Main window container
    self.outerContainer = QtWidgets.QVBoxLayout(self)
    self.setLayout(self.outerContainer)
    
    # Worker list container
    self.workerContainer = QtWidgets.QVBoxLayout(self)
    self.outerContainer.addLayout(self.workerContainer)
    self.workerLabel = QtWidgets.QLabel("Workers")
    self.workerList = QtWidgets.QTableView()
    self.workerContainer.addWidget(self.workerLabel)
    self.workerContainer.addWidget(self.workerList)
    
    # Worker list header
    self.workerListHeader = QtWidgets.QHeaderView(Qt.Horizontal)
    self.workerList.setHorizontalHeader(self.workerListHeader)
    
    # Worker list buttons
    self.workerButtonContainer = QtWidgets.QHBoxLayout(self)
    self.workerContainer.addLayout(self.workerButtonContainer)
    
    self.workerButtonAdd = QtWidgets.QPushButton("&Add",self)
    self.workerButtonEdit = QtWidgets.QPushButton("&Edit",self)
    self.workerButtonRemove = QtWidgets.QPushButton("&Remove",self)
    self.workerButtonContainer.addWidget(self.workerButtonAdd)
    self.workerButtonContainer.addWidget(self.workerButtonEdit)
    self.workerButtonContainer.addWidget(self.workerButtonRemove)
    
  #@QtCore.Slot()
