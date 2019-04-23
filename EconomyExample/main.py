from discord.ext import commands
import discord
import json


with open("config.json", "r") as data:
    data = json.load(data)


class Cogs:
    safe = [
        "cogs.games",
        "cogs.player"
    ]

bot = commands.Bot(command_prefix=data['commandPrefix'])

@bot.event
async def on_ready():
    print(f"READY\nUSER: {bot.user}\nSERVERS: {len(bot.guilds)}")
    await bot.change_presence(activity=discord.Game(name=f"{data['commandPrefix']}help for help. In {len(bot.guilds)} servers!"))

for ext in Cogs.safe:
    bot.load_extenstion(ext)

bot.run(data['token'])
