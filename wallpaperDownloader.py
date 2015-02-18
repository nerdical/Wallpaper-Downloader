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

wallpapers = r.get_subreddit("wallpaper")
##########CHANGE NOTHING ABOVE THIS LINE##########

#USER DEFINED VARIABLES BELOW:

#Reddit user login information
user_id = ""
user_pass = ""
r.login(user_id, user_pass)

#You can set more than one boolean to true.

hour = True #Set hour to True to check top submissions from 'this hour'
day = True #Set day to True to check top submissions from 'today'
week = True #Set week to True to check top submissions from 'this week'

number = 10 #Set this value to the number of top submissions, ie: top 5

#Set the qty value to limit the number of files located in your target path.
#This should never be less than the 'number' variable above and therefore will not work
#qty = 10

path = os.path.expanduser("~\\Path\\to\\directory") #Path to save images

##########CHANGE NOTHING BELOW THIS LINE##########
##########    BOT SCRIPT BEGINS HERE    ##########

if hour: #Get top submission(s) from this hour
	print "Checking top of the hour"
	top = wallpapers.get_top_from_hour(limit=number)
	for image in top:
	
		#Check if image source is imgur
		if "imgur.com/" in image.url:
		
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

if day: #Get top submission(s) from today
	print "Checking top of the day"
	top = wallpapers.get_top_from_day(limit=number)
	for image in top:
	
		#Check if image source is imgur
		if "imgur.com/" in image.url:
		
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

if week: #Get top submission(s) from this week
	print "Checking top of the week"
	top = wallpapers.get_top_from_week(limit=number)
	for image in top:
	
		#Check if image source is imgur
		if "imgur.com/" in image.url:
		
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
