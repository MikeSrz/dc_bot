import datetime
from zoneinfo import ZoneInfo
import asyncio
import random
from discord.ext import commands, tasks
class PlayPetancaController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.petanca_message.start() #Como esto ya no es un evento que espera a que alguien ponga un comando, debes indicarle que empiece.
        self.messages = [
            "Ignorada bastisima...",
            "Racismo.",
            "Tu #%TA Madre bot de petanca!",
            "Vivimos en una sociedad...",
            "Sálganse del chat, quiero estar solo :("
        ]

    @tasks.loop(time=datetime.time(hour=20, minute=35, tzinfo=ZoneInfo("Europe/Madrid")))
    async def petanca_message(self):
        print("se ha ejecutada petanca")
        canal = self.bot.get_channel(776505761836171315) #Id del canal
        if canal is None:
            print("No he encontrado Petanca")
            return
        message = random.choice(self.messages)
        await canal.send("hora de jugar a la petanca!")
        await asyncio.sleep(2)
        await canal.send("!petanqueo")
        await asyncio.sleep(2)
        await canal.send(message)
        


async def setup(bot): #esta función es la que busca el hook.
    await bot.add_cog(PlayPetancaController(bot)) #Add_cog es un método de discord.py.