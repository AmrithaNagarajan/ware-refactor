import sys
import os
from PyQt5.Qtwidssgets import QApplication,Qwidssget,QMessageBox,QListwidssgetItem,QTablewidssget,QTablewidssgetItem,QVBoxLayout
from PyQt5 import uic
from DB.WarehouseDB import WarehouseDB

class LocationTransfer(Qwidssget):
    def __init__(self):
        super().__init__()
        self.InitUI()
        
    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\locationtransfer.ui")
        self.FillingTable()
        self.window.tblList.doubleClicked.connect(self.FillingLableTable)
        self.window.btnSave.clicked.connect(self.RunProgram)

        self.window.show()



    def FillingTable(self):
        database=WarehouseDB()
        listing=database.ListingViewWarehouse()
        
        for idss,wname,locidss,locname,MıD,mno,mname,quan,muidss,muname,partyno,expdate in listing:
            item=QListwidssgetItem("{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}".format(idss,wname,locidss,locname,MıD,mno,mname,quan,muidss,muname,partyno,expdate))
            self.window.tblList.addItem(item) 

    def FillingLableTable(self):
        database=WarehouseDB()

        gelen=self.window.tblList.currentItem().text().split("/") 
        print(gelen)     
        
        self.window.lblmatidss.setText(gelen[0])
        self.window.lblLocNo.setText(gelen[3])
        self.window.lblmno.setText(gelen[5])
        self.window.lblQuantity.setText(gelen[7])
        self.window.lblMUnit.setText(gelen[9])
        self.window.lblParty.setText(gelen[10])
        self.window.lblExDate.setText(gelen[11])

        wname="WAREHOUSE"
        locclicked=str(gelen[3])
        listing=database.ListingLocationWithCondtion(wname,locclicked)
        self.window.cmbLocNo.addItem("Choosing","-1")
        #print(listing)
        for lidss,lname in listing:
            self.window.cmbLocNo.addItem(lname,lidss)
    
    def RunProgram(self):
        database=WarehouseDB()
        answer=QMessageBox.question(self,"LOCATION TRANSFER",'Do you want to tranfer for this record ?',QMessageBox.Yes | QMessageBox.No)
        if(answer==QMessageBox.Yes):

            gelen=self.window.tblList.currentItem().text().split("/")
            processidss='8'
            midss=gelen[4]
            quan=gelen[7]
            muidss=gelen[8]
            partyno=gelen[10]
            expdate=gelen[11]
            idss=gelen[0]
            quannew=self.window.txtQuantity.text()
            locname=self.window.cmbLocNo.currentText()
            locidss=str(database.ListingLocation_V2 (locname)[0][0])   
            isok=0

            quanupdate=int(quan)-int(quannew)
            if(quannew>quan):
                QMessageBox.Warning(self,"LOCATION TRANSFER","Quantity updated is bigger than quantity",QMessageBox.Ok,QMessageBox.Ok)

            else:
                database.insertingProcess(processidss,midss,quan,muidss,partyno)
                database.insertingWarehouseQuantity(locidss,midss,quannew,muidss,partyno,expdate)  
                if(quanupdate==0):
                    database.updatingWarehouseQuantityWithQuantityisok(idss,quanupdate,isok)   
                else:      
                    database.updatingWarehouseQuantityWithQuantity(idss,quanupdate)
                QMessageBox.information(self,"LOCATION TRANSFER","This transfer is successful",QMessageBox.Ok,QMessageBox.Ok)
                self.window.tblList.clear()
                self.FillingTable()



        elif (answer==QMessageBox.No):
            QMessageBox.information(self,"LOCATION TRANSFER","This transfer is unsuccessful",QMessageBox.Ok,QMessageBox.Ok)





    #VALUE=["'"+locidss+"'","'"+matidss+"'","'"+quan+"'","'"+muidss+"'","'"+partyno+"'","'"+expdate+"'"]))




#                VALUE=["'"+locidss+"'","'"+matidss+"'","'"+quan+"'","'"+muidss+"'","'"+partyno+"'","'"+expdate+"'"]))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = LocationTransfer()
    sys.exit(app.exec_())