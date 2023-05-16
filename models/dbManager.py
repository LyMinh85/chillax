import sqlite3
from sqlite3.dbapi2 import Connection, Cursor
from dto.MusicLibraryDto import MusicLibraryDto


class Database:
    def __init__(self, db_file_path):
        self.db_file_path = db_file_path
        self.conn: Connection | None = None
        self.create_database_if_not_exist()

    def get_connection(self):
        if self.conn is None:
            self.conn = sqlite3.connect(self.db_file_path)
        return self.conn

    def close_connection(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None


    def create_database_if_not_exist(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS MusicLibrary (
                folderPath TEXT PRIMARY KEY
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Song (
                songId INTEGER PRIMARY KEY,
                title TEXT,
                artist TEXT,
                artwork TEXT,
                duration TIME,
                filePath TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Playlist (
                playlistId INTEGER PRIMARY KEY,
                title TEXT
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS PlaylistSong (
                songId INTEGER,
                playlistId INTEGER,
                songOrder INTEGER,
                FOREIGN KEY (songId) REFERENCES Song (songId),
                FOREIGN KEY (playlistId) REFERENCES Playlist (playlistId),
                PRIMARY KEY (songId, playlistId)
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Settings (
                settingsId INTEGER PRIMARY KEY,
                defaultMusicFolder TEXT,
                appSettings TEXT
            )
        ''')
        conn.commit()
        cursor.close()
        self.close_connection()


class MusicLibraryModel:
    def __init__(self, db: Database):
        self.db = db

    def get_all_music_library(self):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM MusicLibrary
        ''')

        rows = cursor.fetchall()
        list_music_library_dto: list[MusicLibraryDto] = []
        for row in rows:
            record = MusicLibraryDto(row[0])
            list_music_library_dto.append(record)

        cursor.close()
        self.db.close_connection()
        return list_music_library_dto

    def add_one(self, folder_path):
        conn = self.db.get_connection()
        cursor = conn.cursor()

        sql = 'INSERT INTO MusicLibrary(folderPath) VALUES(?)'

        cursor.execute(sql, (folder_path, ))
        conn.commit()
        cursor.close()
        self.db.close_connection()


database = Database("music_app.db")
music_library_model = MusicLibraryModel(database)

