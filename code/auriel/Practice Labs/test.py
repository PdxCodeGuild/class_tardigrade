import lyricsgenius
import json
test = []

song_input = input('Enter song name: ')
artist_input = input('Enter artist name: ')
 
genius = lyricsgenius.Genius(access_token='hw_boxg7Ur3re20KM_3bK9qCAhXhdGe8OUYoDnz3Lh720FmbWARu7eD8cpdzs5TP')
song = genius.search_song(song_input, artist_input)

test.append(song.lyrics)

print(song.lyrics)