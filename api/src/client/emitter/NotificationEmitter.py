from python_helper import Constant as c
from python_helper import log, ObjectHelper, StringHelper
from queue_manager_api import MessageEmitter, MessageEmitterMethod
from python_framework import HttpStatus, GlobalException

from config import QueueConfig
import NotificationDto


@MessageEmitter(
    url = QueueConfig.API_NOTIFICATIONS_EMITTER_BASE_URL,
    headers = {
        'Api-Key': f'Bearer {QueueConfig.API_NOTIFICATIONS_EMITTER_API_KEY}'
    },
    timeout = QueueConfig.API_NOTIFICATIONS_EMITTER_TIMEOUT
    , logRequest = True
    , logResponse = True
)
class NotificationEmitter :

    @MessageEmitterMethod(
        queueKey = QueueConfig.API_NOTIFICATIONS_QUEUE_KEY,
        requestClass = [[NotificationDto.NotificationRequestDto]],
        runInAThread = True
        , logRequest = True
        , logResponse = True
    )
    def speakAll(self, dtoList):
        return self.emit(body=dtoList)
