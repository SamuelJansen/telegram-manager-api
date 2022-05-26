from python_framework import Enum, EnumItem


@Enum(associateReturnsTo='command')
class BotComandsEnumeration :
    POST_SHIFT = EnumItem(
        command = 'hit_shift',
        description = 'Hit shift'
    )
    GET_SHIFT = EnumItem(
        command = 'get_shift',
        description = 'Get shif status'
    )


    UPDATE_COMMANDS = EnumItem(
        command = 'refresh_commands',
        description = 'Refresh commands'
    )

BotComands = BotComandsEnumeration()
