from django.contrib.sites import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu():
    keyboard = [
        [
            InlineKeyboardButton('Tours', callback_data='1'),
        ],
        [
            InlineKeyboardButton('Search', callback_data='3')
        ],
    ]

    return InlineKeyboardMarkup(keyboard)


def get_categories():
    data = requests.get('http://localhost/categories/').json()
    keyboard = []

    for cat in data:
        keyboard.append(
            [

            ]
        )
