import time
import random
import os
if os.path.isfile("D:\\PROJECT\\config\\Blarj.test_uuid_and_cookie.json"):
    os.remove("D:\\PROJECT\\config\\Blarj.test_uuid_and_cookie.json")


from instabot import Bot
bot = Bot()
bot.login(username="username",password="password")
bot.upload_photo("image.jpg",caption="caption")

os.remove("D:\\PROJECT\\image.jpg.REMOVE_ME")
