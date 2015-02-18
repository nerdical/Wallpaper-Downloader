# Wallpaper-Downloader
Reddit bot to download top submissions in /r/wallpapers

Run this script manually, or setup a schedule using cron or windows task scheduler, to download the top submissions in /r/wallpapers.

Variables to modify
  user_id = your reddit username
  user_pass = your reddit password
  number = number of top submissions to download
  path = local directory where to store downloaded image files
  booleans:
    hour
    day
    week

Once the above variables have been set by the user, run the script to download the top 'number' images. The booleans will tell the script if you want to download the top by hour, day, week, or any combination of the three.
