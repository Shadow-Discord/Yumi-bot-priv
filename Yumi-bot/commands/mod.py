# importing 

import discord
from discord.ext import commands

# other imports

import time
from datetime import datetime
import asyncio
import re
import sys
import traceback

# variables 

color = 0xECC1BA
yes = '<:greenTick:596576670815879169>'
no = '<:redTick:596576672149667840>'
time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h":3600, "s":1, "m":60, "d":86400}

# time convert

class TimeConverter(commands.Converter):
    async def convert(self, ctx, argument):
        args = argument.lower()
        matches = re.findall(time_regex, args)
        time = 0
        for v, k in matches:
            try:
                time += time_dict[k]*float(v)
            except KeyError:
                raise commands.BadArgument("{} is an invalid time-key! h/m/s/d are valid!".format(k))
            except ValueError:
                raise commands.BadArgument("{} is not a number!".format(v))
        return time

# cog commands class

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} | Mod cog loaded')

    @commands.command(description = 'Bans a member from guild.')
    @commands.bot_has_permissions(ban_members=True)
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, member: discord.Member = None, *,reason = 'Reason for ban was not provided...'):

        if ctx.author.top_role <= member.top_role:
            await ctx.reply(embed = discord.Embed(description = f"{no} You can't ban someone higher than you.",color = color),mention_author = False)

        await member.send(embed=discord.Embed(description = '{} You have been banned from {}'.format(no, ctx.guild),color = color),mention_author = False)
        await member.ban(reason=reason)

        await ctx.reply(embed=discord.Embed(description = '{} I have banned {}'.format(yes, member),color = color),mention_author = False)

    @commands.command(description = 'Unbans member from guild.')
    @commands.bot_has_permissions(ban_members = True)
    @commands.has_guild_permissions(ban_members = True)
    async def unban(self, ctx, id: int, *,reason = 'Reason was not provided for kick'):
        
        user = discord.Object(id = id)
        await ctx.guild.unban(user, reason = reason)

        await ctx.reply(embed = discord.Embed(description = '{} I have unabnned {}'.format(yes, user.name),color = color),mention_author = False)

    @commands.command(description = 'Kicks member from guild.')
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_guild_permissions(kick_members = True)
    async def kick(self, ctx, member: discord.Member, *,reason = None):

        if ctx.author.top_role <= member.top_role:
            await ctx.reply(embed = discord.Embed(description = "{} You can't kick a member higher than you.".format(yes),color = color),mention_author = False)

        await member.send(embed=discord.Embed(description = "{} You have been kicked from {}".format(member, ctx.guild),color = color),mention_author = False)
        await member.kick(reason=reason)

        await ctx.reply(embed=discord.Embed(description = "{} I have kicked {}".format(yes, member.name),color = color),mention_author = False)

    @commands.command(description = 'Locks a guild channel.')
    @commands.bot_has_permissions(manage_channels = True)
    @commands.has_guild_permissions(manage_channels = True)
    async def lockdown(self, ctx, channel: discord.TextChannel = None):

        if channel is None:
            channel = ctx.channel

        await channel.set_permissions(ctx.guild.default_role, send_messages = False)
        await ctx.reply(embed = discord.Embed(description = "{} I have locked {}".format(yes, channel.mention),color = color),mention_author = False)

    @commands.command(description = 'Unlocks a guild channel.')
    @commands.has_guild_permissions(manage_channels = True)
    @commands.bot_has_permissions(manage_channels = True)
    async def unlock(self, ctx, channel: discord.TextChannel = None):

        if channel is None:
            channel = ctx.channel

        await channel.set_permissions(ctx.guild.default_role, send_messages = True)
        await ctx.reply(embed = discord.Embed(description = "{} I have unlocked {}".format(yes, channel.mention),color = color),mention_author = False)

    @commands.command(description = 'Mutes a member from guild.')
    @commands.bot_has_permissions(mute_members = True)
    @commands.has_permissions(manage_channels = True)

    async def mute(self, ctx, member:discord.Member, *, time:TimeConverter = None):

        role = discord.utils.get(ctx.guild.roles, name="Muted")

        if role is None:
            role = ctx.guild.create_role(name = "Muted")
        
        await member.add_roles(role)
        await ctx.reply(embed = discord.Embed(description = "{} I have muted member for {}'s" if time else "{} I have muted {}".format(member, time),color = color),mention_author = False)
        
        if time:
            await asyncio.sleep(time)
            await member.remove_roles(role)

    @commands.command(description = 'Unmutes a member from guild.')
    @commands.bot_has_permissions(mute_members = True)
    @commands.has_permissions(manage_channels = True)
    async def unmute(self, ctx, member: discord.Member = None,reason = 'Reason was not provided for unmute...'):

        if ctx.author.top_role <= member.top_role:
            await ctx.reply(embed = discord.Embed(description = "{} you can't unmute someone higher than you.".format(no),color = color),mention_author = False)

        role = discord.utils.get(ctx.guild.roles, name="Muted")
        await member.remove_roles(role)

        await ctx.reply(embed = discord.Embed(description = "{} I have unmuted {}".format(yes, member),color = color),mention_author = False)

    @commands.command(description = 'Purges a curtain amount of messages.')
    @commands.bot_has_permissions(manage_channels = True)
    @commands.has_guild_permissions(manage_channels = True)
    async def purge(self, ctx, *, amount = None):

        if amount > 500:
            return await ctx.reply(embed = discord.Embed(description = "{} You can't purge more than 500 messages.".format(no),color = color),mention_author = False)

        else:
            await ctx.channel.purge(limit = amount+1)

    @commands.command(description = 'Sets channels slowmode.')
    @commands.bot_has_permissions(manage_channels = True)
    @commands.has_guild_permissions(manage_channels = True)
    async def slowmode(self, ctx, *,slowmode: int):

        await ctx.channel.edit(slowmode_delay = slowmode)
        await ctx.message.add_reaction(yes)

# setting up cog class

def setup(bot):
    bot.add_cog(Moderation(bot))