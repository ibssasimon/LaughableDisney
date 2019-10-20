import requests
import string
from bs4 import BeautifulSoup as bs
import re
 
def main():

    artist = input("Artist name:  ")
    song_title = input("Song name: ")
    html = get_html("https://genius.com/" + construct_song_URL(artist, song_title))

    soup = bs(html.text, 'html.parser')

    song_body = soup.find(class_="lyrics")
    lyrics = song_body.find('p')

    lyrics = re.sub("<(?:a\b[^>]*>|/a>)", "", lyrics.text)

    print(lyrics)
    


# Function to get HTML 
def get_html(URL):
    r = requests.get(URL)
    return r

def construct_song_URL(artist, song_title):

    #Replacing punctuation
    for c in string.punctuation:
        song_title = song_title.replace(c, "")

    artist_URL = ""
    song_URL = ""


    artist = artist.lower().capitalize()
    song_title = song_title.lower()    
    artist_list = artist.split(" ")


    song_title_list = song_title.split(" ")

    for i in artist_list:
        artist_URL += i + "-"

    for j in range(0, len(song_title_list)):
        song_URL += song_title_list[j] + "-"
    return(artist_URL + song_URL + "lyrics")


if __name__ == "__main__":
    main()
