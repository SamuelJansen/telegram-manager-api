from python_helper import Constant as c
from python_helper import ReflectionHelper, ObjectHelper, StringHelper
from python_framework import Listener, ListenerMethod

from constant import TelegramConstant
from enumeration.BotComands import BotComands


@Listener(manager=TelegramConstant.BOT_MANAGER, muteLogs=False)
class BotListener:

    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = ['hi']
    )
    def hi(self, message):
        print(message.chat.id)
        self.manager.bot.reply_to(message, 'Hi')


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotComands.LIST_COMMANDS
        ]
    )
    def listCommands(self, message):
        self.service.telegram.listCommands(message)


    @ListenerMethod(
        interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
        commands = [
            BotComands.UPDATE_COMMANDS
        ]
    )
    def updateCommands(self, message):
        self.service.telegram.updateCommands(message)


    # @ListenerMethod(
    #     interceptor = TelegramConstant.MESSAGE_HANDLER_INTERCEPTOR,
    #     func = lambda message: True
    # )
    # def anythingElse(self, message):
    #     print(message)
    #     print(StringHelper.prettyPython(message))
    #     print(StringHelper.prettyPython(ReflectionHelper.getAttributeDataDictionary(message)))
    #     markup = self.manager.module.types.ReplyKeyboardMarkup(row_width=2, selective=True)
    #     itembtn1 = self.manager.module.types.KeyboardButton('a')
    #     itembtn2 = self.manager.module.types.KeyboardButton('v')
    #     itembtn3 = self.manager.module.types.KeyboardButton('d')
    #     markup.add(itembtn1, itembtn2, itembtn3)
    #     self.manager.bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)
