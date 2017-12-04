#-*- coding: utf-8 -*-
import config
import telebot
from lxml import html
import requests
from time import sleep
from bittrex import Bittrex
import auth
bot = telebot.TeleBot(config.token)
url = 'https://coinmarketcap.com/'
zcash = ".//*[@id='id-zcash']/td[4]/a"
btc = ".//*[@id='id-bitcoin']/td[4]/a"


def coin_price(coin):
	
	result = requests.get(url)
	tree = html.fromstring(result.text)
	value = tree.xpath(coin)
	for i in value:
		coin_val = int(i.text.split('.')[0].split('$')[1])
	
	return coin_val
		





@bot.message_handler(commands=['start'])
def handle_start_help(message):
    bot.send_message(message.chat.id, 'Ага')
	



@bot.message_handler(commands=['zcash'])
def handle_zchash(message):
    bot.send_message(message.chat.id, coin_price(zcash))




@bot.message_handler(commands=['bitcoin'])
def handle_btc(message):
    bot.send_message(message.chat.id, coin_price(btc))

@bot.message_handler(commands=['bittrex'])
def handle_bittrex_balance(message):
    my_b = Bittrex(auth.api_key, auth.api_secret)
    balance = my_b.get_balance('ZEC')
    zec_value = balance['result']['Available']
    bot.send_message(message.chat.id, zec_value)
    

@bot.message_handler(commands=['test'])
def test(message):
    for i in range(1, 4):
        bot.send_message(message.chat.id, i)
        sleep(30)

@bot.message_handler(content_types=["text"])
def handle_other(message):
	bot.send_message(message.chat.id, "А, понял")








# @bot.message_handler(content_types=["text"])
# def repeat_all_messages(message):
	
# 	if message.text == "z":
# 		bot.send_message(message.chat.id, coin_price(zcash))

	
# 	elif message.text == "btc":
# 		bot.send_message(message.chat.id, coin_price(btc))
	
# 	elif message.text == "card":
# 		try:
# 			r = requests.get(url1)
# 			data  = r.json()
# 			dict0 =  data['result'][0]
# 			dict1 =  data['result'][1]
# 			dict2 =  data['result'][2]
#                         dict3 =  data['result'][3]
# 			mes1 = "card0_speed: " + str(dict0['speed_sps']) + ' ' +  "card0_temp: " + str(dict0['temperature'])
# 			mes2 = "card1_speed: " + str(dict1['speed_sps']) + ' ' +  "card1_temp: " + str(dict1['temperature'])
# 			mes3 = "card2_speed: " + str(dict2['speed_sps']) + ' ' +  "card2_temp: " + str(dict2['temperature'])
#                         mes4 = "card3_speed: " + str(dict3['speed_sps']) + ' ' +  "card2_temp: " + str(dict3['temperature'])
# 			all_mes = mes1 + "\n" + mes2 + "\n" + mes3 +"\n" + mes4
# 			bot.send_message(message.chat.id, all_mes)
# 		except requests.exceptions.ConnectionError:
# 			bot.send_message(message.chat.id, "не отвечает эта хуета")
	
# 	elif message.text == "bittrex":
# 		my_b = Bittrex(auth.api_key, auth.api_secret)
# 		balance = my_b.get_balance('ZEC')
# 		zec_value = balance['result']['Available']
# 		bot.send_message(message.chat.id, zec_value)



# 	else:
# 		bot.send_message(message.chat.id, "пошел нахуй, не знаю такой команды")






if __name__ == '__main__':
     bot.polling(none_stop=True)






# my_b = Bittrex(auth.api_key, auth.api_secret)
# balance = my_b.get_balance('ZEC')
# zec_value = balance['result']['Available']

