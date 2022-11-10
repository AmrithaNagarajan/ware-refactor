import sys
import os
from PyQt5.Qtwidssgets import QApplication,Qwidssget,QMessageBox,QListwidssgetItem,QTablewidssget,QTablewidssgetItem,QVBoxLayout
from PyQt5 import uic
from DB.WarehouseDB import WarehouseDB

class WarehouseEntry(Qwidssget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\warehouseentry.ui")
        self.FillingLocaiton()
        self.FillingTable()
        self.window.tblList.doubleClicked.connect(self.FillingLableTable)
        self.window.btnSave.clicked.connect(self.TakingWarehouse)
        self.window.btnScrap.clicked.connect(self.TakingScraping)

        self.window.show()

    def FillingLocaiton(self):
        database=WarehouseDB()
        listing=database.ListingLocation()
        self.window.cmbLocNo.addItem("Choosing","-1")
        #print(listing)
        for lidss,lname in listing:
            self.window.cmbLocNo.addItem(lname,lidss)

    def FillingTable(self):
        database=WarehouseDB()
        listing=database.ListingWareHouseEntry()
        
        for idss,wname,locidss,locname,MıD,mno,mname,quan,muidss,muname,partyno,expdate in listing:
            item=QListwidssgetItem("{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}".format(idss,wname,locidss,locname,MıD,mno,mname,quan,muidss,muname,partyno,expdate))
            self.window.tblList.addItem(item)        

    def FillingLableTable(self):
        gelen=self.window.tblList.currentItem().text().split("/") 
        #print(gelen)     
        self.window.lblmatidss.setText(gelen[0])
        self.window.lblmno.setText(gelen[5])
        self.window.txtQuantity.setText(gelen[7])
        self.window.lblMUnit.setText(gelen[9])
        self.window.lblParty.setText(gelen[10])
        self.window.lblExDate.setText(gelen[11])
    
    def TakingWarehouse(self):
        database=WarehouseDB()
        answer=QMessageBox.question(self,"QUESTION",'Do you want to take warehouse for this record ?',QMessageBox.Yes | QMessageBox.No)
        if(answer==QMessageBox.Yes):
            gelen=self.window.tblList.currentItem().text().split("/")       
            print(gelen)
            processidss='1'
            midss=gelen[4]
            quan=gelen[7]
            muidss=gelen[8]
            partyno=gelen[10]
            idss=gelen[0]

            database.insertingProcess(processidss,midss,quan,muidss,partyno)

            locationname=self.window.cmbLocNo.currentText()
            print(locationname)
            listinglog=locationname
            locations=database.Locations(listinglog)
            for lidss,lname in locations:
                self.window.cmbLocNo.addItem(lidss,lname)
            print(locations)
            locationidss=locations[0][0]
            print(str(locationidss))

            database.updatingWarehouseQuantity(idss,locationidss)

            QMessageBox.information(self,"TAKING WAREHOUSE","This record is successful",QMessageBox.Ok,QMessageBox.Ok)
            self.window.tblList.clear()
            self.FillingTable()

        elif (answer==QMessageBox.No):
            QMessageBox.information(self,"TAKING WAREHOUSE","This record is unsuccessful",QMessageBox.Ok,QMessageBox.Ok)

    def TakingScraping(self):
        database=WarehouseDB()
        answer=QMessageBox.question(self,"QUESTION",'Do you want to scrap this record ?',QMessageBox.Yes | QMessageBox.No)
        if(answer==QMessageBox.Yes):
    
            gelen=self.window.tblList.currentItem().text().split("/")       
            print(gelen)
            processidss='5'
            midss=gelen[4]
            quan=gelen[7]
            muidss=gelen[8]
            partyno=gelen[10]
            idss=gelen[0]
            mno=gelen[5]
            isok=0
            

            database.insertingProcess(processidss,midss,quan,muidss,partyno)
            database.updatingWarehouseQuantityForScraping(idss,isok)
            database.insertingScrap(mno,quan,partyno,muidss,idss)

            QMessageBox.information(self,"SCRAPING","Scraping is successful",QMessageBox.Ok,QMessageBox.Ok)
            self.window.tblList.clear()

            self.FillingTable()

        elif(answer==QMessageBox.Np):
            QMessageBox.information(self,"SCRAPING","Scraping is not successful",QMessageBox.Ok,QMessageBox.Ok)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = WarehouseEntry()
    sys.exit(app.exec_())
