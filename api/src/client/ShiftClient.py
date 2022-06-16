from python_framework import JwtConstant, HttpClient, HttpClientMethod

from config import ShiftClientConfig


@HttpClient(
    url = ShiftClientConfig.BASE_URL,
    timeout = ShiftClientConfig.TIMEOUT,
    headers = {
        'Content-Type': 'application/json',
        JwtConstant.DEFAULT_JWT_API_KEY_HEADER_NAME: f'Bearer {ShiftClientConfig.API_KEY}'
    }
    , logRequest = True
    , logResponse = True
)
class ShiftClient:

    @HttpClientMethod(
        url = '/shift/today',
        responseClass=[[dict]]
        , logRequest = True
        , logResponse = True
    )
    def getTodayShift(self):
        return self.get()
