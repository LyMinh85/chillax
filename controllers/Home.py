from dto.Song import Song

class Home:
    def __init__(self):
        self.list_recent_media = []

    def add_song_to_list_recent_media(self, song: Song):
        for index, s in enumerate(self.list_recent_media):
            if s.file_path == song.file_path:
                # If this song already in list recent media
                # then move it to top
                self.list_recent_media.insert(0, self.list_recent_media.pop(index))
                return
        self.list_recent_media.insert(0, song)


home = Home()
