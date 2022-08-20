import xml.etree.ElementTree as ET
import glob
import codecs
import re


class Parsing:

    def __init__(self):
        self.all_words = set()
        self.songs_lyrics = []

    def all_words_appear(self):
        filenames = glob.glob("../Lyrics/*/*.xml")
        i = 0

        for filename in filenames:
            i = i + 1
            lyrics = []
            hebrew_flag = False
            try:
                with codecs.open(filename, "r", "utf8") as f:
                    tree = ET.parse(f)
                    root = tree.getroot()

                    lgs = root[1][0][0]
                    titles = root[0][0][0][0]
                    titles = titles.text.split('\n')
                    artists = root[0][0][0][1].text.split('\n')
                    albums = root[0][0][0][4].text.split('\n')
                    for lg in lgs:
                        for l in lg:
                            words = l.text.split(' ')
                            if is_hebrew_song(words):
                                hebrew_flag = True
                                lyrics.append(l.text)
            except:
                continue
            if hebrew_flag:
                with codecs.open("../words_to_tag2.txt", "a", "utf8") as words_to_tag:
                    words_to_tag.write(titles[0] + "\n")
            self.songs_lyrics.append([titles[0], artists[0], ' '.join(lyrics),albums[0]])


def is_hebrew_song(words):
    for word in words:
        if re.search('[a-zA-Z]', word) is None:  # we want only the Hebrew words
            with codecs.open("../words_to_tag.txt", "a", "utf8") as words_to_tag:
                words_to_tag.write(word + "\n")
            return True
    return False


def remove_vav_and_hei(words):
    output = []
    for word in words:
        if word[0] == 'ה' or word[0] == 'ו':
            output.append(word[1:])
        else :
            output.append(word)
    return output


parsing = Parsing()
parsing.all_words_appear()
print("done")
