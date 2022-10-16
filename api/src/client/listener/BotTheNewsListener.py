from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper
from python_framework import Listener, ListenerMethod

from constant import TelegramConstant
from enumeration.BotTheNewsComands import BotTheNewsComands


@Listener(manager=TelegramConstant.BOT_MANAGER, muteLogs=False)
class BotTheNewsListener:

    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotTheNewsComands.THE_NEWS
        ]
    )
    def presentCommands(self, message):
        return self.service.telegramTheNews.presentCommands(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotTheNewsComands.CREATE_TODAY_NEWS
        ]
    )
    def createTodayNews(self, message):
        return self.service.telegramTheNews.createTodayNews(message)
