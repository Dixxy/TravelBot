from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

from bot.keyboards import get_menu, get_categories
from bot.settings import BOT_TOKEN


def start(update, context):
    user = update.effective_user
    update.message.reply_text(f'Hello {user.first_name}!', reply_markup=get_menu())


def categories(update, context):
    query = update.callback_query

    query.edit_message_text(text='Categories', reply_markup=get_categories())


def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(categories, pattern='^categories$'))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

