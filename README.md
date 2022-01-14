# MIDDMARKIT - Automatic Instagram Uploader

## Files

###### posting_old.py
First posting function using instabot API which allowed us to autimatically upload photos onto Instagram. 
Discontinued because of difficulty with API to post other media content.

###### posting_multiple_old.py
Posting function using instabot API which allowed for multiple photo upload per post on Instagram.
Discontinued because of difficulty with API to post other media content.

###### deleting_old.py
First deleting function using instabot API to delete posts.
Discontinued because of difficulty deleting specific posts.

###### posting_deleting_instagrapi.py
Improved posting and deleting functions, using new instagrapi API to automate uploading and deleting posts on Instagram.

###### gsheet.py
Set up to retrieve post data including photos/videos/other media and caption.

###### itemclass.py
Item class containing usueful information about each retreived item, and also includes posting and deleting functions.

###### main.py
Main function that when triggered retrieves data from a google spreadsheet, and autimatically generates a post with a caption and uploads onto instagram.

###### main.delete.py 
Main function that when triggered, autimatically deletes the specific post.
