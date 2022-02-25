from python_helper import Constant as c
from python_helper import RandomHelper
from python_framework import Service, ServiceMethod


@Service()
class TelegramService:

    @ServiceMethod()
    def updateChampionshipTables(self, message):
        self.emitter.telegram.aknowledgeByMessage(message, long=True)
        teamDataList = self.service.aixSportsChampionship.updateAll()
        self.emitter.telegram.successByMessage(
            message,
            text = self.mapper.aixSportsChampionship.fromResponseToText(teamDataList)
        )


    @ServiceMethod()
    def updateChampionshipTable(self, message):
        if self.service.aixSportsChampionship.teamCommandExists(message.text):
            self.emitter.telegram.aknowledgeByMessage(message)
            teamDataList = self.service.aixSportsChampionship.updateByteamCommand(message.text)
            self.emitter.telegram.successByMessage(
                message,
                text = self.mapper.aixSportsChampionship.fromResponseToText(teamDataList)
            )
        else:
            self.emitter.telegram.optionsByChatId(
                message.chat.id,
                'Escolha um time',
                self.service.aixSportsChampionship.getTeamNameList(),
                placeholder = 'Escolha o campeonato que deseja atualizar as tabelas'
            )
