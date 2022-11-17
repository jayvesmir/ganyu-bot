from discord import app_commands, Interaction, Embed, Object
from discord.ext import commands
from enkapy import Enka

from ganyuDB import ganyuDB as gdb
from config import IS_DEBUG, DEBUG_GUILD
DEBUG_GUILD = Object(DEBUG_GUILD)

class genshinCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # TODO: Rewrite to use buttons, only testing enka for now.
    @app_commands.command(name='builds', description="Gets your character's builds.")
    @app_commands.guilds(DEBUG_GUILD if IS_DEBUG else None)
    async def builds(self, i: Interaction):
        # TODO: Not be lazy and add a check for a user having a registered UID.
        client: Enka = self.bot.enkaClient
        await client.load_lang('en')

        uid = gdb.getUID(i.user.id)
        user = await client.fetch_user(uid)

        # TODO: Remove testing code fromthe enka.py docs.
        print(f"Nickname: {user.player.nickname}")
        print(f"Level: {user.player.level}")
        for character in user.characters:
            print('-'*20)
            print(f'Name: {character.name}')
            print(f'Weapon: {character.weapon.nameText}')
            print('Artifacts:')
            for artifact in character.artifacts:
                print(f'\t{artifact.setNameText} {artifact.nameText}:')
                print(f'\t{artifact.main_stat.prop}:{artifact.main_stat.value}')
                for sub_stats in artifact.sub_stats:
                    print(f'\t\t{sub_stats.prop}:{sub_stats.value}')
            print('-'*20)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(genshinCog(bot))
