from transportation import transportation
import json

numberOfPagesToGet = 10
numberOfSongsPerPage = '1'

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

    def getSongObjectsForArtist(self, artistId):
        page = 1
        responseArray = []
        songs = None
        queryString = "https://api.genius.com/artists/" + \
            str(artistId) + "/songs"

        while page != None and page <= numberOfPagesToGet:
            parameters = {'per_page': numberOfSongsPerPage, 'page': str(page)}
            songsCallResponse = transportation.getJsonResult(
                transportation, queryString, parameters)
            songs = songsCallResponse['response']['songs']
            for song in songs:
                if song["primary_artist"]["id"] == artistId:
                    responseArray.append(song)

            # print("got songs:" + str(len(responseArray)))
            nextPage = songsCallResponse['response']['next_page']
            page = nextPage
        return responseArray

    def getSongLyrics(self, songUrl):
        queryString = songUrl
        pageResult = transportation.getPageResult(
            transportation, queryString)

        lyrics = pageResult.find("div", class_="lyrics").get_text()
        return lyrics
