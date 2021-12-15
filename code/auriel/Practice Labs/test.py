import lyricsgenius
from lyricsgenius import Genius


genius = lyricsgenius.Genius(access_token='Ic-M8PkaB4baGt-st-sD1WnXHlGGZcwIPWM7z1eMhzk_7YjBjtjWo7Czwhu8X7Sj')
genius = Genius()
artist = genius.search_artist("Drake", max_songs=3, sort="title")
print(artist.songs)