import telebot as tb
from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper, RandomHelper
from python_framework import Emitter, EmitterMethod
from enumeration.TelegramComands import TelegramComands



AKNOWLEDGE = [
    'Deixa pra mim',
    'Tá rolando',
    'Beleza, já tô fazendo',
    'Um minuto',
    'Ok, já faço isso',
    'Vou tentar pra ontem',
    'Bora'
]

LONG_AKNOWLEDGE = [
    'Na real esse é mais demoradinho',
    'É demorado... mas vai',
    'Vou tentar agilizar, mas é lento',
    'Mals aí mas esse vai demorar',
    'Uns 4 minutinhos e tá pronto'
]

OK = [
    'Feito',
    'Pronto',
    'Foi',
    'Prontinho',
    'É os guri, pai',
    'Deu bom',
    'Feito chefe'
]


@Emitter(manager='telegramManager', muteLogs=False)
class TelegramEmitter :

    @EmitterMethod()
    def updateCommands(self):
        self.manager.bot.delete_my_commands(scope=None, language_code=None)
        self.manager.bot.set_my_commands(
            commands=[
                tb.types.BotCommand(command, command.description) for command in [
                    *ReflectionHelper.getAttributeDataDictionary(TelegramComands).values()
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
        self.manager.bot.reply_to(message, f'{RandomHelper.sample(OK)}{f"{2*c.NEW_LINE}{text}" if ObjectHelper.isNotEmpty(text) else c.BLANK}')


    @EmitterMethod()
    def optionsByChatId(self, chatId, text, optionList, placeholder=c.BLANK):
        markup = tb.types.ReplyKeyboardMarkup(
            one_time_keyboard = True,
            selective = True,
            input_field_placeholder = placeholder
        )
        for team in optionList:
            markup.add(team)
        # a = tb.types.KeyboardButton('gauchão')
        # b = tb.types.KeyboardButton('catarinense')
        # c = tb.types.KeyboardButton('paulista série A3')
        # d = tb.types.KeyboardButton('paranaense')
        # e = tb.types.KeyboardButton('mineiro')
        # markup.row(a, b)
        # markup.row(c, d, e)
        self.manager.bot.send_message(chatId, text, reply_markup=markup)
