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
