import json
from app.sys_logger import logger


# The presentation log
def presentation():
    print("------------------------------------------------------")
    print("--------------- Ogram-Bot Started v0.1 ---------------")
    print("------------------------------------------------------")
    print("                                     By Sanix darker  ")
    print("------------------------------------------------------")


# To print a log and save it in logs.log
def printLog(command, telegram_user):
    tolog = command + " by: first_name: {}, last_name: {}, username: {}, language_code: {}, is_bot: {}".format(
        str(telegram_user.first_name), str(telegram_user.last_name), str(telegram_user.username),
        str(telegram_user.language_code), str(telegram_user.is_bot))
    logger.info(tolog)
    print("------------------------------------------------------")
    print(tolog)


# To rejects other bots that wanted to querry JeveuBot
def reject_bots(bot, update):
    if update.message.from_user.is_bot:
        logger.info("OUPS BOT, not authorized here!")
        bot.send_message(chat_id=update.message.chat_id,
                         text="NOT AUTHORIZED")
        return False
    return True


# Lang management
def get_lang_string_by_code(lang_code, code):
    if lang_code is None or lang_code not in ["en", "fr"]:
        lang_code = "en"
    with open('lang/' + lang_code + '.json', 'r+', encoding='utf-8') as f:
        lang_string = json.load(f)
        return lang_string[code]

# Get name from user object
def get_name(from_user):
    name = ""
    if from_user.first_name == None or from_user.last_name == None :
        if from_user.first_name != None:
            name += str(from_user.first_name)
        if from_user.last_name != None:
            name += str(from_user.last_name)
    else:
        name = str(from_user.first_name) + " " + str(from_user.last_name)

    return name