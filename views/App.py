import math
from tkinter import filedialog

import customtkinter as ctk
import pygame

import config
from views.LeftFrame import LeftFrame
from views.MusicPlayerFrame import MusicPlayerFrame
from views.RightFrame import RightFrame
from controllers.MusicPlayer import music_player
from PIL import Image
from io import BytesIO

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
            self, width=250, fg_color=config.left_frame_background_color, corner_radius=0
        )
        self.left_frame.grid(row=0, column=0, sticky="nsew")

        self.add_folder_image = ctk.CTkImage(dark_image=Image.open("assets/images/folder-add.png"), size=(30, 30))
        self.add_folder_button = ctk.CTkButton(
            self.left_frame,
            text="Load a audio file",
            text_color="white", fg_color="#a61313", hover_color="#d51818",
            image=self.add_folder_image,
            anchor="w",
            command=self.btn_load_on_click,
        )
        self.add_folder_button.grid(row=6, column=0, columnspan=3, padx=20, pady=360, sticky="swe")

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

    # Function to quit the program and stop the loop
    def quit_program(self):
        self.destroy()

    def btn_load_on_click(self):
        # Ask for open mp3 file
        file_path = filedialog.askopenfilename(filetypes=[("mp3 Files", "*.mp3")])
        if file_path == "":
            return
        music_player.load_song(file_path)
        # Update song information in music player frame
        self.music_player_frame.song_name_label.configure(text=music_player.song.title)
        self.music_player_frame.artwork_image.configure(dark_image=Image.open(BytesIO(music_player.song.artwork)))
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
