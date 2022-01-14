from instagrapi import Client


#post function
def posting(photos,text):
    bot = Client()
    bot.login("username", "password")
    if len(photos) == 1:
        bot.photo_upload(photos[0],caption = text)
    else:
        bot.album_upload(photos,caption = text)

#posting(["something.jpg"],"i love my face")


#delete function
def deleting(identity):
    bot = Client()
    bot.login("username", "password")
    bot.media_delete(identity)

#deleting("2603233439598503056_48320791129")
