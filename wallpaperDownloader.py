##################################################
# /r/wallpaper top submission downloader 5000    #
#                                                #
# Downloads top n submissions that are hosted    #
# on imgur. Skips submissions that are not.      #
#                                                #
# Created by /u/koberg                           #
#                                                #
# To customize, see comments in the body of code #
##################################################

######VARIABLES AND SUCH THAT DO NOT CHANGE!######
import praw
import urllib
import os
import re
import random
import time

r = praw.Reddit(user_agent = ("/r/wallpaper downloader by /u/koberg"
			  "User defined Frequency by hour, [to]day, and week"))

#r.login("wallpaper_downloader", "D0wn10adW@11p@P3r5")
#Reddit user login information
user_id = "<REDDIT USER ID>"
user_pass = "<REDDIT USER PASS>"
r.login(user_id, user_pass)

wallpapers = r.get_subreddit("wallpaper")
##########CHANGE NOTHING ABOVE THIS LINE##########

#USER DEFINED VARIABLES BELOW:

hour = True #Set hour to True to check top submissions from 'this hour'
day = True #Set day to True to check top submissions from 'today'
week = True #Set week to True to check top submissions from 'this week'

number = 10 #Set this value to the number of top submissions, ie: top 10

'''
Set the qty value to limit the number of files located in your target path.
Set the age value to limit the number of days to keep files.
Set both qty and age to 0 if you do not want to automatically remove wallpapers.
'''
#qty = 0 Functionality not yet implemented
age = 7

path = os.path.expanduser("~\\Pictures\\wallpapers\\") #Path to save images. Can be anywhere on your local machine.

words = ["Awesome!", "Amazing!", "Beautiful!", "Brilliant!", "Cool!", "Fantastic!"]

##########CHANGE NOTHING BELOW THIS LINE##########
##########    BOT SCRIPT BEGINS HERE    ##########

def downloader(range):
	if range == "day":
		top = wallpapers.get_top_from_day(limit=number)
	elif range == "week":
		top = wallpapers.get_top_from_week(limit=number)
	elif range == "hour":
		top = wallpapers.get_top_from_hour(limit=number)
	else:
		print "Error with range variable in downloader() function"
	
	for image in top:
		
		adjective = words[random.randrange(1,len(words))]
		#Make sure image(s) aren't NSFW
		if not image.over_18:
	
			#Check if image source is imgur
			if "imgur.com/" in image.url and not "imgur.com/a/" in image.url:
			
				#Check if link ends with jpg or png: (might need to add more file extensions or a better method)
				if str(image.url).endswith(".jpg") or str(image.url).endswith(".png"):
					url = str(image.url)
					fileName = re.search('[^\\/:*?"<>|\r\n]+$', url)
					
					#check if File already exists
					if not os.path.isfile(path + fileName.group(0)):
						urllib.urlretrieve(url, path + fileName.group(0))
						image.add_comment("%s\n\nThis image has been downloaded by /u/wallpaper_downloader for use on a personal computer.\n\nThank you for the submission, have an upvote!\n\nMore information is available at https://github.com/nerdical/Wallpaper-Downloader" %(adjective))
						image.upvote()
					else:
						print "Image " + str(image.url) + " already exists"
		
				else:
					url = str(image.url) + ".jpg"
					fileName = re.search('[^\\/:*?"<>|\r\n]+$', url)
					
					#If file does not exists on local machine:
					if not os.path.isfile(path + fileName.group(0)):
						urllib.urlretrieve(url, path + fileName.group(0))
						image.add_comment("%s\n\nThis image has been downloaded by /u/wallpaper_downloader for use on a personal computer.\n\nThank you for the submission, have an upvote!\n\nMore information is available at https://github.com/nerdical/Wallpaper-Downloader" %(adjective))
						image.upvote()
					else:
						print "Image " + str(image.url) + " already exists"
					
			else:
				print "\t" + str(image.url) + "\n\t not located on www.imgur.com"
	
	print "Done checking %s" %(range)

def cleanup():
	
	#Function to clean up wallpaper folder based on age and/or quantity of images stored
	'''
	Quantity removal loop not yet worked out
	if qty > 0:
		print "Cleanup by Quantity..."
		print path
	'''
	if age > 0:
		import time
		count = 1
		now = time.time()
		
		print "Cleanup by Age..."
		for image in os.listdir(path):
			if os.stat(path + image).st_mtime < now - age * 86400:
				if os.path.isfile(path + image):
					os.remove(path + image)
					count += 1
	
	raw_input("Removed " + str(count) + " images.\nPress Enter to Complete")

if __name__ == '__main__':
	if hour:
		downloader("hour")
	if day:
		downloader("day")
	if week:
		downloader("week")
	
	cleanup()
