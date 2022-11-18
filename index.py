from tkinter import *
import random
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
        self.root.geometry("1300x600+0+0")
        self.root.maxsize(width = 1280,height = 700)
        self.root.minsize(width = 1280,height = 700)
        self.root.title("Grocery Billing System BY DIGVIJAY DHANGAR")
        
        #====================Variables========================#
        self.cus_name = StringVar()
        self.c_phone = StringVar()
        #For Generating Random Bill Numbers
        x = random.randint(1000,9999)
        self.c_bill_no = StringVar()
        #Seting Value to variable
        self.c_bill_no.set(str(x))
        self.cid=IntVar()
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
        bg_color = "maroon"
        fg_color = "white"
        lbl_color = 'white'
        #Title of App
        title = Label(self.root,text = "Grocery Billing System",bd = 12,relief = GROOVE,fg = fg_color,bg = bg_color,font=("times new roman",30,"bold"),pady = 3).pack(fill = X)

        #==========Customers Frame==========#
        F1 = LabelFrame(text = "Customer Details",font = ("time new roman",12,"bold"),fg = "gold",bg = bg_color,relief = GROOVE,bd = 10)
        F1.place(x = 0,y = 70,relwidth = 1)

        #===============Customer Id===========#
        cname_lbl = Label(F1,text="Customer ID",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 0,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cid)
        cname_en.grid(row = 0,column = 1,ipady = 4,ipadx = 30,pady = 5)

        #===============Customer Name===========#
        cname_lbl = Label(F1,text="Customer Name",bg = bg_color,fg = fg_color,font=("times new roman",15,"bold")).grid(row = 0,column = 2,padx = 10,pady = 5)
        cname_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.cus_name)
        cname_en.grid(row = 0,column = 3,ipady = 4,ipadx = 30,pady = 5)

        #=================Customer Phone==============#
        cphon_lbl = Label(F1,text = "Phone No",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold")).grid(row = 0,column = 4,padx = 20)
        cphon_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_phone)
        cphon_en.grid(row = 0,column = 5,ipady = 4,ipadx = 30,pady = 5)

        #====================Customer Bill No==================#
        cbill_lbl = Label(F1,text = "Bill No.",bg = bg_color,fg = fg_color,font = ("times new roman",15,"bold"))
        cbill_lbl.grid(row = 0,column = 6,padx = 20)
        cbill_en = Entry(F1,bd = 8,relief = GROOVE,textvariable = self.c_bill_no)
        cbill_en.grid(row = 0,column = 7,ipadx = 30,ipady = 4,pady = 5)
        
        #==================Food Frame=====================#
        F2 = LabelFrame(self.root,text = 'Food',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F2.place(x = 5,y = 150,width = 325,height = 360)

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
        F2.place(x = 330,y = 150,width = 325,height = 360)

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
        F2.place(x = 655,y = 150,width = 325,height = 360)

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

        #===================Bill Aera================#
        F3 = Label(self.root,bd = 10,relief = GROOVE)
        F3.place(x = 960,y = 150,width = 325,height = 360)
        #===========
        bill_title = Label(F3,text = "Bill List",font = ("Lucida",13,"bold"),bd= 7,relief = GROOVE)
        bill_title.pack(fill = X)

        #============
        scroll_y = Scrollbar(F3,orient = VERTICAL)
        self.txt = Text(F3,yscrollcommand = scroll_y.set)
        scroll_y.pack(side = RIGHT,fill = Y)
        scroll_y.config(command = self.txt.yview)
        self.txt.pack(fill = BOTH,expand = 1)

        #===========Buttons Frame=============#
        F4 = LabelFrame(self.root,text = 'Bill Menu',bd = 10,relief = GROOVE,bg = bg_color,fg = "gold",font = ("times new roman",13,"bold"))
        F4.place(x = 0,y = 510,relwidth = 1,height = 145)

        #===================
        cosm_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Food")
        cosm_lbl.grid(row = 0,column = 0,padx = 10,pady = 0)
        cosm_en = Entry(F4,bd = 4,relief = GROOVE,textvariable = self.total_food)
        cosm_en.grid(row = 0,column = 1,ipady = 1,ipadx = 1)

        #===================
        gro_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Total Grocery")
        gro_lbl.grid(row = 1,column = 0,padx = 10,pady = 5)
        gro_en = Entry(F4,bd = 4,relief = GROOVE,textvariable = self.total_grocery)
        gro_en.grid(row = 1,column = 1,ipady = 1,ipadx = 1)

        #================
        oth_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Total")
        oth_lbl.grid(row = 2,column = 0,padx = 10,pady = 5)
        oth_en = Entry(F4,bd = 4,relief = GROOVE,textvariable = self.total_other)
        oth_en.grid(row = 2,column = 1,ipady = 1,ipadx = 1)

        #================
        cosmt_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Food Tax")
        cosmt_lbl.grid(row = 0,column = 2,padx = 30,pady = 0)
        cosmt_en = Entry(F4,bd = 4,relief = GROOVE,textvariable = self.tax_cos)
        cosmt_en.grid(row = 0,column = 3,ipady = 2,ipadx = 5)

        #=================
        grot_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Grocery Tax")
        grot_lbl.grid(row = 1,column = 2,padx = 30,pady = 5)
        grot_en = Entry(F4,bd = 4,relief = GROOVE,textvariable = self.tax_groc)
        grot_en.grid(row = 1,column = 3,ipady = 2,ipadx = 5)

        #==================
        otht_lbl = Label(F4,font = ("times new roman",15,"bold"),fg = lbl_color,bg = bg_color,text = "Others Tax")
        otht_lbl.grid(row = 2,column = 2,padx = 10,pady = 5)
        otht_en = Entry(F4,bd = 4,relief = GROOVE,textvariable = self.tax_other)
        otht_en.grid(row = 2,column = 3,ipady = 2,ipadx = 5)

        #====================
        total_btn = Button(F4,text = "Total",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.total)
        total_btn.grid(row = 1,column = 4,ipadx = 20,padx = 30)

        #========================
        genbill_btn = Button(F4,text = "Generate Bill",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.bill_area)
        genbill_btn.grid(row = 1,column = 5,ipadx = 20)

        #====================
        clear_btn = Button(F4,text = "Clear",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.clear)
        clear_btn.grid(row = 1,column = 6,ipadx = 20,padx = 30)

        #======================
        exit_btn = Button(F4,text = "Edit Details",bg = bg_color,fg = fg_color,font=("lucida",12,"bold"),bd = 7,relief = GROOVE,command = self.next)
        exit_btn.grid(row = 1,column = 7,ipadx = 20)

#Function to get total prices
    def total(self):
        pr=collection.find_one({'name':"Bread"})
        br=pr["price"]
        pr=collection.find_one({'name':"Candy"})
        cn=pr["price"]
        pr=collection.find_one({'name':"Hamburger"})
        hm=pr["price"]
        pr=collection.find_one({'name':"Hotdog"})
        hd=pr["price"]
        pr=collection.find_one({'name':"Sandwich"})
        sd=pr["price"]
        #=================Total Food Prices
        self.total_food_prices =(
            (self.bread.get() * br)+
            (self.candy.get() * cn)+
            (self.hamburger.get() * hm)+
            (self.hotdog.get() * hd)+
            (self.sandwich.get() * sd)
        )
        self.total_food.set(""+str(self.total_food_prices)+" Rs")
        self.tax_cos.set(""+str(round(self.total_food_prices*0.05))+" Rs")
        #====================Total Grocery Prices

        pr=collectionG.find_one({'name':"Wheat"})
        br=pr["price"]
        pr=collectionG.find_one({'name':"FoodOil"})
        cn=pr["price"]
        pr=collectionG.find_one({'name':"Salt"})
        hm=pr["price"]
        pr=collectionG.find_one({'name':"Rice"})
        hd=pr["price"]
        pr=collectionG.find_one({'name':"Sugar"})
        sd=pr["price"]
        self.total_grocery_prices = (
            (self.wheat.get()*br)+
            (self.food_oil.get() *cn)+
            (self.salt.get() *hm)+
            (self.rice.get() *hd)+
            (self.sugar.get() *sd)

        )
        self.total_grocery.set(""+str(self.total_grocery_prices)+" Rs")
        self.tax_groc.set(""+str(round(self.total_grocery_prices*0.05))+" Rs")
        #======================Total Other Prices
        pr=collectionO.find_one({'name':"Gatorade"})
        br=pr["price"]
        pr=collectionO.find_one({'name':"Coke"})
        cn=pr["price"]
        pr=collectionO.find_one({'name':"Juice"})
        hm=pr["price"]
        pr=collectionO.find_one({'name':"Waffer"})
        hd=pr["price"]
        pr=collectionO.find_one({'name':"Biscuits"})
        sd=pr["price"]
        self.total_other_prices = (
            (self.gatorade.get() *br)+
            (self.juice.get() *hm)+
            (self.coke.get() *cn)+
            (self.waffer.get() *hd)+
            (self.biscuits.get() *sd)
        )
        self.total_other.set(""+str(self.total_other_prices)+" Rs")
        self.tax_other.set(""+str(round(self.total_other_prices*0.05))+"Rs")


#Function For Text Area
    def welcome_soft(self):
        self.txt.delete('1.0',END)
        self.txt.insert(END,"       Welcome To Store's Retail\n")
        self.txt.insert(END,f"\nBill No. : {str(self.c_bill_no.get())}")
        self.txt.insert(END,f"\nCustomer Name : {str(self.cus_name.get())}")
        self.txt.insert(END,f"\nPhone No. : {str(self.c_phone.get())}")
        self.txt.insert(END,"\n===================================")
        self.txt.insert(END,"\nProduct          Qty         Price")
        self.txt.insert(END,"\n===================================")
    
    def cust(self):
        a=self.cid.get()
        prev={'cid':a}            
        pr=collectionC.find_one(prev)
        cd=pr["name"]
        self.cus_name.set(str(cd))
        cd=pr["phone"]
        self.c_phone.set(str(cd))




#Function to clear the bill area
    def clear(self):
        self.txt.delete('1.0',END)

#Add Product name , qty and price to bill area
    def bill_area(self):
        self.cust()
        self.welcome_soft()
        
        if self.bread.get() != 0:
            prev={'name':"Bread"}            
            pr=collection.find_one(prev)
            pr=self.bread.get()*pr["price"]
            self.txt.insert(END,f"\nBread             {self.bread.get()}           {pr}")

        if self.candy.get() != 0:
            prev={'name':"Candy"}            
            pr=collection.find_one(prev)
            pr=self.candy.get()*pr["price"]
            self.txt.insert(END,f"\nCandy             {self.candy.get()}           {pr}")

        if self.hamburger.get() != 0:

            prev={'name':"Hamburger"}            
            pr=collection.find_one(prev)
            pr=self.hamburger.get()*pr["price"]
            self.txt.insert(END,f"\nHamburger         {self.hamburger.get()}           {pr}")

        if self.hotdog.get() != 0:

            prev={'name':"Hotdog"}            
            pr=collection.find_one(prev)
            pr=self.hotdog.get()*pr["price"]
            self.txt.insert(END,f"\nHotdog            {self.hotdog.get()}           {pr}")

        if self.sandwich.get() != 0 :

            prev={'name':"Sandwich"}            
            pr=collection.find_one(prev)
            pr=self.sandwich.get()*pr["price"]
            self.txt.insert(END,f"\nSandwich          {self.sandwich.get()}           {pr}")

        if self.wheat.get() != 0:

            prev={'name':"Wheat"}            
            pr=collectionG.find_one(prev)
            pr=self.wheat.get()*pr["price"]
            self.txt.insert(END,f"\nWheat             {self.wheat.get()}          {pr}")

        if self.food_oil.get() != 0:

            prev={'name':"FoodOil"}            
            pr=collectionG.find_one(prev)
            pr=self.food_oil.get()*pr["price"]
            self.txt.insert(END,f"\nFood Oil          {self.food_oil.get()}           {pr}")

        if self.salt.get() != 0:

            prev={'name':"Salt"}            
            pr=collectionG.find_one(prev)
            pr=self.salt.get()*pr["price"]
            self.txt.insert(END,f"\nSalt              {self.salt.get()}           {pr}")

        if self.rice.get() != 0:

            prev={'name':"Rice"}            
            pr=collectionG.find_one(prev)
            pr=self.rice.get()*pr["price"]
            self.txt.insert(END,f"\nRice              {self.rice.get()}           {pr}")

        if self.sugar.get() != 0:

            prev={'name':"Sugar"}            
            pr=collectionG.find_one(prev)
            pr=self.sugar.get()*pr["price"]
            self.txt.insert(END,f"\nSugar             {self.sugar.get()}           {pr}")

        if self.gatorade.get() != 0:

            prev={'name':"Gatorade"}            
            pr=collectionO.find_one(prev)
            pr=self.gatorade.get()*pr["price"]
            self.txt.insert(END,f"\nGatorade          {self.gatorade.get()}           {pr}")

        if self.juice.get() != 0:

            prev={'name':"Juice"}            
            pr=collectionO.find_one(prev)
            pr=self.juice.get()*pr["price"]
            self.txt.insert(END,f"\nJuice             {self.juice.get()}           {pr}")

        if self.coke.get() != 0:

            prev={'name':"Coke"}            
            pr=collectionO.find_one(prev)
            pr=self.juice.get()*pr["price"]
            self.txt.insert(END,f"\nCoke              {self.coke.get()}          {pr}")

        if self.waffer.get() != 0:

            prev={'name':"Waffer"}            
            pr=collectionO.find_one(prev)
            pr=self.waffer.get()*pr["price"]
            self.txt.insert(END,f"\nWaffer            {self.waffer.get()}           {pr}")

        if self.biscuits.get() != 0:

            prev={'name':"Biscuits"}            
            pr=collectionO.find_one(prev)
            pr=self.biscuits.get()*pr["price"]
            self.txt.insert(END,f"\nBiscuits          {self.biscuits.get()}           {pr}")

        self.txt.insert(END,"\n===================================")
        T=(self.total_food_prices +self.total_grocery_prices + self.total_other_prices+ (self.total_food_prices * 0.05) + (self.total_grocery_prices * 0.05) + (self.total_other_prices* 0.05))
        self.txt.insert(END,f"\n                      Total : {T} "+" Rs")
    

    def next(self):
        
        import index2



        


root = Tk()
object = Bill_App(root)
root.mainloop()


