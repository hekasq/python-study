from projects.spotify_time_machine.scraper import Scraper
from bs4 import BeautifulSoup
from datetime import datetime

import re

from projects.spotify_time_machine.spotify_api import get_playlist, get_artist, get_song_uri, add_songs_to_playlist, \
    create_playlist, get_song_uri

song_list_class = "o-chart-results-list-row-container"


def get_time_travel_date():
    result = input("Which year do you want to travel to? Type the data in this format: YYYY-MM-DD")
    try:
        datetime.strptime(result, "%Y-%m-%d")
    except:
        print("Invalid time format.")
        exit()
    print(result)
    return result


def get_billboard_for_date(desired_date):
    return Scraper().scrape(desired_date)


def parse_site_to_songs(raw_file):
    songs = []
    soup = BeautifulSoup(raw_file, "html.parser")
    song_list = soup.findAll("div", class_=song_list_class)

    for song_container in song_list:
        try:
            elements = song_container.text.replace("\n", "")
            lists = re.split('\t+', elements)
            songs.append(lists[2])
        except Exception as e:
            print(e)

    return songs


def ensure_playlist(desired_date):
    playlist_name = f"Top Billboard {desired_date}"
    id = get_playlist(playlist_name)
    if id is None:
        id = create_playlist(playlist_name)
    return id


def add_songs_to_spotify(desired_date, songs):
    playlist = ensure_playlist(desired_date)
    song_uris = []
    for song in songs:
        uri = get_song_uri(song)
        if uri is not None:
            song_uris.append(uri)
    add_songs_to_playlist(playlist, song_uris)


if __name__ == '__main__':
    print("Welcome to the Spotify Time Machine")
    desired_date = get_time_travel_date()
    raw_file = get_billboard_for_date(desired_date)
    songs = parse_site_to_songs(raw_file)
    add_songs_to_spotify(desired_date, songs)
