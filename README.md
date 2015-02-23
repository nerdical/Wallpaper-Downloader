# Wallpaper-Downloader
<br>
Reddit bot to download top submissions in /r/wallpapers
<br>
Run this script manually, or setup a schedule using cron or windows task scheduler to download the top submissions in /r/wallpapers.<br>

<dl>
<dt>Variables to modify</dt>
<dd>user_id = your reddit username</dd>
<dd>user_pass = your reddit password</dd>
<dd>number = number of top submissions to download</dd>
<dd>path = local directory where to store downloaded image files</dd>
<dd>booleans: hour, day, week</dd>
</dl>

Once the above variables have been set by the user, run the script to download the top 'number' images. The booleans will tell the script if you want to download the top submissions by hour, day, week, or any combination of the three.
