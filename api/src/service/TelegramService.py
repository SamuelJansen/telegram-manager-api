from python_helper import Constant as c
from python_helper import RandomHelper, log, ReflectionHelper
from python_framework import Service, ServiceMethod, EnumItem, EnumItemStr

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
        else:
            log.info(self.hitShift, f'The {message.chat.id} chat id is trying to hit shift. But this method only responds to {BotConfig.CHAT_ID}')


    @ServiceMethod()
    def hitShift(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            if BotComands.HIT_SHIFT == self.mapToEnum(message.text):
                self.emitter.bot.optionsByChatId(str(BotConfig.CHAT_ID), 'What momment?', [
                    f'{c.SLASH}{command}' for command in [
                        BotComands.HIT_FIRST_SHIFT_BEGIN,
                        BotComands.HIT_FIRST_SHIFT_END,
                        BotComands.HIT_SECOND_SHIFT_BEGIN,
                        BotComands.HIT_SECOND_SHIFT_END
                    ]
                ])
            else:
                self.emitter.shift.hitShift({'momment': self.mapToEnum(message.text).momment})
        else:
            log.info(self.hitShift, f'The {message.chat.id} chat id is trying to hit shift. But this method only responds to {BotConfig.CHAT_ID}')


    @ServiceMethod()
    def acceptMessages(self, dtoList):
        for dto in dtoList:
            self.emitter.bot.optionsByChatId(str(BotConfig.CHAT_ID), dto.get('message'), ['Ok'])


    @ServiceMethod()
    def updateCommands(self, message):
        self.emitter.bot.updateCommands(message)


    @ServiceMethod(requestClass=[str])
    def mapToEnum(self, slashCommand):
        return BotComands.map(slashCommand.replace(c.SLASH, c.BLANK))
