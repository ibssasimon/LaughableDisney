from bs4 import BeautifulSoup

with open("https://genius.com/Kendrick-lamar-bitch-dont-kill-my-vibe-lyrics") as fp:
    soup = BeautifulSoup(fp)

soup = BeautifulSoup("<html>data</html>")