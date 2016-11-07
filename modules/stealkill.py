from bs4 import BeautifulSoup
from urllib.request import *

def currentsong () :
    html_doc = urlopen('http://listen.42fm.ru/').read()
    soup = BeautifulSoup(html_doc, "lxml")
    a = soup.find_all('td', 'streamstats')
    song_f = a[6].contents
    b = song_f.split('-')
    artist = b[0]
    song = b[1]
    return artist,song
