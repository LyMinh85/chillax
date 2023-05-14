from mutagen import File, FileType
from mutagen.id3 import ID3
from dto.Song import Song


class MusicLibrary:
    def __init__(self):
        self.list_song: list[Song] = []

    def add_song(self, song):
        for s in self.list_song:
            if s.file_path == song.file_path:
                return
        self.list_song.append(song)

    def get_song_from(self, file_path):
        file: FileType = File(file_path, easy=True)
        try:
            tags = ID3(file_path)
            if file['title'] is not None:
                song_title = file['title'][0]
            else:
                import os
                song_title = os.path.basename(file_path)
            artwork = tags.getall('APIC')[0].data  # access APIC frame and grab the image
        except Exception:
            import os
            song_title = os.path.basename(file_path)
            artwork = ""

        album = "Unknown"
        artist = "Unknown"
        try:
            album = file['album'][0]
            artist = file['artist'][0]
        except KeyError:
            pass

        song = Song(song_title, file_path, file.info.length)
        song.artwork = artwork
        song.album = album
        song.artist = artist
        return song

    def get_list_song_from(self, folder_path):
        import glob
        for filename in glob.glob(folder_path + "/*.mp3"):
            file_path = filename
            song = self.get_song_from(file_path)
            self.add_song(song)


music_library = MusicLibrary()
