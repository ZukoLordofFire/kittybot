# send_random_image.py

import requests  # Импортируем библиотеку для работы с запросами

from telegram import Bot

bot = Bot(token='5649919241:AAFUNQL1SPKd7mFh82IyFFk7HEGTj1FfR5k')
URL = 'https://api.thecatapi.com/v1/images/search'
chat_id = 247789172

# Делаем GET-запрос к эндпоинту:
response = requests.get(URL).json()
# Извлекаем из ответа URL картинки:
random_cat_url = response[0].get('url')  

# Передаём chat_id и URL картинки в метод для отправки фото:
bot.send_photo(chat_id, random_cat_url) 