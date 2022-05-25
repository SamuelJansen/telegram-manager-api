from python_framework import ConverterStatic

from constant import NotificationConstant
from enumeration.NotificationSeverity import NotificationSeverity
from enumeration.NotificationStatus import NotificationStatus


class NotificationRequestDto:

    def __init__(self,
        message = None,
        severity = None
    ):
        self.message = ConverterStatic.getValueOrDefault(message, NotificationConstant.DEFAULT_MESSAGE)
        self.severity = NotificationSeverity.map(ConverterStatic.getValueOrDefault(severity, NotificationConstant.DEFAULT_SEVERITY))


class NotificationResponseDto:

    def __init__(self,
        message = None,
        severity = None,
        status = None
    ):
        self.message = ConverterStatic.getValueOrDefault(message, NotificationConstant.DEFAULT_MESSAGE)
        self.severity = NotificationSeverity.map(ConverterStatic.getValueOrDefault(severity, NotificationConstant.DEFAULT_SEVERITY))
        self.status = NotificationStatus.map(ConverterStatic.getValueOrDefault(status, NotificationConstant.DEFAULT_STATUS))
