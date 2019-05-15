from artistSongs import artistSongs
from fileHandling import fileHandling
import re

def logInfo(self, stringToLog):
    print("----")    
    print(stringToLog)
    print("----")    

# this is Aesop Rock's genius artist id. This is pretty important at the moment.
artistId = 178
songs = artistSongs.getSongObjectsForArtist(artistSongs, artistId)

# Here we start doing magic things. For each result here I'll need to get the actual song object?
# at worst I'll need to store all the song urls so that they can be scraped in genius-song-scrape
for song in songs:
    if song["primary_artist"]["id"] == artistId:
        songid = str(song['id'])
        songUrl = song['url']
        songTitle = song['full_title']
        songLyrics = artistSongs.getSongLyrics(artistSongs, songUrl)

        logInfo(infoLogging, "Now writing '" + songTitle + "' to file")       
        # logInfo("lyrics: \n" + songLyrics)
        logInfo(infoLogging, "songid: " + songid + "\n - full_title: " + songTitle + "\n - url:" + songUrl)        

        cleanedFileName = "songs\\" + re.sub('[^\w\-_\. ]', '_', songTitle)
        fileHandling.writeToFile(
            fileHandling, cleanedFileName, songLyrics)
        





