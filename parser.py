import requests
import string
from bs4 import BeautifulSoup as bs
import re
 
def main():

    # Get artist input from user
    artist = input("Artist name:  ")
    song_title = input("Song name: ")
    artist = artist.lower().capitalize()
    song_title = song_title.lower()

    # Format the artist / song
    formatted_artist = construct_song_URL(artist, song_title)

    # Get URL for Genius
    html = get_html("https://genius.com/" + formatted_artist)

    # Parse for lyrics using BeautifulSoap
    soup = bs(html.text, 'html.parser')
    song_body = soup.find(class_="lyrics")
    lyrics = song_body.find('p')
    lyrics = re.sub("<(?:a\b[^>]*>|/a>)", "", lyrics.text)


    with open(formatted_artist + ".txt", 'w') as f:
        f.write(lyrics)
    


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

    artist_list = artist.split(" ")


    song_title_list = song_title.split(" ")

    for i in artist_list:
        artist_URL += i + "-"

    for j in range(0, len(song_title_list)):
        song_URL += song_title_list[j] + "-"
    return(artist_URL + song_URL + "lyrics")


if __name__ == "__main__":
    main()
