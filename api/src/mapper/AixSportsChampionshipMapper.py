from python_helper import Constant as c
from python_helper import log, StringHelper
from python_framework import Mapper, MapperMethod, EnumItem, HttpStatus, FlaskUtil

import AixSportsConfig as ASC


@Mapper()
class AixSportsChampionshipMapper:

    @MapperMethod(requestClass=[[dict]])
    def fromResponseToText(self, teamDataList):
        return StringHelper.join(
            [
                f'Aix Sports: {teamData["destinyUrl"]}{c.NEW_LINE}G1: {teamData["originUrl"]}' for teamData in teamDataList
            ],
            character = c.NEW_LINE
        )
