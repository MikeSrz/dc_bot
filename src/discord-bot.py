import random
import discord
import os
from discord.ext import commands

TOKEN = os.getenv('TOKEN_DISCORD')

#Creamos intents y le damos la capacidad de leer mensajes.
intents = discord.Intents.default()
intents.message_content = True

#Cuando el usuario ponga !ping se llamará a ping()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    #mensaje de OK para nuesstra consola
    print(f'{bot.user} se ha conectado al servidor!')

@bot.command()
async def pika(ctx):
    messages = [
        "Pika pika!",
        "Pikaaachuuuuuuuuu!",
        "Pinga!",
        ":3"
    ]
    await ctx.send(random.choice(messages))


if __name__ == '__main__':
    if not TOKEN:
        print("Error: No se ha encontrado el token de Discord. Asegúrate de establecer la variable de entorno TOKEN_DISCORD.")
    
    bot.run(TOKEN)