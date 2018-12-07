from artistSongs import artistSongs

# this is Aesop Rock's genius artist id. This is pretty important at the moment.
artistId = 178
parsed = artistSongs.getSongsForArtist(artistSongs, artistId)

# Here we start doing magic things. For each result here I'll need to get the actual song object?
# at worst I'll need to store all the song urls so that they can be scraped in genius-song-scrape
for item in parsed['response']['songs']:
    if item["primary_artist"]["id"] == artistId:
        print(
            " - songid:", item['id'],
            "\n - full_title:", item['full_title'],
            "\n - title_with_featured:", item['title_with_featured'],
            "\n - url:", item['url']
        )
        print("----")
