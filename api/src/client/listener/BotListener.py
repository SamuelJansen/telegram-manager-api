from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper
from python_framework import Listener, ListenerMethod
from enumeration.BotComands import BotComands


@Listener(manager='telegramManager', muteLogs=False)
class BotListener :

    @ListenerMethod(
        interceptor = 'telegramManager.bot.message_handler',
        commands = ['hi']
    )
    def hi(self, message):
        print(message.chat.id)
        self.manager.bot.reply_to(message, 'Hi')


    @ListenerMethod(
        interceptor = 'telegramManager.bot.message_handler',
        commands = [BotComands.POST_SHIFT]
    )
    def updateChampionshipTables(self, message):
        self.service.telegram.postShift(message)


    @ListenerMethod(
        interceptor = 'telegramManager.bot.message_handler',
        commands = [
            BotComands.GET_SHIFT
        ]
    )
    def updateChampionshipTable(self, message):
        self.service.telegram.getShift(message)
