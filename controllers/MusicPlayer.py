import pygame
from controllers.MusicLibrary import music_library
from enum import Enum


class RepeatState(Enum):
    REPEAT_OFF = 1
    REPEAT_ONE = 2
    REPEAT_ALL = 3


class MusicPlayer:
    def __init__(self):
        self.list_song = []
        self.current_song_index = 0
        self.song = None
        self.current_time = 0
        self.is_playing = False
        self.is_pause = False
        self.is_load = False
        self.is_mute = False
        self.repeat_state: RepeatState = RepeatState.REPEAT_OFF
        self.volume = 100
        self.next_song = 0;

    def set_list_song(self, list_song):
        self.list_song = list_song

    # Function to browse and load a song
    def load_song(self, file_path: str):
        self.song = music_library.get_song_from(file_path)
        pygame.mixer.music.load(self.song.file_path)
        self.is_load = True

        print("index", self.current_song_index)
        print("list_song", len(self.list_song))

    def load_previous_song(self):
        if not self.has_previous_song():
            self.current_song_index = len(self.list_song) - 1
        else:
            self.current_song_index -= 1
        self.song = self.list_song[self.current_song_index]
        pygame.mixer.music.load(self.song.file_path)
        self.is_load = True

    def load_next_song(self):
        if not self.has_next_song():
            self.current_song_index = 0
        else:
            self.current_song_index += 1
        self.song = self.list_song[self.current_song_index]
        pygame.mixer.music.load(self.song.file_path)
        self.is_load = True

    def load_repeat_one_song(self):
        self.next_song = self.current_song_index
        self.song = self.list_song[self.next_song]
        pygame.mixer.music.load(self.song.file_path)
        self.is_load = True


    def has_next_song(self):
        return self.current_song_index + 1 < len(self.list_song)

    def has_previous_song(self):
        return self.current_song_index - 1 > -1

    def set_repeat_state(self, repeat_state: RepeatState):
        self.repeat_state = repeat_state


music_player = MusicPlayer()
