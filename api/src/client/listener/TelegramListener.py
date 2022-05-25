from python_helper import log
from python_framework import HttpStatus
from queue_manager_api import MessageListener, MessageListenerMethod

from ApiKeyContext import ApiKeyContext
from config import QueueConfig


@MessageListener(
    timeout = QueueConfig.SEND_TELEGRAM_LISTENER_TIMEOUT
    , muteLogs = False
    , logRequest = True
    , logResponse = True
)
class TelegramListener:

    @MessageListenerMethod(url = '/listener/messages',
        requestClass = [[dict]],
        apiKeyRequired=[ApiKeyContext.ADMIN, ApiKeyContext.USER, ApiKeyContext.API],
        runInAThread = True
        , logRequest = True
        , logResponse = True
    )
    def acceptMessages(self, dtoList):
        return self.service.telegram.acceptMessages(dtoList), HttpStatus.ACCEPTED
