from artistSongs import artistSongs

# this is Aesop Rock's genius artist id. This is pretty important at the moment.
artistId = 178
songs = artistSongs.getSongObjectsForArtist(artistSongs, artistId)

# Here we start doing magic things. For each result here I'll need to get the actual song object?
# at worst I'll need to store all the song urls so that they can be scraped in genius-song-scrape
for song in songs:
    if song["primary_artist"]["id"] == artistId:

        print(
            " - songid:", str(song['id']),
            "\n - full_title:", song['full_title'],
            "\n - url:", song['url']
        )
        print("----")
