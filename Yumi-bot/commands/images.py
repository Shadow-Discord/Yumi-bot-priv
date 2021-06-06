# imports
import discord
from discord.ext import commands
from flask.wrappers import Request
import aiohttp
import io
import asyncio


# vars

color = 0xECC1BA
trash = '<:trashcan:846484978615058442>'
blacklist = 850376658938757140

# commands class

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,10) 
    async def hug(self, ctx, member: discord.Member = None):



        if member is None:
            member = ctx.author

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/hug')
            hugjson = await request.json()

            embed = discord.Embed(title = f"You have hugged {member.name}, Cute!",color = color)
            embed.set_image(url = hugjson['link'])

            await ctx.reply(embed=embed,mention_author = False)

    @commands.command()
    @commands.cooldown(1,10) 
    async def pat(self, ctx, member: discord.Member = None):

        if member is None:
            member = ctx.author

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/animu/pat')
            patjson = await request.json()

            embed = discord.Embed(title = f"You have patted {member.name}, Cute!",color = color)
            embed.set_image(url = patjson['link'])

            await ctx.reply(embed=embed,mention_author = False)

    @commands.command(aliases = ['trigger'])
    @commands.cooldown(1,10) 
    async def triggered(self, ctx, member: discord.Member=None):


        if not member: # if no member is mentioned
            member = ctx.author # the user who ran the command will be the member
        
        async with aiohttp.ClientSession() as wastedSession:
            async with wastedSession.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format = "png")}') as wastedImage: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await wastedImage.read()) # read the image/bytes
            
                await wastedSession.close()
                
                embed = discord.Embed(title = f'{member} is triggerd. 0-0',color = color)
                embed.set_image(url = "attachment://triggered.gif")
            
                await ctx.reply(embed = embed,file=discord.File(imageData, 'triggered.gif'),mention_author = False)

    @commands.command()
    @commands.cooldown(1,10) 
    async def wasted(self, ctx, member: discord.Member=None):
        
        
        if not member: # if no member is mentioned
            member = ctx.author # the user who ran the command will be the member
        
        async with aiohttp.ClientSession() as wastedSession:
            async with wastedSession.get(f'https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url}') as wastedImage: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await wastedImage.read()) # read the image/bytes
            
                await wastedSession.close()
                
                embed = discord.Embed(title = f'{member} wasted.',color = color)
                embed.set_image(url = "attachment://wasted.gif")
            
                await ctx.reply(embed = embed,file=discord.File(imageData, 'wasted.gif'),mention_author = False)

    @commands.command()
    @commands.cooldown(1,10) 
    async def gay(self, ctx, member: discord.Member=None):

        if not member: # if no member is mentioned
            member = ctx.author # the user who ran the command will be the member
        
        async with aiohttp.ClientSession() as wastedSession:
            async with wastedSession.get(f'https://some-random-api.ml/canvas/gay?avatar={member.avatar_url}') as wastedImage: # get users avatar as png with 1024 size
                imageData = io.BytesIO(await wastedImage.read()) # read the image/bytes
            
                await wastedSession.close()
                
                embed = discord.Embed(title = f"{member}'s Gay profile pic.",color = color)
                embed.set_image(url = "attachment://wasted.gif")
            
                await ctx.reply(embed = embed,file=discord.File(imageData, 'wasted.gif'),mention_author = False)


    @commands.command()
    @commands.cooldown(1,10) 
    async def dog(self, ctx):

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/dog')
            patjson = await request.json()

            embed = discord.Embed(color = color)
            embed.set_image(url = patjson['link'])

            await ctx.reply(embed=embed,mention_author = False)

    @commands.command()
    @commands.cooldown(1,10) 
    async def cat(self, ctx):

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/cat')
            patjson = await request.json()

            embed = discord.Embed(color = color)
            embed.set_image(url = patjson['link'])

            await ctx.reply(embed=embed,mention_author = False)

    @commands.command()
    @commands.cooldown(1,10) 
    async def panda(self, ctx):

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/panda')
            patjson = await request.json()

            embed = discord.Embed(color = color)
            embed.set_image(url = patjson['link'])

            await ctx.reply(embed=embed,mention_author = False)

    @commands.command()
    @commands.cooldown(1,10) 
    async def bird(self, ctx):

        async with aiohttp.ClientSession() as session:
            request = await session.get('https://some-random-api.ml/img/bird')
            patjson = await request.json()

            embed = discord.Embed(color = color)
            embed.set_image(url = patjson['link'])

            await ctx.reply(embed=embed,mention_author = False)

    @commands.group(invoke_without_command = True)
    @commands.cooldown(1,10) 
    async def waifu(self, ctx):



        async with aiohttp.ClientSession() as session:
            request = await session.get('https://pics.hori.ovh:8036/API/sfw/waifu')
            waifujson = await request.json()

            embed = discord.Embed(color = color)
            embed.set_image(url = waifujson['url'])

            await ctx.reply(embed = embed,mention_author = False)

# setup cog class

def setup(bot):
    bot.add_cog(Images(bot))