# discord imports

import discord
from discord.ext import commands

# other imports

import traceback
import random

# varibales 

color = 0xECC1ba
yes = '<:greenTick:596576670815879169>'
no = '<:redTick:596576672149667840>'
emoji = '<:redTick:596576672149667840> | ' 

# error handler

class ErrorH(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_command_error')
    async def error_hanler(self, ctx, error):
        
        ignored = (commands.CommandNotFound,)

        if isinstance(error, ignored):
            return

        if isinstance(error, commands.DisabledCommand):

            embed = discord.Embed(title = emoji + error.__class__.__name__,description = f'{ctx.command} is a disabled command.',color = color)
            
            await ctx.reply(embed=embed)

        elif isinstance(error, commands.CommandOnCooldown):

            embed = discord.Embed(title = emoji + error.__class__.__name__,description = f"You're on command cooldown, Retry after `{error.retry_after:.2f}` seconds.",color = color)

            await ctx.reply(embed=embed,mention_author = False)

        elif isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(title = emoji + error.__class__.__name__,description = f"{error.param} is a required argument that is missing.",color = color)

            await ctx.reply(embed=embed,mention_author = False)

        elif isinstance(error, commands.MissingPermissions):

            embed = discord.Embed(title = emoji + error.__class__.__name__,description = f"You're missing permissions to run {ctx.command}.",color = color)

            await ctx.reply(embed=embed,mention_author = False)

        elif isinstance(error, commands.BadArgument):

            embed = discord.Embed(title = emoji + error.__class__.__name__,description= f"{ctx.command} is a bad argument.",color = color)
            
            await ctx.reply(embed=embed,mention_author = False)

        elif isinstance(error, commands.NoPrivateMessage):

            embed = discord.Embed(title = emoji + error.__class__.__name__,description = f"{ctx.command} can't be used in a dm channel, Try in {random.choice(ctx.author.mutual_guilds)}. <3",color = color)

            await ctx.reply(embed=embed, mention_author = False)

        elif isinstance(error, commands.CheckFailure):
            return 

        elif isinstance(error, commands.TooManyArguments):

            embed = discord.Embed(title = emoji + error.__class__.__name__,description = f"You have passed to many arguments.",color = color)
            
            await ctx.reply(embed=embed, mention_author = False)
        
        else:
            etype = type(error)
            trace = error.__traceback__

            lines = traceback.format_exception(etype, error, trace)
            final_eror = ''.join(lines)

            embed = discord.Embed(description = f"```py\n{final_eror}\n```",color = color)

            shadow = self.bot.get_user(534403455201312793)
            await shadow.send(embed=embed)
            await ctx.message.add_reaction(no)

            raise error

# setup cog class

def setup(bot):
    bot.add_cog(ErrorH(bot))