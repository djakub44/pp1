class song:
    def __init__(self,name,artist,album,year):
        self.name = name
        self.artist = artist
        self.album = album
        self.year = year
    
    def __str__(self):
        return "Performer: " + self.artist + "\nSong: " + self.name + "\nAlbum: " + self.album + "\nYear: " + str(self.year)
    
if __name__ == "__main__":

    song1 = song("stayin alive", "Bee Gees", "Im not sure", 1970)
    song2 = song("Parostatkiem w piekny rejs","Krzysztof Krawczyk","jakis album",1985)

    print(song1)
    print("")
    print(song2)
