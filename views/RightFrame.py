import customtkinter as ctk
import config
from views.HomeFrame import HomeFrame
from views.MusicLibraryFrame import MusicLibraryFrame
from views.PlaylistFrame import PlaylistFrame
from views.SettingFrame import SettingFrame


class RightFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.parent = master
        self.list_page = (HomeFrame, MusicLibraryFrame, PlaylistFrame, SettingFrame)
        self.current_page = None

        self.frames = {}
        for page in self.list_page:
            page_name = page.__name__
            frame = page(self)
            self.frames[page_name] = frame

    def show_frame(self, page_name):
        if self.current_page is not None:
            self.current_page.grid_forget()
        frame = self.frames[page_name]
        frame.configure(fg_color=config.right_frame_background_color)

        # if choose Home page
        if page_name == HomeFrame.__name__:
            # Render recent listened songs
            frame.on_render()

        frame.grid(row=0, column=0, sticky="nsew")
        self.current_page = frame

