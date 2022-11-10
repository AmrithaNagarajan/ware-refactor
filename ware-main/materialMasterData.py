import sys
import os
from PyQt5.Qtwidssgets import QApplication,Qwidssget,QMessageBox,QListwidssgetItem,QTablewidssget,QTablewidssgetItem,QVBoxLayout
from PyQt5 import uic
from DB.WarehouseDB import WarehouseDB

#warehouse dbden okumuyor

class MaterialMasterDataUI(Qwidssget):
    def __init__(self):
        super().__init__()
        self.InitUI()
    
    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\materialmasterdata.ui")
        self.window.btnSave.clicked.connect(self.RunProgram)

        self.window.cmbmeaunit.currentIndexChanged.connect(self.cmbDegisti)

        self.FillingMeasurementUnit()
        self.FillingMaterialType()

        self.window.show()

    def RunProgram(self):
        
        database=WarehouseDB()
        
        database.insertMaterialMasterData("aa","aa",1,2,5)

    def FillingMeasurementUnit(self):
        database=WarehouseDB()
        listing=database.ListingMeasurementUnit()
        self.window.cmbmeaunit.addItem("Choosing","-1")
        print(listing)
        #SORUN BAKILACAK
        
        for meauniidss,meaunit in listing:
            self.window.cmbmeaunit.addItem(meaunit,meauniidss)

    def FillingMaterialType(self):
        database=WarehouseDB()
        listing=database.ListingMaterialType()
        self.window.cmbmattype.addItem("Choosing","-1")
        print(listing)

    def FillingTable(self):
        database=WarehouseDB()
        listing=database.ListingMaterialMasterData()
        print(listing)

    def cmbDegisti(self):
        print(self.window.cmbmeaunit.currentText())
        print(self.window.cmbmeaunit.currentIndex())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MaterialMasterDataUI()
    sys.exit(app.exec_())

    
