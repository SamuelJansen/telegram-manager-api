from python_framework import Enum, EnumItem


@Enum(associateReturnsTo='command')
class BotTheNewsComandsEnumeration:
    THE_NEWS = EnumItem(
        command = 'the_news',
        description = 'The news'
    )
    CREATE_TODAY_NEWS = EnumItem(
        command = 'create_today_news',
        description = 'Create today news'
    )


BotTheNewsComands = BotTheNewsComandsEnumeration()
