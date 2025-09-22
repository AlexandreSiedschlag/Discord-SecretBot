import discord
from discord import app_commands
from modules.mover import Mover
from utils import load_that_shit

class Client(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)

        self.bot_token = load_that_shit()["bot_token"]
        self.server_id = "1206945281279660092"
        self.tree = app_commands.CommandTree(self)
        self.synced = False
        self.table_message = None

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:
            await self.tree.sync(guild=discord.Object(id=self.server_id))
            self.synced = True
        print(f"Entramos como {self.user}.")
