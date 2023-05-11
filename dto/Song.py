import time
from io import BytesIO


class Song:
    def __init__(self, title: str, file_path: str, length: float):
        self.title = title
        self.file_path = file_path
        self.length = length
        self.artwork = None

    def get_art_work(self):
        if isinstance(self.artwork, str):
            if self.artwork == "":
                return "assets/images/empty-artwork.png"
            else:
                return self.artwork
        else:
            return BytesIO(self.artwork)

    # Method return a duration of song
    # with format hh:mm:ss
    # Example: 01:30:12
    def getTime(self):
        return time.strftime('%H:%M:%S', time.gmtime(self.length))
