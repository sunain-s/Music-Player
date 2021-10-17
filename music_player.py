# Music Player
import sys
import os
import random

# reads from file and adds songs to a usable list
def song_list():
    songs = []
    with open('songs.txt', 'r') as file:
        for line in file:
            songs.append(line.rstrip('\n'))
    return songs

# lets the user view the song options
def view_song_list(songs):
    i = 1
    print('\n')
    for song in songs:
        print(f'{i} - {song}')
        i += 1
    print('\n')
    main()
    
# saves new playlist to 'playlists.txt'
def save_new_playlist(playlist_name):
    with open('playlists.txt', 'a') as file:
        file.write(playlist_name + '\n')
    main()

# writes playlist tracks to a file, saving it for future use
def save_playlist(playlist, playlist_name, new_playlist):
    print(f'[{playlist_name}] has been saved with {len(playlist)} tracks\n')

    with open(playlist_name + '.txt', 'w') as file:
        for song in playlist:
            file.write(f'{song}\n')
    
    if new_playlist:
        save_new_playlist(playlist_name)
    main() 
    
