from mutagen import File, FileType
from mutagen.id3 import ID3
from dto.Song import Song


class MusicLibrary:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

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

        song = Song(song_title, file_path, file.info.length)
        song.artwork = artwork
        return song


music_library = MusicLibrary()
