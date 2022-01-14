import time
import random
import os

if os.path.isfile("D:\\PROJECT\\config\\Blarj.test_uuid_and_cookie.json"):
    os.remove("D:\\PROJECT\\config\\Blarj.test_uuid_and_cookie.json")

from instabot import Bot
bot = Bot()
time.sleep(5)
bot.login(username="username",password="password")

medias = bot.get_total_user_medias(bot.user_id)
#print(type(medias)) IT'S A LIST
#bot.delete_media("2601815654628512455_48320791129") #IT'S BACKWARDS SO medias[0] is the latest thing you uploaded

for media in medias:
   bot.delete_media(media)
   time.sleep(random.randint(5,15))
   print(media)

bot.delete_media(2601397587352210318_48320791129)#unique media code for each image...

def delete_media(self, media):#delete function 
    data = self.json_data({"media_id": media.get("id")})
    url = "media/{media_id}/delete/".format(media_id=media.get("id"))
    return self.send_request(url, data)
