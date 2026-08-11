class PlayPetancaController(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.petanca_message.start() #Como esto ya no es un evento que espera a que alguien ponga un comando, debes indicarle que empiece.

    @tasks.loop(time=datetime.time(hour=19, minute=55))
    async def petanca_message(self):
        canal = self.bot.get_channel(ID_DEL_CANAL)
        await canal.send("hora de jugar a la petanca!")
        await canal.send("!petanca")


async def setup(bot): #esta función es la que busca el hook.
    await bot.add_cog(PlayPetancaController(bot)) #Add_cog es un método de discord.py.