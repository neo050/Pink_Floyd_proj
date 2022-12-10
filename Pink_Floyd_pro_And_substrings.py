
from functools import reduce
from functools import reduce
from itertools import combinations


class Song:


    def __init__(self, theSong):


        self.name, self.singer, self.sonGTime, self.lyrics, self.theAlbum = theSong
        b = self.lyrics.split()
        a = ""
        for i in range(b.__len__()):
            if i % 10 == 0:
                a = a + " " + '\n' + b[i]
            else:
                a = a + " " + b[i]

        self.lyrics = a

    def getName(self):

        return self.name

    def len(self):
        return self.lyrics.__len__()

    def getlyrics(self):
        return self.lyrics

    def getTheAlbum(self):
        return self.theAlbum


class Album:


    def __init__(self, name):

        g = name.split("::")
        self.name, self.time, self.Songs, self.NamesOfSong = g[0], g[1], {}, ""

    def addSong(self, Song):

        self.Songs[Song.getName()] = Song
        self.NamesOfSong += Song.getName() + "\n"

    def getName(self):

        return self.name

    def gettime(self):

        return self.time

    def GetSongs(self):

        return self.Songs

    def GetNamesOfSongs(self):

        return self.NamesOfSong


def ChargingPinkFloydIntoTheSystem():

    a = ""
    Albums = []
    listOfSongs = {}
    try:
        with open(input("Enter name of file: "), 'r', encoding='utf8') as f:
            for line in f:
                a += line.strip()
                # a.split("#")
            # print(a)
            b = a.split("#")
            for i in range(1, b.__len__()):
                c = b[i].split("*")
                album = Album(c[0])
                Albums.append(album)
                ## print(c[0])
                for j in range(1, c.__len__()):
                    d = c[j].split("::")
                    d.append(album)
                    song = Song(tuple(d))
                    listOfSongs[song.getName()] = song
                    album.addSong(song)

            # print(c)
            # print(c[1])
    except OSError as err:
        print(f" the file Not found OS error: {err}.")
        return 0
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")
        return 0
    return Albums, listOfSongs



try:
    listOfAlbum, listOfSongs = ChargingPinkFloydIntoTheSystem()

except BaseException as err:
   print(f"Unexpected {err}, {type(err)}")
   exit(0)


def NamesOfAlbums():
    for i in range(listOfAlbum.__len__()):
        print(listOfAlbum[i].getName(), listOfAlbum[i].gettime())


def NamesOfSongsByAlbum(string):
    for i in range(listOfAlbum.__len__()):
        if listOfAlbum[i].getName() == string:
            print(listOfAlbum[i].NamesOfSong)
            return


def lenOFSongs(string):
    if listOfSongs[string].getName() == string:
        print(listOfSongs[string].len())


def lyricsOFSong(string):
    if listOfSongs[string].getName() == string:
        print(listOfSongs[string].getlyrics())


def getTheAlbum(string):
    if listOfSongs[string].getName() == string:
        print(listOfSongs[string].getTheAlbum().getName())


def Getnamesbythelyrics(string):
    searchforlyrics(listOfSongs.values(), string)


def GetnamesbytheWord(string):
    searchforWord(listOfSongs.keys(), string)


def searchforlyrics(values, searchFor):
    for k in values:
        if searchFor.__len__() > 1:
            if searchFor[0].lower() + searchFor[1:] in k.getlyrics() or searchFor[0].upper() + searchFor[
                                                                                               1:] in k.getlyrics():
                print(k.getName())
        elif searchFor.__len__() == 1:
            if searchFor[0].lower() in k.getlyrics() or searchFor[0].upper() in k.getlyrics():
                print(k.getName())


def searchforWord(values, searchFor):
    for k in values:
        if searchFor.__len__() > 1:
            if searchFor[0].lower() + searchFor[1:] in k or searchFor[0].upper() + searchFor[1:] in k:
                print(k)
        elif searchFor.__len__() == 1:
            if searchFor[0].lower() in k or searchFor[0].upper() in k:
                print(k)


def exm1():
    try:


        while True:

            print(
                "Enter 1 --> List of albums\n Enter 2 --> List of songs on the album\n Enter 3 --> Getting the length of a song\nEnter 4 --> Getting lyrics to a song \nEnter 5 --> What album is the song on?\nEnter 6 --> Search song by name\nEnter 7 --> Search a song by lyrics in a song\nEnter 8--> EXIT")
            x = input()
            while not x.isdigit():
                x = input("Enter number only(int)")
            x = int(x)
            if x == 1:
                NamesOfAlbums()
            if x == 2:
                NamesOfSongsByAlbum(input("Enter Album: "))
            if x == 3:
                lenOFSongs(input("Enter name of song:"))
            if x == 4:
                lyricsOFSong(input("Enter name of song:"))
            if x == 5:
                getTheAlbum(input("Enter name of song:"))
            if x == 6:
                GetnamesbytheWord(input("Enter word from song name:"))
            if x == 7:
                Getnamesbythelyrics(input("Enter lyrics from song:"))
            if x == 8:
                break
            print("\n\n")
    except BaseException as err:
        print(f"Unexpected {err}, {type(err)}")
        exit(0)


dix = {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7: 'pqrs', 8: 'tuv', 9: 'wxyz'}

exm1()
def select():
    a = ''
    x = input("select numbers 2-9:")
    if x.isdigit() and '1' not in x:
        for i in x:
            if int(i) in dix.keys():
                a += dix[int(i)]
    return a


def solve(s):
   st_arr = []

   for i in range(len(s)-1,-1,-1):
      for j in range(len(st_arr)):
         st_arr.append(s[i]+st_arr[j])
      st_arr.append(s[i])
   print(st_arr.__len__())
   return st_arr

try:
    print(solve(select()))

except BaseException as err:
   print(f"Unexpected {err}, {type(err)}")
   exit(0)

