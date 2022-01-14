import gsheet
import posting_deleting_instagrapi as pdi
from instagrapi import Client

class item:

    def __init__(self, row, date, email, name, paymenttype, number, item, price, condition, photo,identity = "0"):
        self.row = str(row)
        self.email = email
        self.name = (name+date).replace(" ","")#name of photo from sheet = name+ date
        self.paymenttype = paymenttype
        self.number = number
        self.caption = str(condition) +" " +str(item) +"\n" + "$"+str(price)
        # self.item = item
        # self.price = price
        # self.condition = condition
        self.photo = photo
        self.id = identity

    def get_id(self):
        bot = Client()
        bot.login("username", "password")
        medias = bot.user_medias(48320791129)
        p0 = str(medias[0]).split()
        self.id = p0[1][4:-1]
        sheet = gsheet.sheet_return()
        sheet.update_acell("J"+self.row,self.id)

    def post(self):
        pdi.posting(self.photo,self.caption)
        self.get_id()

    def delete(self,sheet): 
        pdi.deleting(self.id)
        sheet = gsheet.sheet_return()
        sheet.update_acell("K"+self.row,"yes") #this updates the "sold?"" column in google sheets to "yes" because the item is sold.
