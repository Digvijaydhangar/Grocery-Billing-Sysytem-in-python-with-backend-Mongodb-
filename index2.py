from asyncio.windows_events import NULL
from tkinter import *
import random
from turtle import update
from typing import Collection
import pymongo
client=pymongo.MongoClient("mongodb://localhost:27017/")
#print("\ncmplt")
db=client['harry']
#collection=db['mycolect']

collection=db['Food']
collectionG=db['Grocery']
collectionO=db['Others']
collectionC=db['Customer']


class Bill_App:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1300x700+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Grocery Billing System BY DIGVIJAY DHANGAR")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        self.cus_id=IntVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        
        
        self.c_bill_no.set(str(x))
        self.c_add=StringVar()
        self.bread = IntVar()
        self.candy = IntVar()
        self.hamburger = IntVar()
        self.hotdog = IntVar()
        self.sandwich = IntVar()
        self.rice = IntVar()
        self.salt = IntVar()
        self.food_oil = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.gatorade = IntVar()
        self.coke = IntVar()
        self.juice = IntVar()
        self.waffer = IntVar()
        self.biscuits = IntVar()
        self.total_food = StringVar()
        self.total_grocery = StringVar()
        self.total_other = StringVar()
        self.tax_cos = StringVar()
        self.tax_groc = StringVar()
        self.tax_other = StringVar()

       
        #===================================
        bg_color = "brown"
        g_color="red"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Grocery Billing System",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 70,relwidth = 1)
        #==========Customers id==========#
        cname_lbl = Label(F1,text="Customer ID",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_id)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)
        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer City==============#
        cphon_lbl = Label(F1,text = "City",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 4,padx = 20,pady=5)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_add)
        cphon_en.grid(row = 0,column = 5,ipady = 4,ipadx = 30,pady = 5)

         #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 6,padx = 20,pady=5)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 7,ipady = 4,ipadx = 30,pady = 5)
       
        #==================Food Frame=====================#
        F2 = LabelFrame(self.root,text = 'Food',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 150,width = 415,height = 360)

        #===========Frame Content
        
        bath_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Bread")
        bath_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        bath_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.bread)
        bath_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======Candy
        face_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Candy")
        face_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        face_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.candy)
        face_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #========Hamburger
        wash_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hamburger")
        wash_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        wash_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hamburger)
        wash_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========Hotdog
        hair_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Hotdog")
        hair_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        hair_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.hotdog)
        hair_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============Sandwich
        lot_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sandwich")
        lot_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        lot_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sandwich)
        lot_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Grocery Frame=====================#
        F2 = LabelFrame(self.root,text = 'Grocery',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 420,y = 150,width = 420,height = 360)

        #===========Frame Content
        rice_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Rice")
        rice_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        rice_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.rice)
        rice_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        oil_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Oil")
        oil_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        oil_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.food_oil)
        oil_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        daal_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Salt")
        daal_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        daal_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.salt)
        daal_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        wheat_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Wheat")
        wheat_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        wheat_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.wheat)
        wheat_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        sugar_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Sugar")
        sugar_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        sugar_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.sugar)
        sugar_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)

        #==================Other Stuff=====================#

        F2 = LabelFrame(self.root,text = 'Others',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 840,y = 150,width = 430,height = 360)

        #===========Frame Content
        maza_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Gatorade")
        maza_lbl.grid(row = 0,column = 0,padx = 10,pady = 20)
        maza_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.gatorade)
        maza_en.grid(row = 0,column = 1,ipady = 5,ipadx = 5)

        #=======
        cock_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Coke")
        cock_lbl.grid(row = 1,column = 0,padx = 10,pady = 20)
        cock_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.coke)
        cock_en.grid(row = 1,column = 1,ipady = 5,ipadx = 5)

        #=======
        frooti_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Juice")
        frooti_lbl.grid(row = 2,column = 0,padx = 10,pady = 20)
        frooti_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.juice)
        frooti_en.grid(row = 2,column = 1,ipady = 5,ipadx = 5)

        #========
        cold_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Waffer")
        cold_lbl.grid(row = 3,column = 0,padx = 10,pady = 20)
        cold_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.waffer)
        cold_en.grid(row = 3,column = 1,ipady = 5,ipadx = 5)

        #============
        bis_lbl = Label(F2,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Biscuits")
        bis_lbl.grid(row = 4,column = 0,padx = 10,pady = 20)
        bis_en = Entry(F2,bd = 8,relief = GROOVE,textvariable = self.biscuits)
        bis_en.grid(row = 4,column = 1,ipady = 5,ipadx = 5)
        
        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 510,relwidth = 1,height = 145)
       

        #====================
        updprc_btn = Button(F4,text = "Update Prices",bg = g_color,fg = fg_color,font=("lucida",12,"bold"),bd = 5,relief = GROOVE,command = self.updatep)
        updprc_btn.grid(row = 1,column = 1,ipadx = 20,padx = 30)
        
        #========================
        addcust_btn = Button(F4,text = "Add Customer",bg = g_color,fg = fg_color,font=("lucida",12,"bold"),bd = 5,relief = GROOVE,command = self.add_customer)
        addcust_btn.grid(row = 1,column = 2,ipadx = 20,padx=30)
        

        
        #====================
        updcus_btn = Button(F4,text = "Update Customer",bg = g_color,fg = fg_color,font=("lucida",12,"bold"),bd = 5,relief = GROOVE,command = self.upd_customer)
        updcus_btn.grid(row = 1,column = 3,ipadx = 20,padx = 30)
        
        #======================
        delcust_btn = Button(F4,text = "Delete Customer",bg = g_color,fg = fg_color,font=("lucida",12,"bold"),bd = 5,relief = GROOVE,command = self.del_cus)
        delcust_btn.grid(row = 1,column = 4,ipadx = 20,padx=30)

        #======== Exit Button =======
        exit_btn = Button(F4,text = "Exit",bg = g_color,fg = fg_color,font=("lucida",12,"bold"),bd = 5,relief = GROOVE,command = self.exit)
        exit_btn.grid(row = 1,column = 5,ipadx = 20,padx=30)

    
    def upd_customer(self):     
        if self.cus_id.get() !=0:
            myproduct = { "cid":self.cus_id.get()  }
            updatek={"$set":{"name":self.cus_name.get(),"phone":self.c_phone.get(),"add":self.c_add.get()}}
            collectionC.update_one(myproduct,updatek)


#Function to update prices of Products
    def updatep(self):
        #========== Food Products ===========
        if self.bread.get() !=0:
            myproduct = { "name": "Bread" }
            updateprice = { "$set": { "price":self.bread.get()} }
            collection.update_one(myproduct,updateprice)
        
        if self.candy.get() !=0:
            myproduct = { "name": "Candy" }
            updateprice = { "$set": { "price":self.candy.get()} }
            collection.update_one(myproduct,updateprice)

        if self.hamburger.get() !=0:
            myproduct = { "name": "Hamburger" }
            updateprice = { "$set": { "price":self.hamburger.get()} }
            collection.update_one(myproduct,updateprice)
        
        if self.hotdog.get() !=0:
            myproduct = { "name": "Hotdog" }
            updateprice = { "$set": { "price":self.hotdog.get()} }
            collection.update_one(myproduct,updateprice)

        if self.sandwich.get() !=0:
            myproduct = { "name": "Sandwich" }
            updateprice = { "$set": { "price":self.sandwich.get()} }
            collection.update_one(myproduct,updateprice)
        
     #================= Grocery Products =================
        if self.rice.get() !=0:
            myproduct = { "name": "Rice" }
            updateprice = { "$set": { "price":self.rice.get()} }
            collectionG.update_one(myproduct,updateprice)

        if self.food_oil.get() !=0:
            myproduct = { "name": "FoodOil" }
            updateprice = { "$set": { "price":self.food_oil.get()} }
            collectionG.update_one(myproduct,updateprice)

        if self.salt.get() !=0:
            myproduct = { "name": "Salt" }
            updateprice = { "$set": { "price":self.salt.get()} }
            collectionG.update_one(myproduct,updateprice)

        if self.wheat.get() !=0:
            myproduct = { "name": "Wheat" }
            updateprice = { "$set": { "price":self.wheat.get()} }
            collectionG.update_one(myproduct,updateprice)

        if self.sugar.get() !=0:
            myproduct = { "name": "Sugar" }
            updateprice = { "$set": { "price":self.sugar.get()} }
            collectionG.update_one(myproduct,updateprice)

    #================= Other Products =================
        if self.gatorade.get() !=0:
            myproduct = { "name": "Gatorade" }
            updateprice = { "$set": { "price":self.gatorade.get()} }
            collectionO.update_one(myproduct,updateprice)

        if self.coke.get() !=0:
            myproduct = { "name": "Coke" }
            updateprice = { "$set": { "price":self.coke.get()} }
            collectionO.update_one(myproduct,updateprice)

        if self.juice.get() !=0:
            myproduct = { "name": "Juice" }
            updateprice = { "$set": { "price":self.juice.get()} }
            collectionO.update_one(myproduct,updateprice)

        if self.waffer.get() !=0:
            myproduct = { "name": "Waffer" }
            updateprice = { "$set": { "price":self.waffer.get()} }
            collectionO.update_one(myproduct,updateprice)

        if self.biscuits.get() !=0:
            myproduct = { "name": "Biscuits" }
            updateprice = { "$set": { "price":self.biscuits.get()} }
            collectionO.update_one(myproduct,updateprice)    
    

#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def add_customer(self):
      
        dict={"cid":self.cus_id.get(),"name":self.cus_name.get(),"add":self.c_add.get(),"phone":self.c_phone.get()}    
        collectionC.insert_one(dict)

    def exit(self):
        self.root.destroy()

    
            
    def del_cus(self):
        pr=collectionC.find_one({"cid":self.cus_id.get()})
        if pr !=0:
            myproduct = { "cid":self.cus_id.get()  }
            collectionC.delete_one(myproduct)

    #function of update button
    def upd(self):
        self.upd_customer
        self.updatep



        


root = Tk()
object = Bill_App(root)
root.mainloop()


