import sys
import os
from PyQt5.Qtwidssgets import QApplication,Qwidssget,QMessageBox,QListwidssgetItem,QTablewidssget,QTablewidssgetItem,QVBoxLayout
from PyQt5 import uic
from DB.WarehouseDB import WarehouseDB

class WarehouseType(Qwidssget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\warehousetype.ui")
        self.FillinWareHouseName()
        self.window.show()

    def RunProgram(self):
        database=WarehouseDB()


    def FillinWareHouseName(self):
        database=WarehouseDB()
        listing=database.ListingWarehouseName()
        self.window.cmbwname.addItem("Choosing","-1")
        print(listing)
        for widss,wname in listing:
            self.window.cmbwname.addItem(wname,widss)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WarehouseType()
    sys.exit(app.exec_())