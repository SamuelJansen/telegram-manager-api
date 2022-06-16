from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


BASE_URL = globalsInstance.getSetting('shift-manager-api.base-url')
API_KEY = globalsInstance.getSetting('shift-manager-api.api-key')
TIMEOUT = globalsInstance.getSetting('shift-manager-api.timeout')
