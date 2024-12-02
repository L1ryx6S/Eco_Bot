import telebot
import random
import os
import requests
from bot_logic import flip_coin, gen_emodji, gen_pass, get_duck_image_url

bot = telebot.TeleBot("8124306218:AAGG_yXPizbRpd2O2ifJSqi3dIgjnr-tJzs")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши команду /hello, /bye, /pass, /emodji, /coin, /mem, /duck, /consequences, /nature")

@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['pass'])
def send_password(message):
    password = gen_pass(10)  # Устанавливаем длину пароля, например, 10 символов
    bot.reply_to(message, f"Вот твой сгенерированный пароль: {password}")

@bot.message_handler(commands=['emodji'])
def send_emodji(message):
    emodji = gen_emodji()
    bot.reply_to(message, f"Вот эмоджи': {emodji}")

@bot.message_handler(commands=['coin'])
def send_coin(message):
    coin = flip_coin()
    bot.reply_to(message, f"Монетка выпала так: {coin}")

@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['duck'])
def duck(message):
        '''По команде duck вызывает функцию get_duck_image_url и отправляет URL изображения утки'''
        image_url = get_duck_image_url()
        bot.reply_to(message, image_url)

@bot.message_handler(commands=['consequences'])
def send_mem(message):
    eco = os.listdir('eco')
    eco_name = random.choice(eco)
    with open(f'eco/{eco_name}', 'rb') as f:  
        bot.send_photo(message.chat.id, f)  

@bot.message_handler(commands=['nature'])
def send_hello(message):
    bot.reply_to(message, "Дорогой пользователь, дам тебе пару советов как защитить природу и окружающих. 1-Всегда сортируй мусор. Это поможет рабочим сортировать мусор и разделять отходы для переработки. 2-Заменять пластиковую посуду на керамическую или металлическую.Недавно ученые выяснили, что после приема пищи из пластиковых тарелок в организм попадает микропластик. Позже он попадет в сосуды и может накапливаться в них, что представляет большую угрозу для человека. 3-Становится волонтером. В нашей стране множество молодых ребят уже вступили в ряды волонтеров. Они помогают природе, животным и людям попавшим в беду.Волонтерство - важная и востребованная профессия особенно в нынешнее время. ")

bot.polling()




