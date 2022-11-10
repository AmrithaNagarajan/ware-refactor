import sys
import os
from PyQt5.Qtwidssgets import QApplication,Qwidssget,QMessageBox,QListwidssgetItem,QTablewidssget,QTablewidssgetItem,QVBoxLayout
from PyQt5 import uic
from DB.WarehouseDB import WarehouseDB
from materialEntry import MaterialEntry
from quality import Quality
from locationTranfer import LocationTransfer
from warehouseEntry import WarehouseEntry

class MainMenu(Qwidssget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\mainmenu.ui")
        self.window.actionMaterial_Entry.triggered.connect(self.OpenMaterialEntry)
        self.window.actionQuality_2.triggered.connect(self.OpenQuality)
        self.window.actionLocation_Transfer.triggered.connect(self.OpenLocationTransfer)
        self.window.actionWarehouse_Entry.triggered.connect(self.OpenWarehouseEntry)

        self.window.show()

    def FillingTable(self):
        WarehouseDB()

    def OpenMaterialEntry(self):
        self.materialEntry=MaterialEntry()

    def OpenQuality(self):
        self.quality=Quality()

    def OpenLocationTransfer(self):
        self.locationTranfer=LocationTransfer()

    def OpenWarehouseEntry(self):
        self.warehouseEntry=WarehouseEntry()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainMenu()
    sys.exit(app.exec_())
