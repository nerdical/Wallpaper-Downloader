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
import os.path
import re

r = praw.Reddit(user_agent = ("/r/wallpaper downloader by /u/koberg"
			  "User defined Frequency by hour, [to]day, and week"))

#Reddit user login information
user_id = "username"
user_pass = "password"
r.login(user_id, user_pass)

wallpapers = r.get_subreddit("wallpaper")
##########CHANGE NOTHING ABOVE THIS LINE##########

#USER DEFINED VARIABLES BELOW:

hour = True #Set hour to True to check top submissions from 'this hour'
day = True #Set day to True to check top submissions from 'today'
week = True #Set week to True to check top submissions from 'this week'

number = 10 #Set this value to the number of top submissions, ie: top 5

'''
Future versions/revisions will include the options to limit the number of wallpapers in your destination folder by
removing the oldest wallpapers and replacing them with newer ones.
There will also be the option to remove wallpapers by age. The oldens n files will be removed after new wallpapers
have been downloaded.
'''
#qty = 10
#age = 7 

path = os.path.expanduser("~\\wallpaper\\directory\\") #Path to save images

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
		print "Error with downloader() function"
	
	for image in top:
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
						image.add_comment("Beautiful!\n\nThis image has been downloaded by /u/wallpaper_downloader for use on a personal computer.\n\nThank you for the submission, have an upvote!")
						image.upvote()
					else:
						print "Image " + str(image.url) + " already exists"
		
				else:
					url = str(image.url) + ".jpg"
					fileName = re.search('[^\\/:*?"<>|\r\n]+$', url)
					
					#If file does not exists on local machine:
					if not os.path.isfile(path + fileName.group(0)):
						urllib.urlretrieve(url, path + fileName.group(0))
						image.add_comment("Beautiful!\n\nThis image has been downloaded by /u/wallpaper_downloader for use on a personal computer.\n\nThank you for the submission, have an upvote!")
						image.upvote()
					else:
						print "Image " + str(image.url) + " already exists"
					
			else:
				print "\t" + str(image.url) + "\n\t not located on imgur"
	
	print "Done checking %s" %(range)

if hour:
	downloader("hour")
if day:
	downloader("day")
if week:
	downloader("week")
