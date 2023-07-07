class Song:
    count = 0
    genres = []
    artists = []
    names = []
    genre_count = {}
    artist_count = {}
    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.count +=1
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_names(name)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def get_song_count(cls):
        return cls.count
    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.append(genre)
    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.append(artist)
    @classmethod
    def add_to_names(cls, name):
        cls.names.append(name)
    @classmethod
    def add_to_genre_count(cls, genre):
        if genre not in cls.genre_count:
            cls.genre_count[genre] = 1
        else:
            cls.genre_count[genre] += 1
    @classmethod
    def add_to_artist_count(cls, artist):
        if artist not in cls.artist_count:
            cls.artist_count[artist] = 1
        else:
            cls.artist_count[artist] += 1

        



            



    