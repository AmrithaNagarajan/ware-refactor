import sys
import os
from PyQt5.Qtwidssgets import QApplication,Qwidssget,QMessageBox,QListwidssgetItem,QTablewidssget,QTablewidssgetItem,QVBoxLayout
from PyQt5 import uic
from DB.WarehouseDB import WarehouseDB

class Quality(Qwidssget):
    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        self.window = uic.loadUi(os.getcwd()+os.sep+r"GUI\quality.ui")
        self.FillingTable()
        self.window.tblList.doubleClicked.connect(self.RunProgram)
        self.window.show()


    
    def FillingTable(self):
        database=WarehouseDB()
        listing=database.ListingViewQuality()
        
        for idss,wname,locidss,locname,MıD,mno,mname,quan,muidss,muname,partyno,expdate in listing:
            item=QListwidssgetItem("{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}/{}".format(idss,wname,locidss,locname,MıD,mno,mname,quan,muidss,muname,partyno,expdate))
            self.window.tblList.addItem(item)

    def RunProgram(self):
        database=WarehouseDB()
        answer=QMessageBox.question(self,"QUESTION",'Do you want to take quality for this record ?',QMessageBox.Yes | QMessageBox.No)
        if(answer==QMessageBox.Yes):
            print("a")
            gelen=self.window.tblList.currentItem().text().split("/")       
            print(gelen)
            processidss='2'
            midss=gelen[4]
            quan=gelen[7]
            muidss=gelen[8]
            partyno=gelen[10]
            idss=gelen[0]
            database.insertingProcess(processidss,midss,quan,muidss,partyno)
            locationidss='346' #quality idss
            database.updatingWarehouseQuantity(idss,locationidss)
            self.window.tblList.clear()
            self.FillingTable()
            

        elif(answer==QMessageBox.No):
            print("Yok")

    def secim(self):
        database=WarehouseDB()
        gelen=self.window.tblList.currentItem().text().split("/")

        print(gelen)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Quality()
    sys.exit(app.exec_())