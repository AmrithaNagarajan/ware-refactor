import sys
import os
from PyQt5.Qtwidssgets import QApplication,Qwidssget,QMessageBox,QListwidssgetItem,QTablewidssget,QTablewidssgetItem,QVBoxLayout
from PyQt5 import uic
from DB.WarehouseDB import WarehouseDB
from datetime import datetime


class MaterialEntry(Qwidssget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\materialentry.ui")
        self.FillingMeasurement()
        self.FillingTable()
        self.FillingMaterilNo()
        self.window.btnSave.clicked.connect(self.RunProgram)
        self.window.tblList.doubleClicked.connect(self.FillingLableTable)

        self.window.show()

    def FillingTable(self):
        database=WarehouseDB()
        listing=database.ListingViewMaterialEntry()
        for idss,matidss,matno,matname,quan,muiname,entdate,partyno,expdate in listing:
            item = QListwidssgetItem("{}/{}/{}/{}/{}/{}/{}/{}/{}".format(idss,matidss,matno,matname,quan,muiname,entdate,partyno,expdate))
            self.window.tblList.addItem(item)

    def FillingLableTable(self):
        gelen=self.window.tblList.currentItem().text().split("/")       
        print(gelen)
        deneme = gelen[0]
        print(deneme)
        self.window.lblmatidss.setText(gelen[0])
        self.window.cmbmno.setCurrentText(gelen[2])
        self.window.txtQuantity.setText(gelen[4])
        self.window.txtParty.setText(gelen[7])
        self.window.cmbmeaunit.setCurrentText(gelen[5])


    def FillingMeasurement(self):
        database=WarehouseDB()
        listing=database.ListingMeasurementUnit()
        self.window.cmbmeaunit.addItem("Choosing","-1")
        print(listing)
        for midss,muname in listing:
            self.window.cmbmeaunit.addItem(muname,midss)

    def FillingMaterilNo(self):
        database=WarehouseDB()
        listing=database.ListingMaterialNo()
        self.window.cmbmno.addItem("Choosing","-1")
        print(listing)
        for midss,mno in listing:
            self.window.cmbmno.addItem(mno,midss)

    def RunProgram(self):
        database=WarehouseDB()
        #current indexte se.ilen ile farklı değer geliyor
        
        
        midss=self.window.cmbmno.currentIndex()
        midss=str(midss)
        print(midss)
        print(database.ListingMaterialNo())
        print(self.window.cmbmno.currentIndex())
        quan=self.window.txtQuantity.text()
        muidss="1"
        muidss=str(muidss)
        print(muidss)
        
        party=self.window.txtParty.text()
        expdate=self.window.dtexpdate.text()

        answer=QMessageBox.question(self,"SAVING MATERIAL ENTRY","Do you want to save this record",QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if(answer==QMessageBox.Yes):
            if(database.insertingMaterialEntry(midss,quan,muidss,party,expdate)):
                database.insertingProcess("7",midss,muidss,quan,party)
                QMessageBox.information(self,"SAVING MATERIAL ENTRY","Saving Successful",QMessageBox.Ok,QMessageBox.Ok)
        elif(answer==QMessageBox.No):
            QMessageBox.information(self,"SAVING MATERIAL ENTRY","Saving Nonsuccessful",QMessageBox.Ok,QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MaterialEntry()
    sys.exit(app.exec_())