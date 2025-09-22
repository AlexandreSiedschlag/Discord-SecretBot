from discord_client import Client
from modules.mover import Mover
from modules.auto_ping_missing_players import AutoPingMissingPlayers

class SecretBot(Client):
    def __init__(self):
        super().__init__()
        self.start_modules()
        self.register_commands()

    def start_modules(self):
        self.mover = Mover()
        self.auto_ping = AutoPingMissingPlayers()

    def register_commands(self):
        self.mover.move(self)
        self.mover.move_reacted(self)
        self.auto_ping.register_commands(self)

    def run_bot(self):
        self.tree._client = self
        self.run(self.bot_token)


if __name__ == "__main__":
    secret_bot = SecretBot()
    secret_bot.run_bot()