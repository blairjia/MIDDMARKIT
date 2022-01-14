import itemclass
import gsheet
import string
import posting_deleting_instagrapi as pdi


#if item is sold, trigger this and return row number
row_num = 6 #temp until we get the trigger
sheet = gsheet.sheet_return()

identity = sheet.acell('J'+str(row_num)).value

pdi.deleting(identity)
sheet.update_acell("K"+str(row_num), "yes")
