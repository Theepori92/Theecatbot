from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = "16627307"
    API_HASH = "a853466115e4ccd120bdf39f98e780f8"
    # the name to display in your alive message
    ALIVE_NAME = "ཫƬꃅͥεͣεͫᎮ๏ᏒᏆཀ"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "Your value"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "Your value"
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "5337555859:AAHGbL2Khcy0l8tDqIWOg05Gp9MRcPE3L64"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "False"
