from python_helper import Constant as c
from python_helper import RandomHelper, log, ReflectionHelper, StringHelper, ObjectHelper
from python_framework import Service, ServiceMethod, EnumItem, EnumItemStr

from enumeration.BotComands import BotComands
from config import BotConfig


@Service()
class TelegramService:

    @ServiceMethod()
    def getShift(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            text = StringHelper.join(
                [
                    responseDto.get('hitAt')
                    for responseDto in self.client.shift.getTodayShift()
                ],
                character = f'{c.COMA}{c.NEW_LINE}'
            )
            self.emitter.bot.successByMessage(
                message,
                text = text if ObjectHelper.isNeitherNoneNorBlank(text) else '''Shift still not hit today'''
            )

        else:
            log.warning(self.hitShift, f'The {message.chat.id} chat id is trying to hit shift. But this method only responds to {BotConfig.CHAT_ID}')


    @ServiceMethod()
    def hitShift(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            if BotComands.HIT_SHIFT == self.mapToEnum(message.text):
                self.emitter.bot.optionsByChatId(str(BotConfig.CHAT_ID), 'What momment?', [
                    f'{c.SLASH}{command}' for command in [
                        BotComands.HIT_FIRST_SHIFT_BEGIN,
                        BotComands.HIT_FIRST_SHIFT_END,
                        BotComands.HIT_SECOND_SHIFT_BEGIN,
                        BotComands.HIT_SECOND_SHIFT_END,
                        BotComands.HIT_SHIFT_NOW
                    ]
                ])
            else:
                self.emitter.bot.aknowledgeByMessage(message)
                if BotComands.HIT_SHIFT_NOW == self.mapToEnum(message.text):
                    self.emitter.shift.hitShiftNow()
                else:
                    self.emitter.shift.hitShift({'momment': self.mapToEnum(message.text).momment})
        else:
            log.warning(self.hitShift, f'The {message.chat.id} chat id is trying to hit shift. But this method only responds to {BotConfig.CHAT_ID}')

    @ServiceMethod()
    def createTodayNews(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.bot.aknowledgeByMessage(message)
            self.client.theNews.createTodayNews()
        else:
            log.warning(self.hitShift, f'The {message.chat.id} chat id is trying to interact with the-news. But this method only responds to {BotConfig.CHAT_ID}')


    @ServiceMethod()
    def acceptMessages(self, dtoList):
        # self.emitter.bot.aknowledgeByChatId(str(BotConfig.CHAT_ID))
        for dto in dtoList:
            self.emitter.bot.sendTextByChatId(str(BotConfig.CHAT_ID), dto.get('message'))


    @ServiceMethod()
    def listCommands(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.bot.optionsByChatId(str(BotConfig.CHAT_ID), 'Tap a command to call it', [
                f'{c.SLASH}{command}'
                for command in [
                    *ReflectionHelper.getAttributeDataDictionary(BotComands).values()
                ]
                if isinstance(command, str)
            ])


    @ServiceMethod()
    def updateCommands(self, message):
        self.emitter.bot.aknowledgeByMessage(message)
        self.emitter.bot.updateCommands([
            BotComands.GET_SHIFT,
            BotComands.HIT_SHIFT,
            BotComands.LIST_COMMANDS
        ])


    @ServiceMethod(requestClass=[str])
    def mapToEnum(self, slashCommand):
        return BotComands.map(slashCommand.replace(c.SLASH, c.BLANK))
