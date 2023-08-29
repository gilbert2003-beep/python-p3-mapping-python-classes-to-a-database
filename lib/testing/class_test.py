# tests/test_song.py

from lib.song import Song

def test_create_table():
    Song.create_table()
    # Your assertions here

def test_create_song():
    song = Song.create("Hold On", "Born to Sing")
    # Your assertions here
