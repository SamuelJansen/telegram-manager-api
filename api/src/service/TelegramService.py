from python_helper import Constant as c
from python_helper import RandomHelper
from python_framework import Service, ServiceMethod


@Service()
class TelegramService:

    @ServiceMethod()
    def getShift(self, message):
        self.emitter.bot.aknowledgeByMessage(message, long=True)
        self.emitter.bot.successByMessage(
            message,
            text = 'Here it is'
        )


    @ServiceMethod()
    def postShift(self, message):
        self.emitter.bot.aknowledgeByMessage(message)
        self.emitter.bot.optionsByChatId(
            message.chat.id,
            'Choose one',
            ['A', 'B', 'C'],
            placeholder = 'Choose one'
        )
        self.emitter.bot.successByMessage(
            message,
            text = 'Well done'
        )


    @ServiceMethod()
    def acceptMessages(self, dtoList):
        for dto in dtoList:
            self.emitter.bot.optionsByChatId('1019762145', dto.get('message'), ['A', 'B', 'C'])


    @ServiceMethod()
    def uodateCommands(self, message):
        self.emitter.bot.updateCommands(message)
