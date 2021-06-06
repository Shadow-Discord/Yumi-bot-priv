# discord imports

from aiohttp.client import request
import discord
from discord.ext import commands

# other imports

import aiohttp

# vars

color = 0xECC1BA

# commnds class

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/meme')
            memejson = await request.json()

            embed = discord.Embed(color = color)
            embed.set_image(url = memejson['image'])

            await ctx.send(embed=embed)

# setup cog class

def setup(bot):
    bot.add_cog(Fun(bot))