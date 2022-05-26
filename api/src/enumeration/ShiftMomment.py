from globals import getGlobalsInstance
from python_helper import Constant as c
from python_framework import Enum, EnumItem


globalsInstance = getGlobalsInstance()

@Enum()
class ShiftMommentEnumeration :
    FIRST_SHIFT_BEGIN = EnumItem()
    FIRST_SHIFT_END = EnumItem()
    SECOND_SHIFT_BEGIN = EnumItem()
    SECOND_SHIFT_END = EnumItem()

ShiftMomment = ShiftMommentEnumeration()
