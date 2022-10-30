import logging

from telegram import Update, ForceReply, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler
from web3 import Web3, HTTPProvider

logger = logging.getLogger("alexandre")


def balance(update: Update, context: CallbackContext) -> None:
    """
    This function handles /whisper command
    """
    #context.bot.send_message(update.message.chat_id, "hello my friend")
    connection = Web3(HTTPProvider('https://mainnet.infura.io/v3/f2b9751eb1fe4a4f968f02653842d1b8'))
    context.bot.send_message(update.message.chat_id, str(connection.eth.get_balance('0xce8A9a40bd846dC8f27DDA35dC8630f461FA0b1a')))

def main() -> None:
    updater = Updater("5749456353:AAFWSIRg1841kHtyUzzwBpuafmJJrxnrfV8")

    # Get the dispatcher to register handlers
    # Then, we register each handler and the conditions the update must meet to trigger it
    dispatcher = updater.dispatcher

    # Register commands
    dispatcher.add_handler(CommandHandler("balance", balance))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
