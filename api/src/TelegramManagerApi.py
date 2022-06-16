from python_framework import ResourceManager
from queue_manager_api import QueueManager

import ModelAssociation

import threading
import telebot as tb
import logging
from python_helper import log, ReflectionHelper


class TelegramManager:

    bot = None
    botThread = None

    def __init__(self):
        log.debug(self.__init__, f'{ReflectionHelper.getName(TelegramManager)} created')


    def addResource(self, api, app):
        # import globals
        # globals.getGlobalsInstance().getSettign(BotConfig.BOT_TOKEN)
        api.resource.manager.telegram = self
        self.api = api
        self.module = tb
        from config import BotConfig
        self.bot = tb.TeleBot(BotConfig.BOT_TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
        self.botThread = threading.Thread(target = self.bot.infinity_polling)
        self.botThread.daemon = True
        self.module.logger.setLevel(logging.DEBUG) ###- logging.CRITICAL
        log.status(self.addResource, 'Telegram manager resource added successfuly')


    def onHttpRequestCompletion(self, api, app):
        ...


    def onRun(self, api, app):
        # api.resource.manager.telegram.botThread.start()
        ...


    def initialize(self, api, app):
        api.resource.manager.telegram.botThread.start()
        log.success(self.initialize, f'{ReflectionHelper.getClassName(self)} is running')


    def onShutdown(self, api, app):
        api.resource.manager.telegram.botThread.join(timeout=0)
        log.success(self.onShutdown, f'{ReflectionHelper.getClassName(self)} is successfuly closed')


app = ResourceManager.initialize(__name__, ModelAssociation.MODEL, managerList=[
    TelegramManager(),
    QueueManager()
])
