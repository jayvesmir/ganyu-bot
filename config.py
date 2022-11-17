import ujson
from discord import Object

with open('config.json', 'r') as __f:
    __jsonConfig = ujson.loads(__f.read())
TOKEN = __jsonConfig['token']
PREFIX: str = __jsonConfig['prefix']
IS_DEBUG = False
DEBUG_GUILD = None

try:
    __debugState: str = __jsonConfig['is_debug']
    if __debugState.lower() == 'true':
        IS_DEBUG = True
    try:
        __debugGuild: str = __jsonConfig['debug_guild']
        try:
            DEBUG_GUILD = int(__debugGuild)
        except ValueError as __e:
            DEBUG_GUILD = 'Invalid guild'
    except KeyError:
        raise Exception('Bot is in debug mode but no debug_guild is set.')
except KeyError:
    print("Not debug")