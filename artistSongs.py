from transportation import transportation
import json


class artistSongs(object):
    """This is the artist class used to house songs... maybe"""
    artist = ""
    songs = []

    def __init__(self, artist, songs):
        self.artist = artist
        self.songs = songs

    def findArtist(self, artistString):
        queryString = "https://api.genius.com/search"
        parameters = {'q': artistString}
        artistResult = transportation.getJsonResult(
            transportation, queryString, parameters)
        return artistResult

    def getSongsForArtist(self, artistId):
        page = 1
        responseArray = []

        songs = None
        while page < 20:

            queryString = "https://api.genius.com/artists/" + \
                str(artistId) + "/songs"
            parameters = {'per_page': '3', 'page': str(page)}
            songsCallResponse = transportation.getJsonResult(
                transportation, queryString, parameters)

            songs = songsCallResponse['response']['songs']
            responseArray.append(songs)

            print("got songs:" + str(len(responseArray)))

            nextPage = songsCallResponse['response']['next_page']
            page = nextPage

        return songs
