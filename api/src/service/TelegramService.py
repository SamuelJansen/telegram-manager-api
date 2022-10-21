from python_helper import Constant as c
from python_helper import RandomHelper, log, ReflectionHelper, StringHelper, ObjectHelper
from python_framework import Service, ServiceMethod, EnumItem, Enum

from enumeration.BotComands import BotComands
from enumeration.BotShiftComands import BotShiftComands
from enumeration.BotTheNewsComands import BotTheNewsComands

from config import BotConfig


@Service()
class TelegramService:

    @ServiceMethod()
    def listCommands(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.bot.optionsByChatId(str(BotConfig.CHAT_ID), 'Tap a command to call it', [
                f'{c.SLASH}{command}'
                for command in [
                    *ReflectionHelper.getAttributeDataDictionary(BotShiftComands).values(),
                    *ReflectionHelper.getAttributeDataDictionary(BotTheNewsComands).values(),
                    *ReflectionHelper.getAttributeDataDictionary(BotComands).values()
                ]
                if isinstance(command, str)
            ])


    @ServiceMethod()
    def updateCommands(self, message):
        self.emitter.bot.aknowledgeByMessage(message)
        self.emitter.bot.updateCommands([
            BotShiftComands.SHIFT,
            BotTheNewsComands.THE_NEWS,
            BotComands.LIST_COMMANDS
        ])


    @ServiceMethod()
    def acceptMessages(self, dtoList):
        # self.emitter.bot.aknowledgeByChatId(str(BotConfig.CHAT_ID))
        for dto in dtoList:
            self.emitter.bot.sendTextByChatId(str(BotConfig.CHAT_ID), dto.get('message'))


    @ServiceMethod(requestClass=[Enum, str])
    def mapToEnum(self, enum, slashCommand):
        return enum.map(slashCommand.replace(c.SLASH, c.BLANK))
