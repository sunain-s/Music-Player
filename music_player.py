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
