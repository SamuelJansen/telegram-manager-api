from python_framework import HttpClient, HttpClientMethod

from config import AixSportsConfig


@HttpClient(
    url = AixSportsConfig.CHAMPIONSHIP_BASE_URL
)
class AixSportsChampionshipClient :

    @HttpClientMethod(
        url = '/g1',
        logRequest = True,
        logResponse = True,
        timeout = AixSportsConfig.CHAMPIONSHIP_TIMEOUT
    )
    def updateByIdList(self, requestBody):
        return self.put(body=requestBody)


    @HttpClientMethod(
        url = '/g1/all',
        logRequest = True,
        logResponse = True,
        timeout = AixSportsConfig.CHAMPIONSHIP_TIMEOUT
    )
    def updateAll(self):
        return self.put()
