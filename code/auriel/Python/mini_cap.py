import tkinter as tk
from tkinter import ttk
import lyricsgenius as lg
from lyricsgenius import Genius


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
song = tk.StringVar()
artist = tk.StringVar()

# Function for search button
def search_clicked():
    ...

# Entry box for artist name 
artist_label = ttk.Label(
    root,
    text = 'Artist Name:'
)
artist_label.pack(fill = 'x', expand = True)

artist_entry = ttk.Entry(
    root,
    textvariable = artist
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
    textvariable = song
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
    expand = True,
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
    expand = True,
    ipady = 5
)

root.mainloop()