from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot.settings import BOT_TOKEN


def start(update, context):
    user = update.effective_user
    update.message.reply_text(f'Hello {user.first_name}!')


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
