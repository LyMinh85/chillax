import customtkinter as ctk
import textwrap
import config


class SettingFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(fg_color=config.right_frame_background_color)
        title_font = ctk.CTkFont(size=50, weight="bold")
        title_font1 = ctk.CTkFont(size=20, weight="bold")
        self.title_label = ctk.CTkLabel(self, text="Setting", font=title_font, width=100)
        self.title_label.grid(row=0, column=0, sticky="w", pady=5)
        thu_cam_on = """
        Kính gửi người dùng,
        Cảm ơn các bạn đã sử dụng phần mềm này,
        Xin gửi lời cảm ơn đến Thầy Phiêu đã bồi dưỡng tụi em
        XIN TRÂN TRỌNG CẢM ƠN
        """
        thu_cam_on_wrapped = textwrap.dedent(thu_cam_on).strip()
        self.title_label1 = ctk.CTkLabel(
            self,
            text=thu_cam_on_wrapped,
            font=title_font1,
            width=100,
            justify="left"
        )
        self.title_label1.grid(row=3, column=0, sticky="w", pady=15)

        self.title_label = ctk.CTkLabel(
            self,
            text="THANKS YOU",
            font=("Arial", 24, "bold"),

        )
        self.title_label.grid(row=4, column=6, sticky="w", pady=15)



