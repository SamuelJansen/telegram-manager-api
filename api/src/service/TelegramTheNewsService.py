from python_helper import Constant as c
from python_helper import RandomHelper, log, ReflectionHelper, StringHelper, ObjectHelper
from python_framework import Service, ServiceMethod

from enumeration.BotTheNewsComands import BotTheNewsComands
from config import BotConfig


@Service()
class TelegramTheNewsService:

    @ServiceMethod()
    def presentCommands(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.bot.optionsByChatId(str(message.chat.id), 'The news commands', [
                f'{c.SLASH}{command}' for command in [
                    BotTheNewsComands.CREATE_TODAY_NEWS
                ]
            ])
        else:
            log.warning(self.presentCommands, f'The {message.chat.id} chat id is trying to list the news commands. But this method only responds to {BotConfig.CHAT_ID}')


    @ServiceMethod()
    def createTodayNews(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.bot.aknowledgeByMessage(message)
            self.client.theNews.createTodayNews()
        else:
            log.warning(self.createTodayNews, f'The {message.chat.id} chat id is trying to interact with the-news. But this method only responds to {BotConfig.CHAT_ID}')
