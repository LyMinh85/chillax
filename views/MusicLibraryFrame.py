import customtkinter as ctk

import config
from controllers.MusicPlayer import music_player
from views.SongFrame import SongFrame


class MusicLibraryFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=config.right_frame_background_color)
        self.grid_columnconfigure(0, weight=1)
        self.list_song = []
        self.current_choosing_frame: SongFrame | None = None
        self.list_song_frame: list[SongFrame] = []

    def add_song_list(self, list_song, command):
        self.list_song = list_song
        for index, song in enumerate(self.list_song):
            song_frame = SongFrame(
                self,
                index=index,
                song=song,
                command=command
            )
            song_frame.grid(row=index + 1, column=0, sticky="we")
            self.list_song_frame.append(song_frame)

