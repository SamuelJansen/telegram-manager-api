from python_helper import log
from globals import getGlobalsInstance
globalsInstance = getGlobalsInstance()


CHAMPIONSHIP_BASE_URL = globalsInstance.getSetting('aix-sports.championship.base-url')
CHAMPIONSHIP_TIMEOUT = globalsInstance.getSetting('aix-sports.championship.timeout')
