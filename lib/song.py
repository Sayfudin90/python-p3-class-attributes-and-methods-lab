class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls,artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        cls.genre_count[genre] = cls.genre_count.get(genre, 0) + 1

    @classmethod
    def add_to_artist_count(cls, artist):
        cls.artist_count[artist] = cls.artist_count.get(artist, 0) + 1


# Example Usage:
ninety_nine_problems = Song("99 Problems", "Jay-Z", "Rap")
halo = Song("Halo", "Beyonce", "Pop")
god_plan = Song("God's Plan", "Drake", "Rap")

print(Song.count)  # 3
print(Song.genres)  # ['Rap', 'Pop']
print(Song.artists)  # ['Jay-Z', 'Beyonce', 'Drake']
print(Song.genre_count)  # {'Rap': 2, 'Pop': 1}
print(Song.artist_count)  # {'Jay-Z': 1, 'Beyonce': 1, 'Drake': 1}



