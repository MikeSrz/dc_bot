import random
import discord
import os
from discord.ext import commands

TOKEN = os.getenv('TOKEN_DISCORD')

#Creamos intents y le damos la capacidad de leer mensajes.
intents = discord.Intents.default()
intents.message_content = True

#Cuando el usuario ponga !miau se llamará a miau()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    #mensaje de OK para nuesstra consola
    print(f'{bot.user} se ha conectado al servidor.')

@bot.command()
async def doctor(ctx):
    messages = [
        "Negocios...",
        "Em si bueno... no se que decir. Bisness",
        "Necesito una pausa para el café.",
        ":3",
        "Lo vemos y te digo...",
        "miau cof cof.. cof...  Llevando datos a decisiones inteligentes como buen miau-doctor en ciencia minina.",
    ]
    await ctx.send(random.choice(messages))


if __name__ == '__main__':
    if not TOKEN:
        print("Error: No se ha encontrado el token de Discord. Asegúrate de establecer la variable de entorno TOKEN_DISCORD.")
    
    bot.run(TOKEN)