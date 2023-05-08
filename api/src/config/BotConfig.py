from python_helper import log, SettingHelperHelper
from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


BOT_TOKEN = globalsInstance.getSetting('telegram.bot-token')
CHAT_ID = globalsInstance.getSetting('telegram.chat-id.main')
TRUSTED_CHAT_ID_LIST = SettingHelperHelper.getValue(globalsInstance.getSetting('telegram.chat-id.trusted-list'))
