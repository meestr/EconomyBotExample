from discord.ext import commands
from utils import macro, client
import json

class Player(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = client.Client()
        with open('config.json','r') as data:
            data = json.load(data)
    @commands.command(name='create')
    async def create(self, ctx):
        check = await self.client.get_value(ctx.message.author.id)
        if len(check) > 0:
            return await ctx.send(embed=await macro.error("You've already created an account."))
        await self.client.create_value(ctx.message.author.id)
        return await ctx.send(embed=await macro.send(f"You've created an account! Your balance is now 0{data['currency']}"))

    @commands.command(name='bal')
    async def bal(self, ctx):
        check = await self.client.get_value(ctx.message.author.id)
        balance = check[0][1]
        return await ctx.send(embed=await macro.send(embed=await macro.send(f"You have {balance}{data['currency']}")))
def setup(bot:commands.Bot):
    bot.add_cog(Player(bot))