from python_framework import Enum, EnumItem


@Enum(associateReturnsTo='command')
class BotComandsEnumeration :
    POST_SHIFT = EnumItem(
        command = 'post_shift',
        description = 'Hit Shift'
    )
    GET_SHIFT = EnumItem(
        command = 'get_shift',
        description = 'Get shif status'
    )

BotComands = BotComandsEnumeration()
