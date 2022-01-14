import time
import random
import os


if os.path.isfile("D:\\PROJECT\\config\\Blarj.test_uuid_and_cookie.json"):
    os.remove("D:\\PROJECT\\config\\Blarj.test_uuid_and_cookie.json")


from instabot import Bot
bot = Bot()
bot.login(username="username",password="password")
list = ["1.jpg", "2.jpg", "3.jpg"]
options = {}
options["is_sidecar"] = "1"
for photo in list:
    bot.upload_photo(photo,caption = "caption", None, False,False,options,None,is_sidecar = True)
