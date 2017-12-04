#-*- coding: utf-8 -*-
import config
import telebot
import requests
import auth
from time import sleep
from bittrex import Bittrex
from requests.exceptions import ConnectionError
from time import sleep

bot = telebot.TeleBot(config.token)



def extract_arg(arg):
    try:
        return arg.split()[1]
    except IndexError:
        return "Не, ну а че?"
		





@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Ага')
	


@bot.message_handler(commands=['zcash'])
def handle_zchash(message):
    zcash = requests.get('https://api.coinmarketcap.com/v1/ticker/zcash/')
    output = zcash.json()[0]['price_usd'] + "$" + "       " + zcash.json()[0]['percent_change_24h'] + "%"
    bot.send_message(message.chat.id, output)



@bot.message_handler(commands=['bitcoin'])
def handle_btc(message):
    btc = requests.get('https://api.coinmarketcap.com/v1/ticker/bitcoin/')
    output = btc.json()[0]['price_usd'] + "$" + "       " + btc.json()[0]['percent_change_24h'] + "%"
    bot.send_message(message.chat.id, output)



@bot.message_handler(commands=['bittrex'])
def handle_bittrex_balance(message):
    my_b = Bittrex(auth.api_key, auth.api_secret)
    balance = my_b.get_balance('ZEC')
    zec_value = balance['result']['Available']
    bot.send_message(message.chat.id, zec_value)
    

@bot.message_handler(commands=['test'])
def test(message):
    arg=extract_arg(message.text)
    bot.send_message(message.chat.id, arg.upper())



@bot.message_handler(commands=['check'])
def check_katka(message):
    i = 0
    while True:
        try:
            r = requests.get('http://192.168.12.181:42000/getstat')
        
        except ConnectionError:
            bot.send_message(message.chat.id, "Катка подохла")

        i+=1
        sleep(5)

        if i > 5:
            break




@bot.message_handler(content_types=["text"])
def handle_other(message):
	bot.send_message(message.chat.id, "А, понял")




if __name__ == '__main__':
     bot.polling(none_stop=True)






