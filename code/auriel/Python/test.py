import tkinter as tk
from tkinter import Label, Toplevel, ttk
from lyricsgenius import Genius
import lyricsgenius

# Create root window with application name
root = tk.Tk()
root.geometry('300x300')
root.resizable(False, False)
root.title('Lyric Finder')

# Show a label with welcome message
label = ttk.Label(
    root,
    text = 'Welcome To Lyric finder'
)
label.pack(ipadx=10, ipady=10)

# Store artist name and song name
song_input = tk.StringVar()
artist_input = tk.StringVar()

# Function for search button
def search_clicked():
    genius = lyricsgenius.Genius(access_token='4Lpv5s9uvBkfdvP6eYk6BGDBAz1Uluafc0qt6oy7OTURbQYzmW6Y3ukOu95yCO5P')
    genius = Genius()

    if song_input == '':
        artist = genius.search_artist(f'{artist_input}', max_songs = None, sort = 'title', include_features = True )
        sl_window = Toplevel(root)
        sl_window.geometry('750x250')
        Label(
            sl_window,
            text = artist
        ).pack(ipady = 30)

# Entry box for artist name 
artist_label = ttk.Label(
    root,
    text = 'Artist Name:'
)
artist_label.pack(fill = 'x', expand = True)

artist_entry = ttk.Entry(
    root,
    textvariable = artist_input
)
artist_entry.pack(fill = 'x', expand = True)
artist_entry.focus()

# Entry box for artist name 
song_label = ttk.Label(
    root,
    text = 'Song Name:'
)
song_label.pack(fill = 'x', expand = True)

song_entry = ttk.Entry(
    root,
    textvariable = song_input
)
song_entry.pack(fill = 'x', expand = True)
song_entry.focus()

# Search button
search_button = ttk.Button(
    root,
    text = 'Search',
    command = search_clicked
)
search_button.pack(
    fill = 'x',
    expand = False,
    ipady = 5
)

# Exit button
exit_button = ttk.Button(
    root,
    text = 'Exit',
    command = root.destroy
)
exit_button.pack(
    fill = 'x',
    expand = False,
    ipady = 5
)

root.mainloop()