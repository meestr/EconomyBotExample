from discord.ext import commands
import random
import aiohttp
from utils import client, macro
import json
import asyncio

class Games(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.client = client.Client()
        with open('config.json','r') as data:
           self.data = json.load(data) 
        self.currency = self.data['currency']
    @commands.command(name="coinflip")
    @commands.cooldown(1,5)
    async def coinflip(self, ctx, bet, side):
        coin = random.choice(
            [{'heads': 'https://www.offthegridnews.com/wp-content/uploads/2012/04/silver_quarter.png'}, {'tails': 'http://washington-quarters.com/coins/1944-quarter-reverse.png'}])
        temp = await self.client.get_value(ctx.message.author.id)
        current = temp[0][1]
        if str(bet).lower() == 'all':
            bet = current
        bet = int(bet)
        assert current >= bet > 0, "Too low of a bet!"
        if side not in ('tails', 'heads'):
            return await ctx.send(embed=await macro.error(
                f"""You didn't enter a correct side. \n(Your side {side} vs ``tails`` or ``heads``) \nPlease re-enter your command.""",
                footer=ctx.message.author, icon=ctx.message.author.avatar_url))
        if side in coin:
            await self.client.update(bal=2 * bet + current, _id=ctx.message.author.id)
            return await ctx.send(
                embed=await macro.send(
                    f'The coin landed on {side}.\nYou won ``{2*bet}`` {self.currency}.\nYour balance is now ``{bet*2+current}`` {self.currency}. ',
                    thumb=coin[side], footer=ctx.message.author, icon=ctx.message.author.avatar_url))
        else:
            loss = current - bet
            await self.client.update(bal=loss, _id=ctx.message.author.id)
            return await ctx.send(embed=await macro.send(
                f"""The coin landed on {str(coin.keys()).replace("dict_keys(['", "").replace("'])", "")}. \nYou lost ``{bet}``. \nYour balance is now ``{current-bet}`` {self.currency}.""",
                thumb=coin.get(str(coin.keys()).replace("dict_keys(['", "").replace("'])", "")),
                footer=ctx.message.author, icon=ctx.message.author.avatar_url))
    @commands.command(name='dice', aliases=['die'])
    @commands.cooldown(1, 5)
    async def dice(self, ctx, bet, side: int):
        assert type(
            bet) == str, 'You likely put the arguments in the wrong order! It should be something like ``p!dice ' \
                         '1 4``! '
        assert side in (
            1, 2, 3, 4, 5,
            6), "You've put an invalid argument for the ``side``! Please use a number from ``1`` to ``6``."
        temp = await self.client.get_value(ctx.message.author.id)
        current = temp[0][1]
        if str(bet).lower() == 'all':
            bet = current
        bet = int(bet)
        assert current >= bet > 0, "Too low of a bet!"
        if random.randint(1, 6) == side:
            await self.client.update(bal=bet * 3 + current, _id=ctx.message.author.id)
            await ctx.send(embed=await macro.send(
                f"You rolled a ``{side}``.\nYou won ``{bet*2}`` Cubes.\nYour balance is now ``{bet*3+current}`` Cubes.", footer=ctx.message.author, icon=ctx.message.author.avatar_url))
        else:
            ohno = ['1', '2', '3', '4', '5', '6']
            ohno.pop(side - 1)
            false_side = random.choice(ohno)
            await self.client.update(bal=current - bet, _id=ctx.message.author.id)
            await ctx.send(embed=await macro.send(
                f"You rolled a {false_side}.\nYou lost ``{bet}`` Cubes.\nYour balance is now ``{current-bet}`` Cubes.",footer=ctx.message.author,
                icon=ctx.message.author.avatar_url))
    @commands.command(name='slots')
    #@commands.cooldown(1, 8)
    async def slots(self, ctx, bet):
        temp = await self.client.get_value(ctx.message.author.id)
        current = temp[0][1]
        if bet == 'all':
            bet = current
        bet = int(bet)
        assert 0 < bet <= current, "You don't have a large enough balance for this. >:c"
        slots = ['chocolate_bar', 'bell', 'tangerine', 'apple', 'cherries', 'seven']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        msg = await ctx.send(embed=await macro.send('Rolling...'))
        await asyncio.sleep(2.5)
        if slot1 == slot2 and slot2 == slot3 and slot3 != 'seven':
            await self.client.update(bal=2 * bet + current, _id=ctx.message.author.id)
            await msg.edit(embed=await macro.send(
                f"|:{slot1}:|:{slot2}:|:{slot3}:|\nGood! You won ``{bet*2}`` Cubes!\nYour balance is now ``{bet*2+current}`` Cubes",
                footer=ctx.message.author,
                icon=ctx.message.author.avatar_url
            ))
        elif slot1 == 'seven' and slot2 == 'seven' and slot3 == 'seven':
            await self.client.update(bal=int(5 * bet + current), _id=ctx.message.author.id)
            await msg.edit(embed=await macro.send(
                f"|:{slot1}:|:{slot2}:|:{slot3}:|\nJACKPOT!! You won ``{bet*5}`` Cubes!\nYour balance is now ``{bet*5+current}`` Cubes",
                footer=ctx.message.author,
                icon=ctx.message.author.avatar_url
        elif slot1 == slot2 or slot1 == slot3 or slot2 == slot3:
            await self.client.update(bal=int(3 * bet + current), _id=ctx.message.author.id)
            await msg.edit(embed=await macro.send(
                f"|:{slot1}:|:{slot2}:|:{slot3}:|\nGreat! You won ``{bet*3}`` Cubes!\nYour balance is now ``{bet*3+current}`` Cubes",
                footer=ctx.message.author,
                icon=ctx.message.author.avatar_url
            ))

        else:
            await self.client.update(bal=current - bet, _id=ctx.message.author.id)
            await msg.edit(embed=await macro.send(
                f"|:{slot1}:|:{slot2}:|:{slot3}:|\nOh no... You lost ``{bet}`` Cubes!\nYour balance is now ``{current-bet}`` Cubes",
                footer=ctx.message.author,
                icon=ctx.message.author.avatar_url
            ))
def setup(bot:commands.Bot):
    bot.add_cog(Games(bot=bot))
