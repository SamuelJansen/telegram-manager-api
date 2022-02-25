from python_framework import Enum, EnumItem


@Enum(associateReturnsTo='command')
class TelegramComandsEnumeration :
    UPDATE_CHAMPIONSHIP_TABLES = EnumItem(
        command = 'atualiza_tabelas_campeonatos',
        description = 'Atualiza as tabelas de todos os campeonatos'
    )
    UPDATE_CHAMPIONSHIP_TABLE = EnumItem(
        command = 'atualiza_tabela_campeonato',
        description = 'Atualiza a tabela de um campeonato'
    )

TelegramComands = TelegramComandsEnumeration()
