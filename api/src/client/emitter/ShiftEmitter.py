from python_framework import Serializer, HttpStatus, JwtConstant
from queue_manager_api import MessageEmitter, MessageEmitterMethod, MessageDto

from config import ShiftQueueConfig, ShiftClientConfig


@MessageEmitter(
    url = ShiftQueueConfig.HIT_SHIFT_EMITTER_URL,
    timeout = ShiftQueueConfig.HIT_SHIFT_EMITTER_TIMEOUT,
    headers = {
        'Content-Type': 'application/json',
        JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {ShiftQueueConfig.HIT_SHIFT_EMITTER_API_KEY}'
    }
    , muteLogs = False
    , logRequest = True
    , logResponse = True
)
class ShiftEmitter:

    @MessageEmitterMethod(
        queueKey = ShiftQueueConfig.HIT_SHIFT_QUEUE_KEY,
        requestHeadersClass=[dict],
        requestClass=[dict]
        # responseClass=[[dict]]
        , logRequest = True
        , logResponse = True
    )
    def hitShift(self, dto, headers=None):
        return self.emit(
            headers = headers,
            messageHeaders = {
                JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {ShiftClientConfig.API_KEY}'
            },
            body = dto
        )

    @MessageEmitterMethod(
        queueKey = ShiftQueueConfig.HIT_SHIFT_NOW_QUEUE_KEY
        # requestHeadersClass=[dict],
        # requestClass=[dict]
        # responseClass=[[dict]]
        , logRequest = True
        , logResponse = True
    )
    def hitShiftNow(self):
        return self.emit(
            # headers = headers,
            messageHeaders = {
                JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {ShiftClientConfig.API_KEY}'
            },
            body = dto
        )
