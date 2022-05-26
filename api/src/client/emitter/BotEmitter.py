from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper, RandomHelper
from python_framework import Emitter, EmitterMethod

from constant import TelegramConstant
from enumeration.BotComands import BotComands


AKNOWLEDGE = [
    'On it',
    'Ok'
]

LONG_AKNOWLEDGE = [
    '''It's going to take a while'''
]

COMPLETE = [
    '''It's done'''
]


@Emitter(manager=TelegramConstant.BOT_MANAGER, muteLogs=False)
class BotEmitter :

    @EmitterMethod()
    def updateCommands(self, message):
        self.manager.bot.delete_my_commands(scope=None, language_code=None)
        self.manager.bot.set_my_commands(
            commands=[
                self.manager.module.types.BotCommand(command, command.description) for command in [
                    *ReflectionHelper.getAttributeDataDictionary(BotComands).values()
                ] if not ReflectionHelper.isNotFunction(command)
            ],
            # scope=telebot.types.BotCommandScopeChat(12345678)  # use for personal command for users
            # scope=telebot.types.BotCommandScopeAllPrivateChats()  # use for all private chats
        )


    @EmitterMethod()
    def aknowledgeByMessage(self, message, long=False):
        self.manager.bot.reply_to(message, RandomHelper.sample(LONG_AKNOWLEDGE if long else AKNOWLEDGE))


    @EmitterMethod()
    def successByMessage(self, message, text):
        self.manager.bot.reply_to(message, f'{RandomHelper.sample(COMPLETE)}{f"{2*c.NEW_LINE}{text}" if ObjectHelper.isNotEmpty(text) else c.BLANK}')


    @EmitterMethod()
    def sendTextMessage(self, message, text):
        self.manager.bot.reply_to(message, f'{RandomHelper.sample(COMPLETE)}{f"{2*c.NEW_LINE}{text}" if ObjectHelper.isNotEmpty(text) else c.BLANK}')


    @EmitterMethod()
    def optionsByChatId(self, chatId, text, optionList, placeholder=c.BLANK):
        markup = self.manager.module.types.ReplyKeyboardMarkup(
            one_time_keyboard = True,
            selective = True,
            input_field_placeholder = placeholder
        )
        for option in optionList:
            markup.add(option)
        # a = self.manager.module.types.KeyboardButton('gauchão')
        # b = self.manager.module.types.KeyboardButton('catarinense')
        # c = self.manager.module.types.KeyboardButton('paulista série A3')
        # d = self.manager.module.types.KeyboardButton('paranaense')
        # e = self.manager.module.types.KeyboardButton('mineiro')
        # markup.row(a, b)
        # markup.row(c, d, e)
        self.manager.bot.send_message(chatId, text, reply_markup=markup)
