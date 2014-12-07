#!/usr/bin/env python

import pafy, os, sys, re

def mycb(total, recvd, ratio, rate, eta):
  print(recvd, ratio, eta)
def playlistcb(str):
  title = re.sub('[\W]+', " ", str)
  print u"{}".format(title)

while True:
  print "1. Download a youtube video"
  print "2. Download a youtube playlist"
  print "3. Exit\n"
  print "Select an action: "
  action = raw_input("> ")
  if action == str(1):
    songUrl = raw_input("Enter youtube url: ")
    video = pafy.new(songUrl)
    if video.getbestaudio(preftype="ogg"):
      video.getbestaudio(preftype="ogg").download()
      print "Done!"
    else:
      print "Invalid song!"
  elif action == str(2):
    playlistUrl = raw_input("Enter playlist url: ")
    playlist = pafy.get_playlist(playlistUrl, callback=playlistcb)
    for i in range(0, len(playlist['items'])):
      #print playlist['items'][i]
      audio = playlist['items'][i]['pafy']  
      if audio.getbestaudio(preftype="ogg"):
        title = re.sub('[\s\W]+', "_", audio.title)
        if not os.path.exists("download/" + title + ".ogg"):
          audio.getbestaudio(preftype="ogg").download(quiet=True, filepath="download/" + title + ".ogg")
          print u"{} / {} {}".format(i+1, len(playlist['items']), title+".ogg")
        else:
          print "Song already exist."
      else:
        print "Invalid song - skipping"
  elif action == str(3):
    raise SystemExit()
  else:
    print "Not a valid option!\n"



