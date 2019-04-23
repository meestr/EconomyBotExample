import discord
import json

with open("config.json",'r') as data:
    data = json.load(data)

class Macro:
    @staticmethod
    async def message(description: str = None, title: str = None, thumbnail: str = None, color: discord.Color = discord.Color.from_rgb(data['color'])):
        embed = discord.Embed(
            type='rich',
            description=description,
            title=title
        )
        if thumbnail:
            embed.set_thumbnail(url=thumbnail)
        return embed
    @classmethod
    async def error(cls, description: str):
        return await cls.message(
            description=description, 
            color=discord.Color.red()
        )

error = Macro.error
send = Macro.message
