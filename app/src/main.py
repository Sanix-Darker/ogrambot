# Main script of the Bot

from app.src.commands import *
from app.settings import *
from app.src.utils import presentation

# Starting with the presentation
presentation()

# Checker for new messages from Telegram API -> polling
updater = Updater(token=TOKEN)
# , use_context=True not working for this version, will check it later
# Allow us to register handlers -> command, text, video, audio, etc
dispatcher = updater.dispatcher

# Add a command handler for dispatcher
dispatcher.add_handler(start_handler)

# Add a command handler for dispatcher
dispatcher.add_handler(help_handler)

# log all errors
dispatcher.add_error_handler(error)


def main():
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
