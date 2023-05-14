import math
from io import BytesIO
from tkinter import filedialog

import customtkinter as ctk
import pygame
from PIL import Image

import config
from controllers.MusicPlayer import music_player
from controllers.MusicLibrary import music_library
from views.LeftFrame import LeftFrame
from views.MusicLibraryFrame import MusicLibraryFrame
from views.MusicPlayerFrame import MusicPlayerFrame
from views.RightFrame import RightFrame

ctk.set_default_color_theme("assets/red.json")


class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__()

        # After ids
        self.update_current_time_after_id = None

        # Initialize Pygame
        pygame.init()
        pygame.mixer.init()

        # -----------------------------------
        # Start init components
        # -----------------------------------
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(1, weight=1)

        # Left frame
        self.left_frame = LeftFrame(
            self, width=250, navigation_command=self.btn_navigation_on_click,
            fg_color=config.left_frame_background_color, corner_radius=0
        )
        self.left_frame.grid(row=0, column=0, sticky="nsew")
        self.left_frame.grid_rowconfigure(6, weight=1)

        # right frame
        self.right_frame = RightFrame(
            self, fg_color=config.right_frame_background_color, corner_radius=0
        )
        self.right_frame.grid(row=0, column=1, sticky="nsew")

        # Music player bar frame
        self.music_player_frame = MusicPlayerFrame(
            self, height=100, fg_color=config.music_player_bar_background_color, corner_radius=0
        )
        self.music_player_frame.grid(row=1, column=0, columnspan=2, sticky="sew")

        # -----------------------------------
        # End init components
        # -----------------------------------

        # Bind the window closing event to the quit_program function
        self.protocol("WM_DELETE_WINDOW", self.quit_program)

        # Set Home is default frame
        self.btn_navigation_on_click("HomeFrame", self.left_frame.home_button)

    # Function to quit the program and stop the loop
    def quit_program(self):
        self.destroy()

    def btn_navigation_on_click(self, page_name, button):
        # Change button color
        if self.left_frame.current_selected_button is not None:
            self.left_frame.current_selected_button.configure(fg_color="transparent")

        self.left_frame.current_selected_button = button
        self.left_frame.current_selected_button.configure(fg_color="gray30")

        self.right_frame.show_frame(page_name)

    def btn_load_on_click(self):
        # Ask for open folder
        folder_path = filedialog.askdirectory()
        if folder_path == "":
            return

        import glob
        for filename in glob.glob(folder_path + "/*.mp3"):
            file_path = filename
            song = music_library.get_song_from(file_path)
            music_library.add_song(song)

        self.right_frame.frames[MusicLibraryFrame.__name__].render_list_song(
            music_library.list_song,
            command=self.on_select_song
        )
        music_player.set_list_song(music_library.list_song)

    def on_select_song(self, index, song):
        music_library_frame = self.right_frame.frames[MusicLibraryFrame.__name__]
        if music_library_frame.current_choosing_frame is not None:
            music_library_frame.current_choosing_frame.set_selected(False)
        music_library_frame.current_choosing_frame = music_library_frame.list_song_frame[index]
        music_library_frame.current_choosing_frame.set_selected(True)

        music_player.current_song_index = index
        music_player.load_song(song.file_path)

        # Update song information in music player frame
        self.music_player_frame.song_name_label.configure(text=music_player.song.title)
        self.music_player_frame.artwork_image.configure(dark_image=Image.open(music_player.song.get_art_work()))
        self.music_player_frame.artwork_label.configure(image=self.music_player_frame.artwork_image)
        self.music_player_frame.current_playing_time.configure(text="00:00:00")
        self.music_player_frame.song_duration_time.configure(text=music_player.song.getTime())
        self.music_player_frame.play_button.configure(image=self.music_player_frame.play_image)

        self.music_player_frame.duration_slider.configure(from_=0, to=math.ceil(music_player.song.length))
        self.music_player_frame.duration_slider.set(0)

        # Refresh if music player is playing
        if music_player.is_playing:
            music_player.is_playing = False
            music_player.current_time = 0
            music_player.is_pause = False

        self.music_player_frame.play_song()
