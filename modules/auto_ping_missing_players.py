from collections import Counter
from datetime import datetime
from libs.raid_helper_api import RaidHelperAPI
import discord

roles_ammount_dict = {
    "MainTank": 1,
    "MainHealer": 1,
    "OffTankGolem": 1,
    "Paratempo": 1,
    "Silence": 1,
    "ShadowCaller": 1,
    "Scout": 1,
    "RaizPTHeal": 1,
    "Fire": 1,
    "Aguia": 1,
    "Frost": 1,
    "Besta": 0,
    "RaizPTHeal": 2,
    "QuebraReinos": 1,
    "CacaEspiritos": 0,
}


class AutoPingMissingPlayers:
    def __init__(self):
        self.raid = None

    def register_commands(self, bot):
        self.raid = RaidHelperAPI(server_id=bot.server_id)

        @bot.tree.command(
            guild=discord.Object(id=int(bot.server_id)),
            name="autoping",
            description="Verifica e avisa as classes que estão faltando no evento"
        )
        async def auto_ping(interaction):
            await interaction.response.defer(ephemeral=True)
            await self.auto_ping_missing_roles(interaction.channel)
            await interaction.followup.send("AutoPing finalizado!", ephemeral=True)

    async def auto_ping_missing_roles(self, channel):
        events = self.raid.get_server_events(
            channel_filter=self.raid.CHANNELS["Ping avalon"]
        )
        for event in events["postedEvents"]:
            response = self.raid.get_event(event_id=event["id"])
            avalon_time = datetime.fromtimestamp(
                response.start_time
            ).strftime("%d/%m as %H:%M")

            # await channel.send(
            #     f"**Avalon:** {event['title']} | Hora: {avalon_time} | "
            #     f"Caller: {event['leaderName']}"
            # )
            
            mensagens = [
                f"**Avalon:** {event['title']} | Hora: {avalon_time} | "
                f"Caller: {event['leaderName']}"
            ]

        for ann in response.announcements:
            ts = response.start_time - int(ann.time) * 60
            hora = datetime.fromtimestamp(ts).strftime("%d/%m as %H:%M")

            class_counter = Counter(
                p.class_name for p in response.sign_ups if p.entry_time <= ts
            )

            faltando = []
            for class_name, required in roles_ammount_dict.items():
                current = class_counter.get(class_name, 0)
                if current < required:
                    faltando.append(class_name)

            if faltando:
                msg = f"[{hora}] Faltando " + " | ".join(f"@{c}" for c in faltando)
                mensagens.append(msg)

        if mensagens:
            await channel.send("\n".join(mensagens))