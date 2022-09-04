from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper
from python_framework import Listener, ListenerMethod

from constant import TelegramConstant
from enumeration.BotShiftComands import BotShiftComands


@Listener(manager=TelegramConstant.BOT_MANAGER, muteLogs=False)
class BotShiftListener:

    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotShiftComands.WORK_SHIFT
        ]
    )
    def presentCommands(self, message):
        self.service.telegramShift.presentCommands(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotShiftComands.HIT_SHIFT
        ]
    )
    def hitShiftCommands(self, message):
        self.service.telegramShift.hitShiftCommands(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotShiftComands.HIT_FIRST_SHIFT_BEGIN,
            BotShiftComands.HIT_FIRST_SHIFT_END,
            BotShiftComands.HIT_SECOND_SHIFT_BEGIN,
            BotShiftComands.HIT_SECOND_SHIFT_END,
            BotShiftComands.HIT_SHIFT_NOW
        ]
    )
    def hitShift(self, message):
        self.service.telegramShift.hitShift(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotShiftComands.HIT_SHIFT_NOW
        ]
    )
    def hitShiftNow(self, message):
        self.service.telegramShift.hitShiftNow(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotShiftComands.GET_TODAY_SHIFT
        ]
    )
    def getTodaysShift(self, message):
        self.service.telegramShift.getTodaysShift(message)
