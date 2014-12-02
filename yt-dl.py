#!/usr/bin/env python
#sudo apt-get install python2.7
#sudo apt-get install mplayer
#sudo apt-get install lame
#pip install requests
#pip install pafy

import requests
import pafy
import os, sys
from subprocess import call


def downloadSong(url):
  video = pafy.new(url)
  best = video.getbest(preftype="mp4")
  best.download(quiet=False)
  call(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader",  video.title + ".mp4"])
  call(["lame", "-h", "-b", "192", "audiodump.wav", video.title + ".mp3"])
  os.remove("audiodump.wav")
  os.remove(video.title + ".mp4")

while True:
  print "1. Download a youtube video"
  print "2. Download a youtube playlist"
  print "3. Exit\n"
  print "Select an action: "
  action = raw_input("> ")
  if action == str(1):
    songUrl = raw_input("Enter youtube url: ")
    downloadSong(songUrl)
  elif action == str(2):
    playlistUrl = raw_input("Enter playlist url: ")
    playlist = pafy.get_playlist(playlistUrl)
    for i in range(0, len(playlist['items'])):
      downloadSong(playlist['items'][i]['pafy'].videoid)
  elif action == str(3):
    raise SystemExit()
  else:
    print "Not a valid option!\n"



