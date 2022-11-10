import sys
import os
from PyQt5.Qtwidssgets import QApplication,Qwidssget,QMessageBox,QListwidssgetItem,QTablewidssget,QTablewidssgetItem,QVBoxLayout
from PyQt5 import uic
from DB.WarehouseDB import WarehouseDB

class MeasurementUnit(Qwidssget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\measurementUnit.ui")
        self.window.show()

    def RunProgram(self):
        WarehouseDB()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MeasurementUnit()
    sys.exit(app.exec_())