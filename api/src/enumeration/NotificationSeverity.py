from python_framework import Enum, EnumItem


@Enum()
class NotificationSeverityEnumeration :

    NONE  = EnumItem(degree=-1)

    DEBUG = EnumItem(degree=0)
    SETTINGS = EnumItem(degree=1)
    INFO = EnumItem(degree=2)
    STATUS = EnumItem(degree=3)
    
    WARNING = EnumItem(degree=4)
    FAILURE = EnumItem(degree=5)
    ERROR = EnumItem(degree=6)

NotificationSeverity = NotificationSeverityEnumeration()
