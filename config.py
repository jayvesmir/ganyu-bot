import ujson
from discord import Object

with open('config.json', 'r') as f:
    jsonConfig = ujson.loads(f.read())
TOKEN = jsonConfig['token']
PREFIX: str = jsonConfig['prefix']