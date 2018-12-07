from transportation import transportation


class artistSongs(object):
    """This is the artist class used to house songs... maybe"""
    artist = ""
    songs = []

    def __init__(self, artist, songs):
        self.artist = artist
        self.songs = songs

    def getSongsForArtist(self, artistId):
        queryString = "https://api.genius.com/artists/" + \
            str(artistId) + "/songs?per_page=50"
        # TODO:  build in dynamic paging here. Currently this can only take 50 per shot. :(
        artistResult = transportation.getResult(
            transportation, queryString)
        return artistResult
