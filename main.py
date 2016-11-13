import logging
from telegram.ext import *
import random
import modules.deathfm as df
import modules.stealkill as st
from telegram import *

updater = Updater(token='xxxx')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)



def start(bot, update):

    keyboard = [[KeyboardButton(text="/photo"),
                 KeyboardButton(text="/phrnd")],
                [KeyboardButton(text="/dfcurrent"),
                 KeyboardButton(text="/dflast"),
                 KeyboardButton(text="/stcurrent")]]

    reply_markup_start = ReplyKeyboardMarkup(keyboard,one_time_keyboard = True, resize_keyboard = True)
    bot.sendMessage(chat_id=update.message.chat_id, text="here are commands", reply_markup = reply_markup_start )
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


def hui(bot, update): bot.sendMessage(chat_id=update.message.chat_id, text="a vot hui tebe", reply_markup=ReplyKeyboardHide())
hui_handler = MessageHandler([Filters.text], hui)
dispatcher.add_handler(hui_handler)


photo_file_url = 'https://pp.vk.me/c626429/v626429662/18f3e/0BpsJlzcS2I.jpg'
def photo_new (bot,update) : bot.sendPhoto (chat_id=update.message.chat_id, photo=photo_file_url)

photo_handler = CommandHandler('photo', photo_new)
dispatcher.add_handler(photo_handler)

photo_list = ['https://pp.vk.me/c626429/v626429662/18f3e/0BpsJlzcS2I.jpg',
              'https://pp.vk.me/c604522/v604522476/2e8bc/3bGACEVfMM8.jpg',
              'https://pp.vk.me/c626828/v626828115/34cb/8ESzvcmg-_Y.jpg' ,
              'https://pp.vk.me/c630016/v630016115/29b2d/jCvgltPt96Q.jpg' ,
              'https://pp.vk.me/c636525/v636525115/11bce/Tr4oIFz7D8Q.jpg' ,
              'https://pp.vk.me/c636525/v636525115/11bd8/kMxeGuJ1Olg.jpg' ,
              'https://pp.vk.me/c631527/v631527115/30791/lccdpkDo7hc.jpg' ,
              'https://pp.vk.me/c631527/v631527115/307a3/RlTDmVFySnY.jpg']
def get_num_photo(bot,update) : bot.sendMessage(chat_id=update.message.chat_id, text= str(photo_list[2]), reply_markup=ReplyKeyboardHide() )
get_num_photo_handler = CommandHandler('phnum',get_num_photo)
dispatcher.add_handler(get_num_photo_handler)


def get_random_photo (bot,update) : bot.sendMessage(chat_id=update.message.chat_id, text= str(random.choice(photo_list)), reply_markup=ReplyKeyboardHide())
get_random_photo_handler = CommandHandler('phrnd',get_random_photo)
dispatcher.add_handler(get_random_photo_handler)


def get_current_song_df(bot,update) :
    song = df.currentsong()
    curr_song = "   artist:  {0} , album:  {1} , song: {2}".format(song[0], song[1], song[2])
    bot.sendMessage(chat_id=update.message.chat_id, text=curr_song, reply_markup=ReplyKeyboardHide())

get_current_song_df_handler = CommandHandler('dfcurrent',get_current_song_df)
dispatcher.add_handler(get_current_song_df_handler)

def get_last_songs_df(bot,update) :
    last_songs = df.last10songs()
    songs_list = ""
    i = 0
    for temp   in last_songs :
        tem = str(temp).split('+')
        i+=1
        aaaa = "   artist:  {0} , album:  {1} , song: {2}".format(tem[0], tem[1], tem[2])
        songs_list += str(i)
        songs_list += aaaa
        songs_list += '\n'
    bot.sendMessage(chat_id=update.message.chat_id, text=songs_list, reply_markup=ReplyKeyboardHide())

get_last_songs_df_handler = CommandHandler('dflast',get_last_songs_df)
dispatcher.add_handler(get_last_songs_df_handler)


def get_current_song_st(bot,update) :
    curr_song = st.currentsong()
    bot.sendMessage(chat_id=update.message.chat_id, text=curr_song, reply_markup=ReplyKeyboardHide())

get_curr_song_st_handler = CommandHandler('stcurrent',get_current_song_st)
dispatcher.add_handler(get_curr_song_st_handler)

updater.start_polling()
