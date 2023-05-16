import customtkinter as ctk
import tkinter as tk
import config
from dto.Song import Song
from PIL import Image


class SongFrame(ctk.CTkFrame):
    def __init__(self, master, song: Song | None, index: int, command, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg_color=config.right_frame_background_color)
        self.grid(pady=2)
        self.is_selected = False
        self.parent = master
        self.song = song
        self.index = index
        self.command = command

        # Title row
        if index == -1:
            title_font = ctk.CTkFont(size=13, weight="bold")
            self.image_label = ctk.CTkLabel(self, text="", anchor="w", width=60, text_color=config.red_color, font=title_font, bg_color=config.right_frame_background_color)
            self.image_label.grid(row=0, column=0, sticky="wens")
            self.name_label = ctk.CTkLabel(self, text="Title", anchor="w", width=400, text_color=config.red_color, font=title_font, bg_color=config.right_frame_background_color)
            self.name_label.grid(row=0, column=1, sticky="wens")
            self.artist_label = ctk.CTkLabel(self, text="Artist", anchor="w", width=200, text_color=config.red_color, font=title_font, bg_color=config.right_frame_background_color)
            self.artist_label.grid(row=0, column=2, sticky="wens")
            self.album_label = ctk.CTkLabel(self, text="Album", anchor="w", width=140, text_color=config.red_color, font=title_font, bg_color=config.right_frame_background_color)
            self.album_label.grid(row=0, column=3, sticky="wens")
        else:
            self.song_image = ctk.CTkImage(dark_image=Image.open(song.get_art_work()), size=(40, 40))
            self.image_label = ctk.CTkLabel(self, image=self.song_image, text="", width=60, compound="left", bg_color=config.right_frame_background_color)
            self.image_label.grid(row=0, column=0, sticky="wens")
            self.name_label = ctk.CTkLabel(self, text=config.reduce_text(song.title, 50), anchor="w", width=400, bg_color=config.right_frame_background_color)
            self.name_label.grid(row=0, column=1, sticky="wens")
            self.artist_label = ctk.CTkLabel(self, text=config.reduce_text(song.artist, 20), anchor="w", width=200, bg_color=config.right_frame_background_color)
            self.artist_label.grid(row=0, column=2, sticky="wens")
            self.album_label = ctk.CTkLabel(self, text=config.reduce_text(song.album, 10), anchor="w", width=140, bg_color=config.right_frame_background_color)
            self.album_label.grid(row=0, column=3, sticky="wens")

        self.menu = tk.Menu(
            self, tearoff=0,
            background="gray20", relief=tk.FLAT,
            foreground="white", borderwidth=0,
            activeborderwidth=0
        )
        self.menu.add_command(label="Delete", command=self.on_click_delete)

        if index != -1:
            for label in (self.image_label, self.name_label, self.artist_label, self.album_label):
                label.bind("<Enter>", self.on_enter)
                label.bind("<Leave>", self.on_leave)
                label.bind("<Button-1>", self.on_click)
                label.bind("<Button-3>", self.do_popup)

    def on_click(self, event):
        self.command(self.index, self.song)

    def on_enter(self, event):
        self.image_label.configure(bg_color="gray20")
        self.name_label.configure(bg_color="gray20")
        self.artist_label.configure(bg_color="gray20")
        self.album_label.configure(bg_color="gray20")

    def on_leave(self, event):
        if not self.is_selected:
            self.image_label.configure(bg_color=config.right_frame_background_color)
            self.name_label.configure(bg_color=config.right_frame_background_color)
            self.artist_label.configure(bg_color=config.right_frame_background_color)
            self.album_label.configure(bg_color=config.right_frame_background_color)

    def set_selected(self, select: bool):
        if select:
            self.is_selected = True
            self.on_enter(None)
        else:
            self.is_selected = False
            self.on_leave(None)

    def do_popup(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def on_click_delete(self):
        self.parent.delete_song(self.index, self.song)

