from microbit import *
import music
import random


piano = [
    'F#4:2', 'G#4:2', 'A4:2', 'B4:2',
    'C#5:2', 'B4:2', 'A4:2', 'G#4:2',
    'F#4:2', 'E4:2', 'F#4:2', 'G#4:2',

    # Main Theme
    'A4:2', 'B4:2', 'C#5:2', 'D5:2',
    'E5:2', 'D5:2', 'C#5:2', 'B4:2',
    'A4:2', 'G#4:2', 'F#4:2', 'E4:2',
    'F#4:2', 'G#4:2', 'A4:2', 'B4:2',

    # Bridge
    'C#5:2', 'B4:2', 'A4:2', 'G#4:2',
    'F#4:2', 'E4:2', 'D#4:2', 'E4:2',
    'F#4:2', 'G#4:2', 'A4:2', 'B4:2',

    # Climax
    'C#5:2', 'D5:2', 'E5:2', 'F#5:2',
    'G#5:2', 'A5:2', 'B5:2', 'C#6:2',
    'D6:2', 'E6:2', 'F#6:2', 'G#6:2',

    # Outro
    'A5:2', 'G#5:2', 'F#5:2', 'E5:2',
    'D5:2', 'C#5:2', 'B4:2', 'A4:2',
    'G#4:2', 'F#4:2', 'E4:2', 'D#4:2',
    'E4:4', 'r:4'
]
happy_birthday = ['C4:2', 'E4:2', 'G4:2', 'C5:2',
    'D4:2', 'F4:2', 'A4:2', 'D5:2',
    'E4:2', 'G4:2', 'B4:2', 'E5:2',
    'F4:2', 'A4:2', 'C5:2', 'F5:2',

    'G4:2', 'B4:2', 'D5:2', 'G5:2',
    'A4:2', 'C5:2', 'E5:2', 'A5:2',
    'B4:2', 'D5:2', 'F5:2', 'B5:2',
    'C5:4', 'E5:4', 'G5:4', 'C6:4',

    # Repeat and expand for length
    'D4:2', 'F4:2', 'A4:2', 'D5:2',
    'E4:2', 'G4:2', 'B4:2', 'E5:2',
    'F4:2', 'A4:2', 'C5:2', 'F5:2',
    'G4:2', 'B4:2', 'D5:2', 'G5:2',

    'A4:2', 'C5:2', 'E5:2', 'A5:2',
    'B4:2', 'D5:2', 'F5:2', 'B5:2',
    'C5:4', 'E5:4', 'G5:4', 'C6:4',
    'C6:8', 'r:4']
bomb=['C4:4', 'r:2',
    'C4:4', 'r:2',
    'C4:4', 'r:1',
    'C4:4', 'r:1',
    'C4:4', 'r:1',
    'C4:4', 'r:1',
    'C4:2', 'r:1',
    'C4:2', 'r:1',
    'C4:1', 'r:1',
    'C4:1', 'r:1',
    'C3:8']
song=['C4:2', 'C4:2', 'D4:4', 'C4:4', 'F4:4', 'E4:8', 'r:2',
    'C4:2', 'C4:2', 'D4:4', 'C4:4', 'G4:4', 'F4:8', 'r:2',
    'C4:2', 'C4:2', 'C5:4', 'A4:4', 'F4:4', 'E4:4', 'D4:4', 'r:2',
    'Bb4:2', 'Bb4:2', 'A4:4', 'F4:4', 'G4:4', 'F4:8', 'r:4',

    # Repeat with slight variation
    'C4:2', 'C4:2', 'D4:4', 'C4:4', 'F4:4', 'E4:8', 'r:2',
    'C4:2', 'C4:2', 'D4:4', 'C4:4', 'G4:4', 'F4:8', 'r:2',
    'C4:2', 'C4:2', 'C5:4', 'A4:4', 'F4:4', 'E4:4', 'D4:4', 'r:2',
    'Bb4:2', 'Bb4:2', 'A4:4', 'F4:4', 'G4:4', 'F4:8', 'r:4']
tune=['A4:2', 'C5:2', 'B4:2', 'G4:2', 'E4:2', 'F4:2', 'G4:2', 'A4:4']

songs = [
    happy_birthday,
    piano,
    bomb,
    song,
    tune
    
]

song_titles = ["1", "2", "3", "4", "5"]
current_song = 0

def generate_frame():
    grid = []
    for y in range(5):
        row = ''
        for x in range(5):
            row += str(random.choice([0, 3, 6, 9]))
        grid.append(row)
    return Image(":".join(grid))

def play_song(song):
    music.set_tempo(bpm=150)
    for note in song:
        music.play([note], wait=False)
        display.show(generate_frame())
        sleep(300)
    display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():
        display.scroll(song_titles[current_song])
        play_song(songs[current_song])

    if button_b.was_pressed():
        current_song = (current_song + 1) % len(songs)
        display.scroll("Next: " + song_titles[current_song])