import customtkinter as ctk

import config
from controllers.MusicPlayer import music_player
from controllers.MusicLibrary import music_library
from views.SongFrame import SongFrame
from PIL import Image


class MusicLibraryFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=config.right_frame_background_color)
        self.parent = master
        self.list_song = []
        self.current_choosing_frame: SongFrame | None = None
        self.list_song_frame: list[SongFrame] = []

        title_font = ctk.CTkFont(size=24, weight="bold")
        self.title_label = ctk.CTkLabel(self, text="Music Library", font=title_font, width=100)
        self.title_label.grid(row=0, column=0, sticky="w", pady=5)

        self.add_folder_image = ctk.CTkImage(dark_image=Image.open("assets/images/folder-add.png"), size=(20, 20))
        self.add_folder_button = ctk.CTkButton(
            self,
            text="Add a folder",
            text_color="white", fg_color="#a61313", hover_color="#d51818",
            image=self.add_folder_image,
            anchor="w",
            command=self.parent.parent.btn_load_on_click,
        )
        self.add_folder_button.grid(row=0, column=0, pady=2, padx=50, sticky="e")

        self.title_row = SongFrame(self, index=-1, song=None, command=None)

        # Get default list song
        music_library.get_list_song_from(config.get_dir_path() + "/songs/ed sheeran")
        self.list_song = music_library.list_song
        self.render_list_song(
            list_song=self.list_song,
            command=self.parent.parent.on_select_song  # access App class
        )
        music_player.set_list_song(self.list_song)

    def render_list_song(self, list_song, command):
        if list_song is not []:
            for song_frame in self.list_song_frame:
                song_frame.grid_forget()
            self.list_song_frame = []

        self.list_song = list_song
        for index, song in enumerate(self.list_song):
            song_frame = SongFrame(
                self,
                index=index,
                song=song,
                command=command,
                bg_color=config.right_frame_background_color,
            )
            song_frame.grid(row=index + 2, column=0, sticky="we")

            self.list_song_frame.append(song_frame)

    def delete_song(self, index, song):
        music_library.delete_song(song)
        self.list_song = music_library.list_song
        self.render_list_song(
            list_song=self.list_song,
            command=self.parent.parent.on_select_song  # access App class
        )
        music_player.set_list_song(self.list_song)
