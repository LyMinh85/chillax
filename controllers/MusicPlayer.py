import pygame
from mutagen import File, FileType
from mutagen.id3 import ID3
from dto.Song import Song


class MusicPlayer:
    def __init__(self):
        self.song = None
        self.current_time = 0
        self.is_playing = False
        self.is_pause = False
        self.is_load = False
        self.is_mute = False
        self.volume = 100

    def get_song_from(self, file_path):
        file: FileType = File(file_path, easy=True)
        tags = ID3(file_path)
        if file['title'] is not None:
            song_title = file['title'][0]
        else:
            import os
            song_title = os.path.basename(file_path)
        artwork = tags.getall('APIC')[0].data  # access APIC frame and grab the image
        self.song = Song(song_title, file_path, file.info.length)
        self.song.artwork = artwork

    # Function to browse and load a song
    def load_song(self, file_path: str):
        self.get_song_from(file_path)
        pygame.mixer.music.load(self.song.file_path)
        self.is_load = True


music_player = MusicPlayer()
