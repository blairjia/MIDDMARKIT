from oauth2client.service_account import ServiceAccountCredentials
import gdown
import gspread
import json

def sheet_return():
    scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("middmarketauth.json", scopes) #access the json key you downloaded earlier
    file = gspread.authorize(credentials) # authenticate the JSON key with gspread
    sheet = file.open("Seller Form (Responses)")  #open sheet
    sheet = sheet.sheet1  #replace sheet_name with the name that corresponds to yours, e.g, it can be sheet1
    return sheet

def down_photo(name,row):
    scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
    ]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("middmarketauth.json", scopes) #access the json key downloaded earlier
    file = gspread.authorize(credentials) # authenticate the JSON key with gspread
    sheet = file.open("Seller Form (Responses)")  #open sheet
    sheet = sheet.sheet1  #
    photos = []
    links = sheet.acell("I"+str(row)).value.split(", ")#umm str(row) in case we get int or check back later 
    if len(links) == 1:
        url = links[0].replace("open","uc")
        output = name+'.jpg'
        gdown.download(url, output, quiet=False)
        photos.append(output)
        return photos

    else:
        for i in range(len(links)):
            url = links[i].replace("open","uc")
            output = name+ str(i) + '.jpg' #maybe instead of "image" -> object.name + object.item + object.date
            gdown.download(url, output, quiet=False)
            photos.append(name+ str(i) + '.jpg')#photos is the list that goes in upload album
        return photos





#all_cells = sheet.range('A2:I3')
#for cell in all_cells:
	#print(cell.value)
#for each row we create an instance of a class