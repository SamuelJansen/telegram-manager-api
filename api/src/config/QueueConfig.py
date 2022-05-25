from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


API_NOTIFICATIONS_QUEUE_KEY = globalsInstance.getSetting('queue-manager-api.api-notifications.queue-key')
API_NOTIFICATIONS_EMITTER_API_KEY = globalsInstance.getSetting('queue-manager-api.api-key')
API_NOTIFICATIONS_EMITTER_BASE_URL = globalsInstance.getSetting('queue-manager-api.base-url')
API_NOTIFICATIONS_EMITTER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.api-notifications.emitter.timeout')
API_NOTIFICATIONS_LISTENER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.api-notifications.listener.timeout')

SEND_TELEGRAM_QUEUE_KEY = globalsInstance.getSetting('queue-manager-api.send-telegram.queue-key')
SEND_TELEGRAM_EMITTER_API_KEY = globalsInstance.getSetting('queue-manager-api.api-key')
SEND_TELEGRAM_EMITTER_BASE_URL = globalsInstance.getSetting('queue-manager-api.base-url')
SEND_TELEGRAM_EMITTER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.send-telegram.emitter.timeout')
SEND_TELEGRAM_LISTENER_TIMEOUT = globalsInstance.getSetting('queue-manager-api.send-telegram.listener.timeout')
