from python_framework import JwtConstant, HttpClient, HttpClientMethod

from config import TheNewsClientConfig


@HttpClient(
    url = TheNewsClientConfig.BASE_URL,
    timeout = TheNewsClientConfig.TIMEOUT,
    headers = {
        'Content-Type': 'application/json',
        JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {TheNewsClientConfig.API_KEY}'
    }
    , logRequest = True
    , logResponse = True
)
class TheNewsClient:

    @HttpClientMethod(
        url = '/today',
        responseClass=[[dict]]
        , logRequest = True
        , logResponse = True
    )
    def createTodayNews(self):
        return self.put()
