from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper
from python_framework import Listener, ListenerMethod

from constant import TelegramConstant
from enumeration.BotComands import BotComands


@Listener(manager=TelegramConstant.BOT_MANAGER, muteLogs=False)
class BotListener :

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
            BotComands.HIT_SHIFT,
            BotComands.HIT_FIRST_SHIFT_BEGIN,
            BotComands.HIT_FIRST_SHIFT_END,
            BotComands.HIT_SECOND_SHIFT_BEGIN,
            BotComands.HIT_SECOND_SHIFT_END
        ]
    )
    def hitShift(self, message):
        self.service.telegram.hitShift(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotComands.GET_SHIFT
        ]
    )
    def getShift(self, message):
        self.service.telegram.getShift(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotComands.UPDATE_COMMANDS
        ]
    )
    def updateCommands(self, message):
        self.service.telegram.updateCommands(message)
