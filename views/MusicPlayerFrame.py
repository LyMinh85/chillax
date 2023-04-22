import math
import time
import customtkinter as ctk
import pygame
from PIL import Image
from controllers.MusicPlayer import music_player

# Set MUSIC_END event for pygame
MUSIC_END = pygame.USEREVENT+1
pygame.mixer.music.set_endevent(MUSIC_END)


class MusicPlayerFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # After ids
        self.check_music_ended_after_id = None
        self.current_playing_time_after_id = None

        # -----------------------------------
        # Start init components
        # -----------------------------------
        # self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # song info
        self.song_info_frame = ctk.CTkFrame(self, width=60, height=60, fg_color="transparent", corner_radius=0)
        self.song_info_frame.grid(row=0, column=0, sticky="w")

        # Image Artwork
        self.artwork_image = ctk.CTkImage(dark_image=Image.open("assets/images/empty-artwork.png"), size=(60, 60))
        self.artwork_label = ctk.CTkLabel(
            self.song_info_frame,
            width=60, height=60, text="",
            corner_radius=0
        )
        self.artwork_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

        # song name
        song_font = ctk.CTkFont(size=16, weight="bold")
        self.song_name_label = ctk.CTkLabel(
            self.song_info_frame, text="", width=200,
            font=song_font, anchor="sw", wraplength=200
        )
        self.song_name_label.grid(row=0, column=1)

        # music control frame
        self.music_control_frame = ctk.CTkFrame(self, height=60, fg_color="transparent", corner_radius=0)
        self.music_control_frame.grid(row=0, column=1, sticky="wens")
        self.music_control_frame.grid_columnconfigure(0, weight=1)

        # music control buttons frame
        self.music_control_buttons_frame = ctk.CTkFrame(self.music_control_frame, height=40, fg_color="transparent")
        self.music_control_buttons_frame.grid(row=0, column=0, pady=10)

        # Previous button
        self.previous_image = ctk.CTkImage(dark_image=Image.open("assets/images/previous-button.png"), size=(30, 30))
        self.previous_button = ctk.CTkButton(
            self.music_control_buttons_frame, text="", image=self.previous_image,
            width=15, height=15, fg_color="transparent",
            hover_color="gray30"
        )
        self.previous_button.grid(row=0, column=0)

        # Play or pause button
        self.play_image = ctk.CTkImage(dark_image=Image.open("assets/images/play-button.png"), size=(30, 30))
        self.pause_image = ctk.CTkImage(dark_image=Image.open("assets/images/pause-button.png"), size=(30, 30))
        self.play_button = ctk.CTkButton(
            self.music_control_buttons_frame, text="", image=self.play_image,
            width=15, height=15, fg_color="transparent", command=self.play_song,
            hover_color="gray30"
        )
        self.play_button.grid(row=0, column=1, padx=10)

        # Next button
        self.next_image = ctk.CTkImage(dark_image=Image.open("assets/images/next-button.png"), size=(30, 30))
        self.next_button = ctk.CTkButton(
            self.music_control_buttons_frame, text="", image=self.next_image,
            width=15, height=15, fg_color="transparent",
            hover_color="gray30"
        )
        self.next_button.grid(row=0, column=2)

        # music duration progress bar frame
        self.duration_frame = ctk.CTkFrame(self.music_control_frame, height=20)
        self.duration_frame.grid(row=1, column=0)

        # Current playing time label
        self.current_playing_time = ctk.CTkLabel(self.duration_frame, text="00:00:00")
        self.current_playing_time.grid(row=0, column=0)

        # music duration progress bar
        self.duration_slider = ctk.CTkSlider(
            self.duration_frame, width=200, height=10,
            from_=0, to=100, state="disabled"
        )
        self.duration_slider.set(0)
        self.duration_slider.grid(row=0, column=1, padx=10)

        # Song duration label
        self.song_duration_time = ctk.CTkLabel(self.duration_frame, text="00:00:00")
        self.song_duration_time.grid(row=0, column=2)

        # volume frame
        self.volume_frame = ctk.CTkFrame(self, height=60, fg_color="transparent", corner_radius=0)
        self.volume_frame.grid(row=0, column=2, sticky="wens")
        self.volume_frame.grid_rowconfigure(0, weight=1)
        self.volume_frame.grid_columnconfigure(0, weight=1)

        self.volume_frame_center_frame = ctk.CTkFrame(
            self.volume_frame, height=60,
            fg_color="transparent", corner_radius=0
        )
        self.volume_frame_center_frame.grid(row=0, column=0)

        # Volume image
        self.volume_image = ctk.CTkImage(dark_image=Image.open("assets/images/volume-button.png"), size=(20, 20))
        self.volume_mute_image = ctk.CTkImage(dark_image=Image.open("assets/images/volume-mute.png"), size=(20, 20))
        self.volume_button = ctk.CTkButton(
            self.volume_frame_center_frame, text="", image=self.volume_image,
            width=30, height=30, fg_color="transparent",
            hover_color="gray30", command=self.volume_button_on_click
        )
        self.volume_button.grid(row=0, column=0)

        # Volume slider
        self.volume_slider = ctk.CTkSlider(
            self.volume_frame_center_frame,
            from_=0, to=100, width=100, orientation='horizontal',
            command=self.volume_slider_on_drag
        )
        self.volume_slider.set(100)
        self.volume_slider.grid(row=0, column=1)

        # Volume value label
        self.volume_label = ctk.CTkLabel(
            self.volume_frame_center_frame, text="100", width=30
        )
        self.volume_label.grid(row=0, column=2, padx=10)
        # -----------------------------------
        # End init components
        # -----------------------------------

    # Function to set volume when drag volume slider
    def volume_slider_on_drag(self, slider_value):
        music_player.volume = math.ceil(slider_value)
        self.volume_label.configure(text="{}".format(music_player.volume))
        pygame.mixer.music.set_volume(music_player.volume / 100)

    # Function to start playing the loaded song
    def play_song(self):
        self.check_music_ended()
        if music_player.is_playing:
            if music_player.is_pause:
                print("resume")
                pygame.mixer.music.unpause()
                music_player.is_pause = False
                self.update_current_time()
                self.play_button.configure(image=self.pause_image)
            else:
                print("pause")
                pygame.mixer.music.pause()
                music_player.is_pause = True
                self.update_current_time()
                self.play_button.configure(image=self.play_image)
        elif not music_player.is_playing:
            print("play music")
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(music_player.volume)
            music_player.is_playing = True
            self.song_duration_time.configure(text=music_player.song.getTime())
            self.duration_slider.configure(to=math.ceil(music_player.song.length))
            self.play_button.configure(image=self.pause_image)
            self.update_current_time()

    # Function to keep track of the current time and update the label
    def update_current_time(self):
        # is playing or pausing
        if music_player.is_playing:
            current_time = pygame.mixer.music.get_pos()
            music_player.current_time = current_time
            if music_player.is_pause:
                # If pause cancel after
                self.current_playing_time.after_cancel(self.current_playing_time_after_id)
            else:
                # Increasing slider value by current of song
                self.duration_slider.set(current_time // 1000)
                time_str = time.strftime('%H:%M:%S', time.gmtime(current_time / 1000))
                self.current_playing_time.configure(text="{}".format(time_str))
                self.current_playing_time_after_id = self.current_playing_time.after(1000, self.update_current_time)
        # finished song
        else:
            self.current_playing_time.after_cancel(self.current_playing_time_after_id)
            self.play_button.configure(image=self.play_image)

    # Function to check is music end for every 0.1 second
    def check_music_ended(self):
        # Loop all event of pygame
        for event in pygame.event.get():
            if event.type == MUSIC_END:
                music_player.is_playing = False
                music_player.current_time = 0
                self.current_playing_time.configure(text=music_player.song.getTime())
                self.duration_slider.set(math.ceil(music_player.song.length))
                self.after_cancel(self.check_music_ended_after_id)

        # Repeat this function every 0.1 second
        self.check_music_ended_after_id = self.after(100, self.check_music_ended)

    # Function toggle mute or unmute volume
    def volume_button_on_click(self):
        if music_player.is_mute:
            music_player.is_mute = False
            self.volume_button.configure(image=self.volume_image)
            self.volume_slider_on_drag(100)
            self.volume_slider.set(100)
        else:
            music_player.is_mute = True
            self.volume_button.configure(image=self.volume_mute_image)
            self.volume_slider_on_drag(0)
            self.volume_slider.set(0)

