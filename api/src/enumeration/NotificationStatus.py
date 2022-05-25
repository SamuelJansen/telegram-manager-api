from python_framework import Enum, EnumItem


@Enum()
class NotificationStatusEnumeration :

    NONE = EnumItem()

    RECEIVED = EnumItem()
    DELIVERED = EnumItem()
    NOT_DELIVERED = EnumItem()

NotificationStatus = NotificationStatusEnumeration()
