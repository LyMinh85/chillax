from PIL import Image
import customtkinter as ctk


class LeftFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        # -----------------------------------
        # Start init components
        # -----------------------------------
        # row 1
        self.logo_image = ctk.CTkImage(dark_image=Image.open("assets/images/logo.png"), size=(30, 30))
        self.logo_label = ctk.CTkLabel(
            self,
            width=50, height=50,
            text="",
            image=self.logo_image,
        )
        self.logo_label.grid(row=0, column=0)

        logo_name_font = ctk.CTkFont(size=20, weight="bold")
        self.logo_name_label = ctk.CTkLabel(
            self,
            text="Chillax",
            font=logo_name_font,
            width=150, justify="left", anchor="w",
            padx=10,
        )
        self.logo_name_label.grid(row=0, column=1)

        # row 1 col 0
        self.home_image = ctk.CTkImage(dark_image=Image.open("assets/images/home-image.png"), size=(30, 30))
        self.home_button = ctk.CTkButton(
            self,
            text="Home",
            fg_color="transparent",
            hover_color="gray30",
            image=self.home_image,
            anchor="w",
            corner_radius=0,
            command=self.home_button_event
        )
        self.home_button.grid(row=1, column=0, columnspan=3, sticky="ew")

        # row 2 col 0
        self.library_image = ctk.CTkImage(dark_image=Image.open("assets/images/libray-image.png"), size=(30, 30))
        self.library_button = ctk.CTkButton(
            self,
            text="Music Library",
            fg_color="transparent",
            hover_color="gray30",
            image=self.library_image,
            anchor="w",
            corner_radius=0,
            command=self.library_button_event
        )
        self.library_button.grid(row=2, column=0, columnspan=3, sticky="ew")

        self.playlist_image = ctk.CTkImage(dark_image=Image.open("assets/images/playlist-image.png"), size=(30, 30))
        self.playlist_button = ctk.CTkButton(
            self,
            text="Playlists",
            fg_color="transparent",
            hover_color="gray30",
            image=self.playlist_image,
            anchor="w",
            corner_radius=0,
            command=self.library_button_event
        )
        self.playlist_button.grid(row=4, column=0, columnspan=3, sticky="ew")

        self.setting_image = ctk.CTkImage(dark_image=Image.open("assets/images/settings.png"), size=(30, 30))
        self.setting_button = ctk.CTkButton(
            self,
            text="Settings",
            fg_color="transparent",
            hover_color="gray30",
            image=self.setting_image,
            anchor="w",
            corner_radius=0,
            command=self.library_button_event
        )
        self.setting_button.grid(row=5, column=0, columnspan=3, sticky="ew")
        # -----------------------------------
        # End init components
        # -----------------------------------


    def menu_button_event(self):
        self.select_button("menu")

    def home_button_event(self):
        self.select_button("home")

    def library_button_event(self):
        self.select_button("library")

    def select_button(self, name):
        if name == "home":
            self.home_button.configure(fg_color="gray25")
        else:
            self.home_button.configure(fg_color="transparent")

        if name == "library":
            self.library_button.configure(fg_color="gray25")
        else:
            self.library_button.configure(fg_color="transparent")