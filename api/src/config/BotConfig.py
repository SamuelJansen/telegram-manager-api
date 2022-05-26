from python_helper import log
from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


BOT_TOKEN = globalsInstance.getSetting('telegram.bot-token')
CHAT_ID = globalsInstance.getSetting('telegram.chat-id')
