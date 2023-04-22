import pygame
from PIL import Image, ImageTk
from views.App import App


def is_macos():
    import platform
    return platform.system() == "Darwin"


if __name__ == "__main__":
    app = App()

    width = 1000  # Width
    height = 700  # Height

    # Create the Tkinter app window
    # app.geometry("1000x700")
    if not is_macos():
        app.resizable(False, False)
    app.title("Music Player")
    ico = Image.open("assets/images/logo.png")
    photo = ImageTk.PhotoImage(ico)
    app.iconphoto(False, photo)
    screen_width = app.winfo_screenwidth()  # Width of the screen
    screen_height = app.winfo_screenheight()  # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)

    app.geometry('%dx%d+%d+%d' % (width, height, x, y))
    app.mainloop()
    # Quit Pygame
    pygame.mixer.quit()

