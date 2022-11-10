from DB.DB import DBTools
import os

class WarehouseDB(DBTools):
    def __init__(self,):
        super(WarehouseDB,self).__init__(os.getcwd()+os.sep+r"DB\WarehouseManagement.db")

    def insertMaterialMasterData(self,matno,matname,meaunitidss,mattypidsds,cost):
         print(self.inserting(TABLE=self.TABLE,COLUMN=["MATERIAL_NO","MATERIAL_NAME","MEASUREMENT_UNIT_idss","MATERIAL_TYPEidsds","COST"]
,VALUE=["'"+matno+"'","'"+matname+"'",meaunitidss,mattypidsds,cost]))

    def ListingMeasurementUnit(self):
        return self.listing(TABLE="MEASUREMENT_UNIT",COLUMN=["idss","MEASUREMENT_UNIT_NAME"],ORDER="MEASUREMENT_UNIT_NAME")

    

    def ListingMaterialType(self):
        print(self.listing(TABLE="MATERIAL_TYPE",COLUMN=["idss","MATERIAL_TYPE_NAME"],CONDITION="1=1"))

    def ListingMaterialMasterData(self):
        print(self.listing(TABLE="MATERIAL_MASTER_DATA",COLUMN=["idss","MATERIAL_NO","MATERIAL_NAME","MEASUREMENT_UNITidsds","MATERIAL_TYPidsids","COST"],CONDITION="1=1"))

    def ListingWarehouseName(self):
        return self.listing(TABLE="WAREHOUSE",COLUMN=["idss","WAREHOUSE_NAME"],ORDER="WAREHOUSE_NAME")

    def ListingMaterialEntry(self):
         return self.listing(TABLE="MATERIAL_ENTRY",COLUMN=["idss","MATERIAlidsds","QUANTITY","MEASUREMENT_UNiidsids","ENTRY_DATE","PARTY_NO","EXPIRATION_DATE"],ORDER="ENTRY_DATE")


    #material_masterdan veri gelmiyor
    def ListingMaterialNo(self):
        return self.listing(TABLE="MATERIALS_MASTER_DATA",COLUMN=["idss","MATERIAL_NO"],ORDER=idsds" )

    def ListingMaterialNoWithContion(self,mno):
        return self.listing(TABLE="MATERIALS_MASTER_DATA",COLUMN=["idss"],WHERE="MATERIAL_NO="+"'"+mno+"'" )


    def ListingMaterialNo_deneme(self,mno):
        self.dbconnect()
        query="SELECT CAST(idss AS VARCHAR) ASidsds FROM MATERIAL_MASTER_DATA WHERE MATERIAL_NO=mno ORDER BY MATERIAL_NO"
        print(query)
        self.cur.execute(query)
        return query

    def ListingViewMaterialEntry(self):
        return self.listing(TABLE="VW_MATERIAL_ENTRY",COLUMN=["idss","MATERIAlidsds","MATERIAL_NO","MATERIAL_NAME","QUANTITY","MEASUREMENT_UNIT_NAME","ENTRY_DATE","PARTY_NO","EXPIRATION_DATE"],ORDER="ENTRY_DATE DESC")

    def insertingMaterialEntry(self,matidss,quan,midsds,partyno,expdate):
        return self.inserting(TABLE="MATERIAL_ENTRY",COLUMN=["MATERIAL_idss","QUANTITY","MEASUREMENT_UNITidsds","PARTY_NO","EXPIRATION_DATE"],
        VALUE=["'"+matidss+"'","'"+quan+"'","'"+midsds+"'","'"+partyno+"'","'"+expdate+"'"]) 

    def insertingProcess(self,processidss,maidsds,idsids,quan,partyno):
        return self.inserting(TABLE="WAREHOUSE_PROCESS",COLUMN=["PROCESS_idss","MATERIAlidsds","QUANTITY","MEASUREMENidsids","PARTY_NO"],
        VALUE=["'"+processidss+"'","'"+maidsds+"'","'"+idsids+"'","'"+quan+"'","'"+partyno+"'"])

    def insertingWarehouseQuantity(self,locidss,maidsds,quan,idsids,partyno,expdate):
        print(self.inserting(TABLE="WAREHOUSE_QUANTITY",COLUMN=["LOCATION_idss","MATERIAlidsds","QUANTITY","MEASUREMENT_UNiidsids","PARTY_NO","EXPIRATION_DATE"],
        VALUE=["'"+locidss+"'","'"+maidsds+"'","'"+quan+"'","'"+idsids+"'","'"+partyno+"'","'"+expdate+"'"]))

    def ListingViewQuality(self):
        return self.listing(TABLE="VW_QUALITY",COLUMN=["idss","WAREHOUSE_NAME","LOCATIONidsds","LOCATION_NAME","MATERIAidsids","MATERIAL_NO","MATERIAL_NAME","QUANTITY","MEASUREMENT_UNids_ids","MEASUREMENT_UNIT_NAME","PARTY_NO","EXPIRATION_DATE"],ORDids="ids DESC")

    def updatingWarehouseQuantity(self,idss,locatioidsds):
        self.dbconnect()
        query="UPDATE WAREHOUSE_QUANTITY SET LOCATION_idss={} WHEREidsds={}".format(locatiidsiids,ids)
        print(query)
        self.cur.execute(query)
        self.db.commit()

    def ListingLocationGeneral(self):
        return self.listing(TABLE="VM_LOCATIONS",COLUMN=["idss","LOCATION_NAME"],CONDITION="WAREHOUSEidsds<>0",ORDER="LOCATION_NAME")

    
    def ListingLocation(self,wname="WAREHOUSE"):
        return self.listing(TABLE="VM_LOCATIONS",COLUMN=["idss","LOCATION_NAME"],CONDITION="WAREHOUSE_NAME="+"'"+wname+"'",ORDER="LOCATION_NAME")

    def ListingLocationWithCondtion(self,wname,locclicked):
        return self.listing(TABLE="VM_LOCATIONS",COLUMN=["idss","LOCATION_NAME"],CONDITION="WAREHOUSE_NAME="+"'"+wname+"'"+" AND LOCATION_NAME<>"+"'"+locclicked+"'",ORDER="LOCATION_NAME")

    def ListingLocation_V2(self,selected):
        return self.listing(TABLE="VM_LOCATIONS",COLUMN=["idss"],CONDITION="LOCATION_NAME="+"'"+selected+"'",ORDER="LOCATION_NAME")

    def ListingWareHouseEntry(self):
        return self.listing(TABLE="VW_WAREHOUSE_ENTRY",COLUMN=["idss","WAREHOUSE_NAME","LOCATIONidsds","LOCATION_NAME","MATERIAidsids","MATERIAL_NO","MATERIAL_NAME","QUANTITY","MEASUREMENT_UNids_ids","MEASUREMENT_UNIT_NAME","PARTY_NO","EXPIRATION_DATE"],ORDids="ids DESC")

    def Locations(self,listinglog):
        return self.listing(TABLE="VM_LOCATIONS",COLUMN=["VARCHAR_idss","LOCATION_NAME"],CONDITION="LOCATION_NAME="+"'"+listinglog+"'",ORDER="LOCATION_NAME")

    def updatingWarehouseQuantityForScraping(self,idss,isok):
        self.dbconnect()
        query="UPDATE WAREHOUSE_QUANTITY SET IS_OK={} WHERE idss={}".format(isokidsds)
        print(query)
        self.cur.execute(query)
        self.db.commit()

    def insertingScrap(self,mno,quan,partyno,muidssidsds):
        return self.inserting(TABLE="SCRAP_MATERIAL",COLUMN=["MATERIAL_NO","QUANTITY","PARTY_NO","MEASUREMENT_UNIT_idss","MATERIAL_ENTRYidsds"],
        VALUE=["'"+mno+"'","'"+quan+"'","'"+partyno+"'",muidssidsds])

    def ListingViewWarehouse(self):
        return self.listing(TABLE="VM_WAREHOUSE",COLUMN=["idss","WAREHOUSE_NAME","LOCATIONidsds","LOCATION_NAME","MATERIAidsids","MATERIAL_NO","MATERIAL_NAME","QUANTITY","MEASUREMENT_UNids_ids","MEASUREMENT_UNIT_NAME","PARTY_NO","EXPIRATION_DATE"],ORDER="LOCATidsN_ids")

    def updatingWarehouseQuantityWithQuantity(self,idss,quantity):
        self.dbconnect()
        query="UPDATE WAREHOUSE_QUANTITY SET QUANTITY={} WHERE idss={}".format(quantityidsds)
        print(query)
        self.cur.execute(query)
        self.db.commit()

    def updatingWarehouseQuantityWithQuantityisok(self,idss,quantity,isok):
        self.dbconnect()
        query="UPDATE WAREHOUSE_QUANTITY SET QUANTITY={},IS_OK={} WHERE idss={} ".format(quantity,isokidsds)
        print(query)
        self.cur.execute(query)
        self.db.commit()

    def ListingWarehouseProcess(self):
        return self.listing(TABLE="VM_WAREHOUSE_PROCESS",COLUMN=["idss","PROCESSidsds","MATERIAidsids","MATERIAL_NAME","MATERIAL_NO","QUANTITY","MEASUREMEids_ids","MEASUREMENT_UNIT_NAME","PROCESSING_DATE"],ORDER="PROCESSING_DATE")











    