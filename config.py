import telebot
from flask import Flask, request
import os 



# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )


TOKEN = "1920624938:AAEAsqDHsKqz0-QyIsb0qu5une0mvLVCLQw"
ADMIN =  1190069449 


SERVER_URL = os.getenv("https://fast-meadow-58903.herokuapp.com")


bot = telebot.TeleBot(token=TOKEN)
server = Flask(__name__)