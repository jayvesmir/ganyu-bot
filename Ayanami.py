from pathlib import Path
import sqlite3 as sqlite

import discord
from discord.ext import commands
from discord.ext.commands import ExtensionAlreadyLoaded, ExtensionFailed, ExtensionNotLoaded, NoEntryPointError

from logger import log
from ganyuDB import ganyuDB as gdb
from config import TOKEN, PREFIX

class Ganyu(commands.Bot):
    def __init__(self, _prefix: str):
        super().__init__(intents=discord.Intents.all(), command_prefix=_prefix)
        self.synced = False

        if not gdb.dbExists('ganyuDB/db/users.db'):
            conn = sqlite.connect('ganyuDB/db/users.db')
            curr = conn.cursor()
            curr.execute('CREATE TABLE users (id text, uid text)')
            conn.commit()
            conn.close()
            log('ganyuDB').info('Created database.')
        self.userDB = gdb(sqlite.connect('ganyuDB/db/users.db'))

    async def setup_hook(self) -> None:
        for filepath in Path("./cogs").glob('**/*.py'):
            cogName = Path(filepath).stem
            try:
                await self.load_extension(f"cogs.{cogName}")
            except (ExtensionAlreadyLoaded, ExtensionFailed, ExtensionNotLoaded, NoEntryPointError) as e:
                log('CogLoader').warning(f'Failed to load {cogName}\n {e}')

    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel:
            await channel.send(f'{member.mention} Welcome To The Server!')

    async def on_ready(self):
        await self.change_presence(status=discord.Status.idle, activity=discord.Game('with your data'))
        log().info(f'Ganyu is online as {self.user}.')

def main():
    bot = Ganyu(PREFIX)
    bot.run(TOKEN)

if __name__ == '__main__':
    main()