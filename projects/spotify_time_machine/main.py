from projects.spotify_time_machine.scraper import Scraper
from bs4 import BeautifulSoup

songs = []


def get_time_travel_date():
    result = input("Which year do you want to travel to? Type the data in this format: YYYY-MM-DD")
    # validate result format
    print(result)
    return result


def get_billboard_for_date(desired_date):
    return Scraper().scrape(desired_date)


def parse_site_to_songs(raw_file):
    soup = BeautifulSoup(raw_file, "html.parser")
    html_list = soup.findAll("div", class_="o-chart-results-list-row-container")
    for container in html_list:
        # malformed string, null handling
        try:
            # number = str(container.find(class_=rating_class).text).strip()
            # song_name = str(container.find(id="title-of-a-story").text).strip()
            #  author_name = str(container.find(class_=author_name_class).text).strip()
            lines = container.text.split('\n')
            non_empty_lines = [line for line in lines if line.strip() != '']
            result = ''
            for entry in non_empty_lines[:3]:
                result = result + entry.replace('\t', '') + ","

            songs.append(result[:-1])


        except Exception as e:
            print(e)

    print(songs)


if __name__ == '__main__':
    print("Welcome to the Spotify Time Machine")
    desired_date = get_time_travel_date()
    raw_file = get_billboard_for_date(desired_date)
    songs = parse_site_to_songs(raw_file)
