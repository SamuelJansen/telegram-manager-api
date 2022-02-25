from python_framework import Service, ServiceMethod


CHAMPIONSHIP_DICTIONARY = {
    167: '/campeonato_catarinense',
    163: '/campeonato_mineiro',
    169: '/campeonato_paranaense',
    165: '/campeonato_gaucho',
    168: '/paulista_serie_a3'
}


@Service()
class AixSportsChampionshipService :

    @ServiceMethod(requestClass=[str])
    def updateByteamCommand(self, teamCommand):
        return self.updateByteamCommandList([teamCommand])


    @ServiceMethod(requestClass=[[str]])
    def updateByteamCommandList(self, teamCommandList):
        return self.client.aixSportsChampionship.updateByIdList({
            'championshipIdList': [
                id for id,teamCommand in CHAMPIONSHIP_DICTIONARY.items() if teamCommand in teamCommandList
            ]
        })


    @ServiceMethod()
    def updateAll(self):
        return self.client.aixSportsChampionship.updateAll()


    @ServiceMethod()
    def teamCommandExists(self, teamName):
        return teamName in CHAMPIONSHIP_DICTIONARY.values()


    @ServiceMethod()
    def getTeamNameList(self):
        return [*CHAMPIONSHIP_DICTIONARY.values()]
