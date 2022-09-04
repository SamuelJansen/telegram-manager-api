from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


BASE_URL = globalsInstance.getSetting('the-news-api.base-url')
API_KEY = globalsInstance.getSetting('the-news-api.api-key')
TIMEOUT = globalsInstance.getSetting('the-news-api.timeout')
