import customtkinter as ctk

import config


class HomeFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=config.right_frame_background_color)
        self.title = ctk.CTkLabel(self, text="Home")
        self.title.grid(row=0, column=0, sticky="news")
