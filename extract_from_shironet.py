import requests
from bs4 import BeautifulSoup
import codecs
import json


def extract():
    output = []
    num_of_singers = 0
    for j in range(16, 22):
        url = 'https://shironet.mako.co.il/html/indexes/performers/heb_' + str(j) + '_popular.html'
        data = requests.get(url)
        soup = BeautifulSoup(data.text, "html.parser")
        next_pages = soup.find_all('a', class_="index_nav_bar")
        last_button = next_pages[len(next_pages) - 1]
        while '>>' in last_button.text:
            for a in soup.find_all('a', class_="index_link"):
                num_of_singers = num_of_singers + 1
                url = 'https://shironet.mako.co.il' + a.get('href')
                songs = get_song_page(url)
                for song in songs:
                    output.append(song)
            url = 'https://shironet.mako.co.il' + last_button.get('href')
            data = requests.get(url)
            soup = BeautifulSoup(data.text, "html.parser")
            next_pages = soup.find_all('a', class_="index_nav_bar")
            last_button = next_pages[len(next_pages) - 1]
    print(num_of_singers)
    return output


def get_song_page(url):
    songs = []
    data = requests.get(url)
    soup = BeautifulSoup(data.text, "html.parser")
    for span in soup.find_all('span', class_="artist_normal_txt"):
        singer_name = soup.find('h1').text
        for a in span.find_all('a', class_="artist_player_songlist"):
            url = "https://shironet.mako.co.il/" + a.get('href')
            song_name = a.text.strip()
            if len(filter_hebrew(singer_name)) > 0 and len(filter_hebrew(song_name)) > 0:
                try:
                    print('"' + song_name + '"' + " של " + singer_name + " - " + url)
                    dictionary = {"singer": singer_name, "song": song_name, "lyrics": get_lyrics(url), "url": url}
                    print(dictionary["lyrics"])
                    update_json(dictionary, "db.json")
                except:
                    continue
    return songs


def get_lyrics(url):
    try:
        data = requests.get(url)
        soup = BeautifulSoup(data.text, "html.parser")
        test = soup.find(itemprop="Lyrics")
        output = ""
        for t in test.contents[0::2]:
            output = output + filter_hebrew(t.text.replace('"', ' ')) + " "
        return output.replace('\r', ' ')
    except:
        return ""


def filter_hebrew(s):
    output = ""
    for c in s:
        if 1424 <= ord(c) <= 1514 or 32 <= ord(c) <= 126:
            output = output + c
    return output


def update_json(dictionary, file_name):
    # with codecs.open("db.json", "a", "utf8") as fd:
    #     data = json.load(fd)

    with open(file_name) as fp:
        data = json.load(fp)
    data.append(dictionary)
    print(len(data))
    json_obj = json.dumps(data, ensure_ascii=False, indent=4, separators=(',', ': '))
    # with codecs.open("db.json", "a", "utf8") as fd:
    #     fd.write(json_obj)
    with open(file_name, "w") as fd:
        fd.write(json_obj)


def is_hebrew(s):
    for c in s:
        if not 1424 <= ord(c) <= 1514:
            return False
    return True
