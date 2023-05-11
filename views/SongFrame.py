import customtkinter as ctk
from dto.Song import Song
from PIL import Image
from io import BytesIO


class SongFrame(ctk.CTkFrame):
    def __init__(self, master, song: Song, index: int, command, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.song = song
        self.index = index
        self.song_image = ctk.CTkImage(dark_image=Image.open(song.get_art_work()), size=(40, 40))
        self.song_button = ctk.CTkButton(
            self,
            text=song.title,
            fg_color="transparent",
            hover_color="gray30",
            anchor="w",
            corner_radius=0,
            image=self.song_image,
            command=lambda: command(index, song)
        )
        self.song_button.grid(row=0, column=0, sticky="we")

