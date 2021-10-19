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
    
# removes a song from a given playlist
def remove_song(playlist, playlist_name):
    save = False
    while not save:
        print(f'Enter the corresponding number for which song you want to remove from [{playlist_name}]\n')
        # outputs tracks and track position
        i = 1
        for track in playlist:
            print(f'{i} - {track}')
            i += 1
        action = input('\nEnter song number or "save" to save the playlist and return to menu:  ')
        if action == 'save':
            save_playlist(playlist, playlist_name, new_playlist=False)
        # input validification check
        elif not action.isdigit() or int(action) > len(playlist) or int(action) < 1:
            print('Invalid input, enter the corresponding number for the song you would like to add')
        else:
            playlist.remove(playlist[int(action) - 1])
            
# adds a song to a given playlist
def add_song(playlist_name, songs, playlist, new_playlist):
    save = False
    print(f'Enter the corresponding number for which song you want to add to [{playlist_name}]\n')
    for song in songs:
        print(f'{songs.index(song) + 1} - {song}')

    while not save:
        action = input('\nEnter song number or "save" to save the playlist and return to menu:  ')
        if action == 'save':
            save_playlist(playlist, playlist_name, new_playlist)
        # input validification check
        elif not action.isdigit() or int(action) > len(songs):
            print('Invalid input, enter the corresponding number for the song you would like to add')
        # checks if song is already in playlist
        elif songs[int(action) - 1] in playlist:
            print(f'{songs[int(action) - 1]} is already in [{playlist_name}] please select another song')
        else:
            playlist.append(songs[int(action) - 1])
        
        print(f'{playlist_name}:\n')
        # outputs tracks and track position
        i = 1
        for song in playlist:
            print(f'{i} - {song}')
            i += 1

# allows user to change playlist track order
def move_song(playlist, playlist_name):
    save = False
    while not save:
        print('\n')
        # outputs tracks and track position
        i = 1
        for track in playlist:
            print(f'{i} - {track}')
            i += 1
        action = input(f'Enter the corresponding number for which song you would like to move, or "save" to save the playlist and return to menu:  ')
        if action == 'save':
            save_playlist(playlist, playlist_name, new_playlist=False)         
        # input validification check
        if not action.isdigit() or int(action) > len(playlist):
            print(f'Invalid input, please enter the corresponding number for the song you would like to move.')
        else:
            song = playlist[int(action) - 1]
            new_pos = input(f'Which position would you like to move {song} to?:  ')
            # input validification check
            if not new_pos.isdigit() or int(new_pos) > len(playlist):
                print(f'Invalid input, please enter the corresponding number for the position you would like to move {song} to.')
            else:
                # moves song to new position
                playlist.remove(playlist[int(action) - 1])
                playlist.insert(int(new_pos) - 1, song)
