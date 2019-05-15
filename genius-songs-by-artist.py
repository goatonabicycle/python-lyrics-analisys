from artistSongs import artistSongs
from _fileHandling import fileHandling
from _collectionHandling import collectionHandling
import re

# this is Aesop Rock's genius artist id. This is pretty important at the moment.
artistId = 178
songs = artistSongs.getSongObjectsForArtist(artistSongs, artistId)
grandCollectionOfLyrics = ''

for song in songs:
    if song["primary_artist"]["id"] == artistId:        
        songId = str(song['id'])
        songUrl = song['url']
        songTitle = song['full_title']
        print("Now getting '" + songTitle + "' to file" + "\n songId: " + songId + "\n url:" + songUrl)       
        songLyrics = artistSongs.getSongLyrics(artistSongs, songUrl)
        grandCollectionOfLyrics += songLyrics.lower()
        
        # print("lyrics: \n" + songLyrics)        

        # cleanedFileName = "songs\\" + re.sub('[^\w\-_\. ]', '_', songTitle)
        # fileHandling.writeToFile(
        #     fileHandling, cleanedFileName, songLyrics)

wordsToIgnore = ['the','a','if','in','it','of','or', 'an', 'is']
result = collectionHandling.stringToCountedCollection(collectionHandling, grandCollectionOfLyrics, wordsToIgnore)
print(result)
