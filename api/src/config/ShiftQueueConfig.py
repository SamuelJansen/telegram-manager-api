from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


HIT_SHIFT_QUEUE_KEY = globalsInstance.getSetting('queue-manager-api.hit-shift.queue-key')

HIT_SHIFT_EMITTER_URL = globalsInstance.getSetting('queue-manager-api.base-url')
HIT_SHIFT_EMITTER_API_KEY = globalsInstance.getSetting('queue-manager-api.api-key')
HIT_SHIFT_EMITTER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.hit-shift.emitter.timeout')
