from artistSongs import artistSongs

artistImLookingFor = 'aesop rock'  # todo: this should be more dynamic eventually
parsed = artistSongs.findArtist(artistSongs, artistImLookingFor)

# Here we start doing magic things
for item in parsed['response']['hits']:
    print(
        "Primary artist url:", item['result']['primary_artist']['url'],
        "Primary artist name:", item['result']['primary_artist']['name'])
    print("----")
