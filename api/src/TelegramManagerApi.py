from python_framework import ResourceManager
from queue_manager_api import QueueManager

import ModelAssociation

import threading
import telebot as tb
import logging


class TelegramManager:

    bot = None
    botThread = None

    def addResource(self, api, app):
        # import globals
        # globals.getGlobalsInstance().getSettign(BotConfig.BOT_TOKEN)
        api.telegramManager = self
        self.api = api
        self.module = tb
        from config import BotConfig
        self.bot = tb.TeleBot(BotConfig.BOT_TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
        self.botThread = threading.Thread(target = self.bot.infinity_polling)
        self.botThread.daemon = True
        self.module.logger.setLevel(logging.DEBUG) ###- logging.CRITICAL


    def onHttpRequestCompletion(self, api, app):
        ...


    def onRun(self, api, app):
        # api.telegramManager.botThread.start()
        ...


    def initialize(self, api, app):
        api.telegramManager.botThread.start()


    def onShutdown(self, api, app):
        api.telegramManager.botThread.join(timeout=0)


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL, managerList=[
    TelegramManager(),
    QueueManager()
])
