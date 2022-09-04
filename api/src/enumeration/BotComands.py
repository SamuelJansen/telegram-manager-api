from python_framework import Enum, EnumItem


@Enum(associateReturnsTo='command')
class BotComandsEnumeration:


    LIST_COMMANDS = EnumItem(
        command = 'list_commands',
        description = 'List commands'
    )
    UPDATE_COMMANDS = EnumItem(
        command = 'update_commands',
        description = 'Update commands'
    )

BotComands = BotComandsEnumeration()
