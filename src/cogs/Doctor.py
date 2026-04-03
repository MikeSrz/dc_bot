import random
class Doctor(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.messages = [
            "Negocios...",
            "Em si bueno... no se que decir. Bisness",
            "Necesito una pausa para el café.",
            ":3",
            "El café es como un abrazo cálido en una taza.",
            "Lo consultaré con mi mujer...",
            "miau cof cof.. cof...  Llevando datos a decisiones inteligentes como buen miau-doctor en ciencia minina."
        ]

    @commands.command(name='doctor')
    async def doctor_command(self, ctx):
        response = random.choice(self.messages)
        await ctx.send(response)
    
async def setup(bot): #esta función es la que busca el hook.
    await bot.add_cog(Doctor(bot)) #Add_cog es un método de discord.py.