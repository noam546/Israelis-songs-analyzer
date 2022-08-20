import process_text
import find_year_of_song
import codecs
# import extract_from_shironet
import json
import extract_data


def main():
    # extract_from_shironet.extract()
    with open("db.json") as fp:
        data = json.load(fp)
    print(len(data))
    has_words = 0
    with_year = 0
    num_of_singers = 0
    prev_singer = ""
    for song in data:
        song_lyrics = song["lyrics"]
        song_name = song["song"]
        song_singer = song["singer"]
        if song_singer != prev_singer:
            num_of_singers = num_of_singers + 1
            prev_singer = song_singer
        filter_words = process_text.process_text(song_lyrics)
        filter_words = extract_data.remove_vav_and_hei(filter_words)
        if len(filter_words) != 0:
            song_year = find_year_of_song.find_year(song_name, song_singer)
            has_words = has_words + 1
            print(str(num_of_singers) + " the year of " + song_name + " by " + song_singer + " is " + str(song_year))
            if int(song_year) != 2222:
                decade = int(song_year) - (int(song_year) % 10)
                with_year = with_year + 1
                with codecs.open("../words of " + str(decade) + ".txt", "a", "utf8") as fd:
                    for word in filter_words:
                        fd.write(word+"\n")
    print(has_words)
    print(with_year)


if __name__ == '__main__':
    main()
