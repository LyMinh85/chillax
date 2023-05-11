import customtkinter as ctk

from views.HomeFrame import HomeFrame
from views.MusicLibraryFrame import MusicLibraryFrame
from views.PlaylistFrame import PlaylistFrame
from views.SettingFrame import SettingFrame


class RightFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.list_page = (HomeFrame, MusicLibraryFrame, PlaylistFrame, SettingFrame)
        self.current_page = None

        self.frames = {}
        for page in self.list_page:
            page_name = page.__name__
            frame = page(self)
            self.frames[page_name] = frame

        self.current_page = self.frames[HomeFrame.__name__]
        self.show_frame(HomeFrame.__name__)

    def show_frame(self, page_name):
        self.current_page.grid_forget()
        frame = self.frames[page_name]
        self.current_page = frame
        frame.grid(row=0, column=0, sticky="nsew")

