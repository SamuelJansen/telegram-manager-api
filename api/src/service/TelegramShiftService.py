from python_helper import Constant as c
from python_helper import RandomHelper, log, ReflectionHelper, StringHelper, ObjectHelper
from python_framework import Service, ServiceMethod, EnumItem

from enumeration.BotShiftComands import BotShiftComands
from config import BotConfig


@Service()
class TelegramShiftService:

    @ServiceMethod()
    def presentCommands(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.bot.optionsByChatId(str(message.chat.id), 'Work shift options:', [
                f'{c.SLASH}{command}' for command in [
                    BotShiftComands.HIT_SHIFT,
                    BotShiftComands.GET_TODAYS_SHIFT
                ]
            ])
        else:
            log.warning(self.presentCommands, f'The {message.chat.id} chat id is trying to interact with work shift. But this method only responds to {BotConfig.CHAT_ID}')


    @ServiceMethod()
    def getTodaysShift(self, message):
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
    def hitShiftCommands(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.bot.optionsByChatId(str(message.chat.id), 'What momment?', [
                f'{c.SLASH}{command}' for command in [
                    BotShiftComands.HIT_FIRST_SHIFT_BEGIN,
                    BotShiftComands.HIT_FIRST_SHIFT_END,
                    BotShiftComands.HIT_SECOND_SHIFT_BEGIN,
                    BotShiftComands.HIT_SECOND_SHIFT_END,
                    BotShiftComands.HIT_SHIFT_NOW
                ]
            ])
        else:
            log.warning(self.hitShiftCommands, f'The {message.chat.id} chat id is trying to hit shift. But this method only responds to {BotConfig.CHAT_ID}')


    @ServiceMethod()
    def hitShiftNow(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.shift.hitShiftNow()
        else:
            log.warning(self.hitShiftNow, f'The {message.chat.id} chat id is trying to hit shift now. But this method only responds to {BotConfig.CHAT_ID}')


    @ServiceMethod()
    def hitShift(self, message):
        if BotConfig.CHAT_ID == message.chat.id:
            self.emitter.shift.hitShift({'momment': self.service.telegram.mapToEnum(BotShiftComands, message.text).momment})
        else:
            log.warning(self.hitShift, f'The {message.chat.id} chat id is trying to hit shift. But this method only responds to {BotConfig.CHAT_ID}')
