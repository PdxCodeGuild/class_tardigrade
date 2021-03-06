import tkinter as tk
from tkinter import Frame, Label, StringVar, Toplevel, ttk
import lyricsgenius

# Create root window with application name
root = tk.Tk()
root.geometry('300x300')
root.resizable(True, True)
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
    genius = lyricsgenius.Genius(access_token='hw_boxg7Ur3re20KM_3bK9qCAhXhdGe8OUYoDnz3Lh720FmbWARu7eD8cpdzs5TP')
    song = genius.search_song(title = song_input.get(), artist = artist_input.get())
    
    lyric_output = tk.StringVar()
    lyric_output.set(song.lyrics)

    new_win = tk.Toplevel(root)
    new_win.geometry('250x650')
    new_win.title(f'Lyrics for {song_input.get()} by {artist_input.get()}')
    Label(
        new_win,
        text = f'{lyric_output.get()}'
    ).pack()
    
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