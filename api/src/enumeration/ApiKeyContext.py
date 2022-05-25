from python_framework import Enum, EnumItem


@Enum()
class ApiKeyContextEnumeration :
    ADMIN = EnumItem()
    USER = EnumItem()
    API = EnumItem()

ApiKeyContext = ApiKeyContextEnumeration()
