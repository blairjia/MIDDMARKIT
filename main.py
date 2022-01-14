import itemclass
import gsheet
import string
import posting_deleting_instagrapi


#if liberal_trigger is true, it will return a row number
row_num = 6#this will store liberal_trigger
sheet = gsheet.sheet_return()

row = sheet.row_values(row_num) #first row

uname = (row[2]+row[0]).replace(" ", "")
for i in uname:
    if i in string.punctuation:
        uname = uname.replace(i, "")

image_list = gsheet.down_photo(uname,row_num)
#print(image_list)
blair_item = itemclass.item(row_num, row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], image_list)

blair_item.post()

#print(sheet.row_values(row_num))
