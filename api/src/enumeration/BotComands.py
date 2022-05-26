from python_framework import Enum, EnumItem

from enumeration.ShiftMomment import ShiftMomment


@Enum(associateReturnsTo='command')
class BotComandsEnumeration :
    HIT_SHIFT = EnumItem(
        command = 'hit_shift',
        description = 'Hit shift'
    )
    HIT_FIRST_SHIFT_BEGIN = EnumItem(
        command = 'hit_first_shift_begin',
        description = 'Hit first shift begin',
        momment = ShiftMomment.FIRST_SHIFT_BEGIN
    )
    HIT_FIRST_SHIFT_END = EnumItem(
        command = 'hit_first_shift_end',
        description = 'Hit first shift end',
        momment = ShiftMomment.FIRST_SHIFT_END
    )
    HIT_SECOND_SHIFT_BEGIN = EnumItem(
        command = 'hit_second_shift_begin',
        description = 'Hit second shift begin',
        momment = ShiftMomment.SECOND_SHIFT_BEGIN
    )
    HIT_SECOND_SHIFT_END = EnumItem(
        command = 'hit_second_shift_end',
        description = 'Hit second shift end',
        momment = ShiftMomment.SECOND_SHIFT_END
    )
    GET_SHIFT = EnumItem(
        command = 'get_shift',
        description = 'Get shif status'
    )


    COMMANDS = EnumItem(
        command = 'commands',
        description = 'Refresh commands'
    )

BotComands = BotComandsEnumeration()
