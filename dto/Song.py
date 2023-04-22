import time


class Song:
    def __init__(self, title: str, file_path: str, length: float):
        self.title = title
        self.file_path = file_path
        self.length = length
        self.artwork = ""

    # Method return a duration of song
    # with format hh:mm:ss
    # Example: 01:30:12
    def getTime(self):
        return time.strftime('%H:%M:%S', time.gmtime(self.length))
