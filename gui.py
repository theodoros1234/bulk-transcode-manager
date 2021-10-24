from PySide2.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QTableView, QHeaderView, QPushButton
from PySide2.QtCore import Qt, Slot

# Main window
class MainWindow(QWidget):
  def __init__(self):
    super().__init__()
    
    # Main window container
    self.outerContainer = QVBoxLayout(self)
    self.setLayout(self.outerContainer)
    
    # Worker list container
    self.workerContainer = QVBoxLayout(self)
    self.outerContainer.addLayout(self.workerContainer)
    self.workerLabel = QLabel("Workers")
    self.workerList = QTableView()
    self.workerContainer.addWidget(self.workerLabel)
    self.workerContainer.addWidget(self.workerList)
    
    # Worker list header
    self.workerListHeader = QHeaderView(Qt.Horizontal)
    self.workerList.setHorizontalHeader(self.workerListHeader)
    
    # Worker list buttons
    self.workerButtonContainer = QHBoxLayout(self)
    self.workerContainer.addLayout(self.workerButtonContainer)
    
    self.workerButtonAdd = QPushButton("&Add",self)
    self.workerButtonEdit = QPushButton("&Edit",self)
    self.workerButtonRemove = QPushButton("&Remove",self)
    self.workerButtonContainer.addWidget(self.workerButtonAdd)
    self.workerButtonContainer.addWidget(self.workerButtonEdit)
    self.workerButtonContainer.addWidget(self.workerButtonRemove)
    
  #@Slot()
