import discord
import config

from discord.ext import commands

client = commands.Bot(command_prefix="*", intents=intents, case_sensitive=True)

@client.event
async def on_ready():
  print("Bot online!")
 
 client.run(config.TOKEN)
