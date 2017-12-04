#-*- coding: utf-8 -*-
import config
import telebot
import requests
import auth
from time import sleep
from bittrex import Bittrex
from requests.exceptions import ConnectionError
from time import sleep
from subprocess import Popen, PIPE

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




@bot.message_handler(commands=['status'])
def handle_status(message):
    data = 'iperf -c 192.168.62.65 -p 3389 -t1'
    stdout = Popen(data, shell=True, stdout=PIPE).stdout
    if stdout.read() != '':
        bot.send_message(message.chat.id, "Катка в порядке")
    else:
        bot.send_message(message.chat.id, "Какая-то хуета с каткой")


@bot.message_handler(commands=['periodic_check'])
def handle_periodic_check(message):
    bot.send_message(message.chat.id, "Ага, запустил")
    data = 'iperf -c 192.168.62.65 -p 3389 -t1'
    count = 0
    while True:
        stdout = Popen(data, shell=True, stdout=PIPE).stdout
        if stdout.read() == '':
            bot.send_message(message.chat.id, "Катка подохла")
            count+=1
        sleep(300)
        if count > 5:
            bot.send_message(message.chat.id, "Стоп проверка, катка подохла.")
            break
            



@bot.message_handler(content_types=["text"])
def handle_other(message):
	bot.send_message(message.chat.id, "А, понял")




if __name__ == '__main__':
     bot.polling(none_stop=True)






