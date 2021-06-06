# imports
from logging import error
import discord
from discord import mentions
from discord.ext import commands, menus

# other imports

import asyncio
import io
import os
import traceback
import textwrap
from contextlib import redirect_stdout
import async_tio 
# variables 

color = 0xECC1BA
yes = '<:greenTick:596576670815879169>'
no = '<:redTick:596576672149667840>'
trashcan = '<:trashcan:846484978615058442>'



class MyMenu(menus.Menu):
    async def send_initial_message(self, ctx, channel):

        embed = discord.Embed(description = f'Are you sure you want to canceled...\n\nYes {yes} | No {no}',color=color)
        return await channel.send(embed=embed)

    @menus.button(yes)
    async def on_thumbs_up(self, payload):

        embed = discord.Embed(description = f'{yes} | Logging out bye...',color = color)
        await self.message.edit(embed=embed)
        await self.bot.close()

    @menus.button(no)
    async def on_thumbs_down(self, payload):
        
        embed = discord.Embed(description = f'{no} | Shutdown has been canceled...',color = color)
        await self.message.edit(embed=embed)

    @menus.button(trashcan)
    async def on_stop(self, payload):
        self.stop()
        await self.message.delete()

# cog commands class

class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self._last_result = None
        self.tio = async_tio.Tio()

    def cleanup_code(self, content):
        if content.startswith('```') and content.endswith('```'):
            return '\n'.join(content.split('\n')[1:-1])

    def owner(ctx):
        return ctx.message.author.id == 534403455201312793

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} | Owner cog loaded')

    @commands.command(hidden=True)
    @commands.check(owner)
    async def load(self,ctx,module):

        try:
            self.bot.load_extension(f'commands.{module}')
        except Exception as e:
            await ctx.message.add_reaction(no)
            shadow = self.bot.get_user()      
            await shadow.send(embed=discord.Embed(description = f'```py\n{traceback.format_exc()}\n```',color = color))
            print(e)
        else:
            await ctx.message.add_reaction(yes)

    @commands.command(hidden=True)
    @commands.check(owner)
    async def unload(self, ctx, *, module : str):
        """Unloads a module."""
        try:
            self.bot.unload_extension(f'commands.{module}')
        except Exception as e:
            await ctx.message.add_reaction(no)
            shadow = self.bot.get_user()      
            await shadow.send(embed=discord.Embed(description = f'```py\n{traceback.format_exc()}\n```',color = color))
            print(e)
        else:
            await ctx.message.add_reaction(yes)

    @commands.command(aliases = ['rl'])
    @commands.check(owner)
    async def reload(self,ctx, *, module : str = None):

        try:
            self.bot.unload_extension(f'commands.{module}')
            self.bot.load_extension(f'commands.{module}')

        except Exception as e:
            await ctx.message.add_reaction(no)
            shadow = self.bot.get_user(534403455201312793)           
            await shadow.send(embed=discord.Embed(description = f'```py\n{traceback.format_exc()}\n```',color = color))
            print(e)
        else:
            await ctx.message.add_reaction(yes)

    @commands.command(aliases = ['r','rs','~'])
    @commands.check(owner)
    async def restart(self, ctx):
        success = []
        for filename in os.listdir("./commands"):
            if filename.endswith(".py"):
                try:
                    self.bot.reload_extension(f"commands.{filename[:-3]}")
                    success.append(filename[:-3])

                    await ctx.message.add_reaction(yes)
                except Exception as e:
                    await ctx.message.add_reaction(no)

                    shadow = await self.bot.get_user(841321088445448212)
                    
                    await shadow.send(embed=discord.Embed(description = f'```py\n{traceback.format_exc()}\n```',color = color))

    @commands.command()
    @commands.check(owner)
    async def cleanup(self, ctx,amount = 5):

        def check(m):
            return (m.author == ctx.me)

        await ctx.channel.purge(limit = amount,check = check)
        await ctx.message.add_reaction(yes)

    @commands.command()
    @commands.check(owner)
    async def shutdown(self, ctx):

        m = MyMenu()
        await m.start(ctx)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == trashcan

        try:
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
        except asyncio.TimeoutError:
            return
        else:
            await ctx.message.add_reaction(yes)

    @commands.command()
    @commands.check(owner)
    async def env(self, ctx):

        await ctx.reply(embed = discord.Embed(description = "```yaml\n'yumi': self.bot\n'ctx': ctx\n'channel': ctx.channel\n'author': ctx.author\n'guild': ctx.guild\n'message': ctx.message,\n'_': self._last_result'\n```",color = color),mention_author = False) 

    @commands.command()
    @commands.check(owner)
    async def deval(self, ctx, *,body: str):

        env = {
            'yumi': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:

            embed = discord.Embed(title = '__Error Found:__',description = f'```py\n{e.__class__.__name__}: {e}\n```',color = color)
            
            return await ctx.reply(embed=embed,mention_author = False)
            await ctx.message.add_reaction(no)

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()

            embed = discord.Embed(description = f'```py\n{value}{traceback.format_exc()}\n```',color = color)
            await ctx.author.send(embed=embed,mention_author = False)
            await ctx.message.add_reaction(no)
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction(yes)
            except:
                pass

            if ret is None:
                if value:

                        embed = discord.Embed(title = "__Evaluation Done:__",description = f'```py\n{value}\n```',color = color)
                    
                        await ctx.reply(embed=embed,mention_author = False)

                else:
                    self._last_result = ret

                    embed = discord.Embed(title = "__Evaluation Done:__",description = f'```py\n{value}{ret}\n```',color = color)
                    await ctx.reply(embed=embed,mention_author = False)


    @commands.command()
    async def eval(self, ctx, lang: str, *,code: str): 

        body = self.cleanup_code(code)
        
        tio = await async_tio.Tio()
        pt = await tio.execute(body, language=lang)

        await ctx.reply(embed = discord.Embed(title = "Evaluation done.",description = f'```py\n{pt}\n```',color = color),mention_author = False)
        await tio.close()

# setting up cog class

def setup(bot):
    bot.add_cog(Owner(bot))