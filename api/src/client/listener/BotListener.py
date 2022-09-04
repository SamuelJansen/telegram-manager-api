from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper
from python_framework import Listener, ListenerMethod

from constant import TelegramConstant
from enumeration.BotComands import BotComands


@Listener(manager=TelegramConstant.BOT_MANAGER, muteLogs=False)
class BotListener:

    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = ['hi']
    )
    def hi(self, message):
        print(message.chat.id)
        self.manager.bot.reply_to(message, 'Hi')


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotComands.LIST_COMMANDS
        ]
    )
    def listCommands(self, message):
        self.service.telegram.listCommands(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotComands.UPDATE_COMMANDS
        ]
    )
    def updateCommands(self, message):
        self.service.telegram.updateCommands(message)
