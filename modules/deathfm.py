import requests
from lxml import html
from cssselect import *
from bs4 import BeautifulSoup
from urllib.request import *

def currentsong () :
    death_url = 'http://death.fm/playing.php'
    death_page = requests.get(death_url)
    parsed_page = html.fromstring(death_page.text)
    info_block = parsed_page.xpath('/html/body/table/tbody/tr[2]/td')

    html_doc = urlopen('http://death.fm/playing.php').read()
    soup = BeautifulSoup(html_doc, "lxml")
    a = soup.find('td', 'td01')
    temp = a.find_all('a')
    artist = temp[0].text
    album = temp[1].text
    song_f = a.contents[5]
    song_str = str(song_f)
    song = song_str[5:-1]



    return artist, album,song

def last10songs () :
    queue_url = 'http://death.fm/modules/Queue_Played/Queue_Played-gen.php'
    queue_doc = urlopen(queue_url)
    queue_mark = BeautifulSoup(queue_doc,"lxml")
    b = queue_mark.find_all('table','table01')
    b_tr = b[1].contents
    b_tr_red = b_tr [3::2]
    text_list = ['song+artist+album']
    last_list = []
    for temp in b_tr_red :
          text_list.append(temp.text)
    text_list_reduced = text_list[2:]
    for temp in text_list_reduced :

        rest = str(temp).split('\n\n\t')
        time =  rest[1].split('\t\n\n\n\n\n\n\n\xa0')
        tt = str(time[1]).split('\n\n',2)
        artist_ = tt[0]
        album_ = tt[1]
        song_tt = str(temp).split('\n\n\t\t',2)
        song_ttt = song_tt[1:]
        song_ = str(song_ttt).split('\\t\\t\\t',1)
        song__ = song_[0]
        song = song__[6:]
        last_list.append(artist_ + '+'+ album_ + '+'+ song)


    return  last_list
if __name__ == "__main__":
    current_song = currentsong()
    last_songs = last10songs()
    print(current_song)
    print('\n')
    for asdf in last_songs:
        aaa=str(asdf).split('+')
        print("artist:  {0} , album:  {1} , song: {2}".format(aaa[0],aaa[1],aaa[2]) )
        print('\n')

last10songs ()
currentsong ()
intt = 1