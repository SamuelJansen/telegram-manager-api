from python_helper import Constant as c
from python_helper import RandomHelper
from python_framework import Service, ServiceMethod

from enumeration.BotComands import BotComands
from config import BotConfig


@Service()
class TelegramService:

    @ServiceMethod()
    def getShift(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.bot.aknowledgeByMessage(message, long=True)
            self.emitter.bot.successByMessage(
                message,
                text = 'Here it is'
            )


    @ServiceMethod()
    def hitShift(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            if BotComands.HIT_SHIFT == BotComands.map(message.text):
                self.emitter.bot.optionsByChatId(BotConfig.CHAT_ID, 'What momment?', [
                    self.manager.module.types.BotCommand(command, command.description) for command in [
                        *ReflectionHelper.getAttributeDataDictionary(BotComands).values()
                    ] if not ReflectionHelper.isNotFunction(command) and not BotComands.HIT_SHIFT == command
                ])
            else:
                self.emitter.shift.hitShift({'momment': BotComands.map(message.text).momment})


    @ServiceMethod()
    def acceptMessages(self, dtoList):
        for dto in dtoList:
            self.emitter.bot.optionsByChatId(BotConfig.CHAT_ID, dto.get('message'), ['Ok'])


    @ServiceMethod()
    def updateCommands(self, message):
        self.emitter.bot.updateCommands(message)
