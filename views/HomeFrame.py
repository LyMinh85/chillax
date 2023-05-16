import customtkinter as ctk
import config
from controllers.Home import home
from views.SongFrame import SongFrame


class HomeFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.list_song = []
        self.parent = master
        self.current_choosing_frame: SongFrame | None = None
        self.list_song_frame: list[SongFrame] = []
        self.configure(fg_color=config.right_frame_background_color)
        title_font = ctk.CTkFont(size=24, weight="bold")
        self.title_label = ctk.CTkLabel(self, text="Home", font=title_font, width=100)
        self.title_label.grid(row=0, column=0, sticky="w", pady=5)
        self.title2 = ctk.CTkLabel(self, text="Recent media", font=("TkDefaultFont", 25, 'bold'))
        self.title2.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

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

    def on_render(self):
        print(home.list_recent_media)
        if home.list_recent_media is not []:
            self.render_list_song(
                home.list_recent_media,
                command=self.parent.parent.on_select_song  # access App class
            )

        # Count the list
        count_label = ctk.CTkLabel(
            self, text=f"Total: {len(home.list_recent_media)} music",
            font=("TkDefaultFont", 15, 'bold')
        )
        count_label.grid(row=len(self.list_song) + 2, column=0, sticky="w")
