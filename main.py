import csv
from gmusicapi import Mobileclient
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()

        self.songs = []
        self._current_song = None
        self.i = 0

    def handle_starttag(self, tag, attrs):
        if tag == 'div' and ('itemprop', 'track') in attrs:
            self._current_song = {}

        if self._current_song is not None and tag == 'meta':
            prop_value = None
            for name, value in attrs:
                if name == 'content':
                    prop_value = value
            if ('itemprop', 'name') in attrs:
                self._current_song['name'] = prop_value
            elif ('itemprop', 'inAlbum') in attrs:
                self._current_song['album'] = prop_value

    def handle_endtag(self, tag):
        if self._current_song and tag == 'div':
            self.songs.append(self._current_song)
            self._current_song = None
            self.i += 1


def create_csv():
    parser = MyHTMLParser()
    with open("Saavn.html") as f:
        parser.feed(f.read())

    print(parser.i)
    with open("output.csv", 'w') as f:
        w = csv.writer(f)
        w.writerow(['Name', 'Album'])
        for s in parser.songs:
            w.writerow([s['name'], s['album']])
        # json.dump(parser.songs, f)


def gpm():
    api = Mobileclient(debug_logging=True)


def main():
    gpm()


if __name__ == '__main__':
    main()
