import lyricsgenius
artist_input = input('Enter name: ')

genius = lyricsgenius.Genius(access_token='hw_boxg7Ur3re20KM_3bK9qCAhXhdGe8OUYoDnz3Lh720FmbWARu7eD8cpdzs5TP')

artist = genius.search_artist(f'{artist_input}', max_songs = 3, sort = 'title')

artist.save_lyrics()