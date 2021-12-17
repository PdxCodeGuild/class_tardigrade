import lyricsgenius

artist_input = input('Enetr artist name: ')
song_input = input('Enter song name: ')


genius = lyricsgenius.Genius(access_token='hw_boxg7Ur3re20KM_3bK9qCAhXhdGe8OUYoDnz3Lh720FmbWARu7eD8cpdzs5TP')
song = genius.search_song(song_input, artist_input)

print(type(song.lyrics))
print(song.lyrics)