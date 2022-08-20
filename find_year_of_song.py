import translators as ts
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
os.environ['SPOTIPY_CLIENT_ID'] = '37a41bb5e05a4e5daa6bfc59f78ce1ed'
os.environ['SPOTIPY_CLIENT_SECRET'] = 'f41d4dd6efc5442f9e298e7cfa381177'


def find_year(song_album, artist_name):
    artist_name = ts.google(artist_name)
    try:
        spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
        results = spotify.search(q='track:' + song_album, type='track')
        album_year = 2222
        for r in results['tracks']['items']:
            singer_name = r['artists'][0]['name']
            if name_matcher(singer_name, artist_name) > 0.75:
                track_id = r['id']
                # ss = spotify.
                # print(ss)
                track_album = spotify.track(track_id)['album']
                temp_year = track_album['release_date'][0:4]
                if int(temp_year) < int(album_year):
                    album_year = temp_year
        return album_year
    except:
        return 0


def name_matcher(s1, s2):
    perc = 0
    min_len = min(len(s1), len(s2))
    for i in range(0, min_len):
        if s1[i] == s2[i]:
            perc = perc + (1 / min_len)
    return perc