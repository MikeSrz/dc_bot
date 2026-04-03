import discord
import os
from discord.ext import commands

class MiBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)
    
    #Con load_extension se cargan los cogs, y con setup_hook se hace que se carguen al iniciar el bot.
    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await self.load_extension(f'cogs.{filename[:-3]}')
                print(f'Cog {filename[:-3]} cargado.')
    
    async def on_ready(self):
        print(f'Bot conectado como {self.user}')


if __name__ == '__main__':
    TOKEN = os.getenv('TOKEN_DISCORD')
    if not TOKEN:
        print("Error: No se ha encontrado el token de Discord. Asegúrate de establecer la variable de entorno TOKEN_DISCORD.")
    else:
        bot = MiBot()
        bot.run(TOKEN)