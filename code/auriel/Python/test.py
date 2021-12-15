import lyricsgenius as lg
from lyricsgenius import Genius

artist_input = input().lower()

genius = Genius()

artist = genius.search_artist(f'{artist_input}', max_songs = None, sort =  "title", include_features = True)

print(artist.songs)