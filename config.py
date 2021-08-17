import telebot
from telebot import TeleBot
from flask import Flask, request
import os 
from __constants__.const import *


# Logging Setup
import logging
logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING
    )


TOKEN = api

ADMIN =  1190069449 



DEBUG = True


SERVER_URL = os.getenv("https://fast-meadow-58903.herokuapp.com")


bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)