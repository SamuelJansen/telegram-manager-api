import telebot as tb
from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper
from python_framework import Listener, ListenerMethod
from enumeration.TelegramComands import TelegramComands


@Listener(manager='telegramManager', muteLogs=False)
class TelegramListener :

    @ListenerMethod(
        interceptor = 'telegramManager.bot.message_handler',
        commands = ['oi']
    )
    def hi(self, message):
        self.manager.bot.reply_to(message, 'Oi')


    @ListenerMethod(
        interceptor = 'telegramManager.bot.message_handler',
        commands = [TelegramComands.UPDATE_CHAMPIONSHIP_TABLES]
    )
    def updateChampionshipTables(self, message):
        self.service.telegram.updateChampionshipTables(message)


    @ListenerMethod(
        interceptor = 'telegramManager.bot.message_handler',
        commands = [
            TelegramComands.UPDATE_CHAMPIONSHIP_TABLE,
            'campeonato_catarinense',
            'campeonato_mineiro',
            'campeonato_paranaense',
            'campeonato_gaucho',
            'paulista_serie_a3'
        ]
    )
    def updateChampionshipTable(self, message):
        self.service.telegram.updateChampionshipTable(message)
