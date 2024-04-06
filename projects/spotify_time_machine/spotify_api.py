import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

user = 'fnareva'


def get_spotify_client():
    client_id = '62b5270dbf74471ba447b24429a1a2f4'
    client_secret = '7e09345dc7be45de8c3211cfd2ed72ed'
    redirect_uri = 'http://localhost:8888/callback'
    scope = 'playlist-modify-private,playlist-read-private'

    return spotipy.Spotify(
        client_credentials_manager=SpotifyOAuth(client_id, client_secret=client_secret, redirect_uri=redirect_uri,
                                                scope=scope))


spotify = get_spotify_client()


def create_playlist(name):
    try:
        response = spotify.user_playlist_create(user=user, name=name, public=False, description=f"Playlist for ${name}")
        return response.get('id')
    except Exception as e:
        print(e)


def get_artist(name):
    try:
        result = spotify.search(q='Mariah Carey', type='artist')
        print(result)
    except Exception as e:
        print(e)


def get_song_uri(name):
    try:
        result = spotify.search(q=f"{name}", type='track')
        if result is None or len(result) == 0:
            print(f"Song {name} not found")
            return None
        return result.get('tracks').get('items')[0].get('uri')
    except Exception as e:
        print(e)


def get_song_tracks(name):
    try:
        result = spotify.search(q=f"{name}", type='track')
        if result is None or len(result) == 0:
            print(f"Song {name} not found")
            return None
        return result.get('tracks').get('items')[0].get('uri')
    except Exception as e:
        print(e)


def add_songs_to_playlist(playlist_id, song_uris):
    try:
        spotify.playlist_add_items(playlist_id=playlist_id, items=song_uris)
    except Exception as e:
        print(e)


def get_track_uri_bulk():
    pass


def get_playlist(playlist_name):
    try:
        playlists = spotify.user_playlists(user)
        for playlist in playlists['items']:
            if playlist_name == playlist['name']:
                return playlist.get('id')

        return None

    except Exception as e:
        print(e)
