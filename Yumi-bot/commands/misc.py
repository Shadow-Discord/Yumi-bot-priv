# imports discord

import discord
from discord.ext import commands

# other imports

import time
import datetime
from datetime import datetime
import asyncio

# variables

color = 0xECC1BA
yes = '<:greenTick:596576670815879169>'
no = '<:redTick:596576672149667840>'
ss = '<:member_join:596576726163914752>'
trashcan = '<:trashcan:846484978615058442>'
onlinest = '<:status_online:596576749790429200>'
offlinest = '<:status_offline:596576752013279242>'
dndst = '<:status_dnd:596576774364856321>'
idlest = '<:status_idle:596576773488115722>'
yees = '<:yes:597590985802907658>'
noo = '<:no:597591030807920660>'


# misc commands

class utils(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self.bot.user} | Utility cog loaded\n\n------------------\nLoggin Success\nConnected: {len(self.bot.users)}')

    @commands.Cog.listener('on_message')
    async def ping(self, message):

        if message.author == self.bot.user:
            return

        if message.guild == None:
            return

        if self.bot.user.mentioned_in(message):

            if message.content == self.bot.commands:
                return

            embed1 = discord.Embed(title = f':ping_pong: Ping pong',description = f'My prefixes are: `yumi`,`@Yumi`',color = color)

            await message.reply(embed=embed1,mention_author = False)

    @commands.command()
    @commands.cooldown(1, 10)
    async def source(self, ctx):
        await ctx.reply(embed = discord.Embed(description = '{} Im not open source dumb fuck.'.format(no),color = color),mention_author = False)    

    @commands.command()
    @commands.cooldown(1, 10)
    async def invite(self, ctx):
        inv = 'https://discordapp.com/api/oauth2/authorize?client_id=841321088445448212&permissions=1609952598&scope=bot'
        
        await ctx.reply(embed = discord.Embed(description = "{} You can [click here]({}) to invite yumi. <3".format(yes, inv),color = color),mention_author = False)

    @commands.command()
    @commands.cooldown(1, 10)
    async def ping(self, ctx):

        if ctx.guild == None:
            return

        start_time = time.time()

        embed = discord.Embed(title = 'Checking Latency...',color = color)
        message = await ctx.reply(embed=embed,mention_author = False)
        
        end_time = time.time()

        latency = f'```py\n{round(self.bot.latency * 1000)}ms\n```'
        api = f'```py\n{round((end_time - start_time) * 1000)}ms\n```'

        ping = discord.Embed(title = ':ping_pong: __Pong!__',color=color)

        ping.add_field(name = "**<:juice1:848578116866801674> | Bot's Latency**",value = f'{latency}',inline = True)
        ping.add_field(name = "**<:juice2:848578163332218911> | Api's Latency**",value = f'{api}',inline = True)

        ping.set_thumbnail(url = f'{self.bot.user.avatar_url}')
        
        await message.edit(embed=ping,mention_author = False)

    @commands.command()
    @commands.cooldown(1, 10)
    async def prefix(self, ctx):

        embed1 = discord.Embed(title = f':ping_pong: Ping pong',description = f'My prefixes are: `yumi`,`@Yumi`',color = color)

        await ctx.reply(embed=embed1,mention_author = False)

    @commands.command(aliases=['av'])
    @commands.cooldown(1, 10)
    async def avatar(self, ctx, member: discord.User = None):

        if ctx.guild == None:
            return

        if member is None:
            member = ctx.author

        embed = discord.Embed(title = f'{member}',description = f'[png]({member.avatar_url_as(format = "png")}) | [jpg]({member.avatar_url_as(format = "jpg")}) | [webp]({member.avatar_url_as(format = "webp")})',color = color)
        embed.set_image(url = member.avatar_url)

        msg = await ctx.reply(embed=embed,mention_author = False)
        await msg.add_reaction(trashcan)

        def check(reaction, user):
            return user == member and str(reaction.emoji) == trashcan

        try:
            reaction, user = await self.bot.wait_for("reaction_add",timeout = None,check = check)

        except asyncio.TimeoutError:
            return

        else:
            await msg.delete()
            await ctx.message.add_reaction(yes)

    @commands.command(aliases=['sav'])
    @commands.cooldown(1, 10)
    async def serveravatar(self, ctx):
        
        embed = discord.Embed(title = f'{ctx.guild}',description = f'[png]({ctx.guild.icon_url_as(format = "png")}) | [jpg]({ctx.guild.icon_url_as(format = "jpg")}) | [webp]({ctx.guild.icon_url_as(format = "webp")})',color = color)
        embed.set_image(url = ctx.guild.icon_url)

        msg = await ctx.reply(embed=embed,mention_author = False)
        await msg.add_reaction(trashcan)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == trashcan

        try:
            reaction, user = await self.bot.wait_for("reaction_add",timeout = None,check = check)

        except asyncio.TimeoutError:
            return

        else:
            await msg.delete()
            await ctx.message.add_reaction(yes)

    @commands.command(aliases=['bav'])
    @commands.cooldown(1, 10)
    async def botavatar(self, ctx):



        embed = discord.Embed(title = f'{self.bot.user}',description = f'[png]({self.bot.user.avatar_url_as("png")}) | [jpg]({self.bot.user.avatar_url_as(format = "jpg")}) | [webp]({self.bot.user.avatar_url_as(format = "webp")})',color = color)
        embed.set_image(url = self.bot.user.avatar_url)

        msg = await ctx.reply(embed=embed,mention_author = False)
        await msg.add_reaction(trashcan)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == trashcan

        try:
            reaction, user = await self.bot.wait_for("reaction_add",timeout = None,check = check)

        except asyncio.TimeoutError:
            return

        else:
            await msg.delete()
            await ctx.message.add_reaction(yes)


    @commands.command()
    @commands.cooldown(1, 10)
    async def serverinfo(self, ctx):

        embed = discord.Embed(title = f"__{ctx.guild.name}'s Info__",description = f'{ss} **Name**: {ctx.guild.name}\n{ss} **Id:** {ctx.guild.id}\n{ss} **Region:** {ctx.guild.region}\n{ss} **Channels:** {len(ctx.guild.text_channels)} | {len(ctx.guild.voice_channels)}\n{ss} **Members:** {len(ctx.guild.members)}',color = color)

        if ctx.guild == None:
            return

        if not ctx.guild.banner:
            
            embed.set_image(url = 'https://media.discordapp.net/attachments/559455534965850142/846491555711942656/unknown.png?width=1090&height=362')

        if ctx.guild.banner:

            embed.set_image(url = f'{ctx.guild.banner_url}')

        info = []
        features = set(ctx.guild.features)
        all_features = {
            'PARTNERED': 'Partnered',
            'VERIFIED': 'Verified',
            'DISCOVERABLE': 'Server Discovery',
            'COMMUNITY': 'Community Server',
            'FEATURABLE': 'Featured',
            'WELCOME_SCREEN_ENABLED': 'Welcome Screen',
            'INVITE_SPLASH': 'Invite Splash',
            'VIP_REGIONS': 'VIP Voice Servers',
            'VANITY_URL': 'Vanity Invite',
            'COMMERCE': 'Commerce',
            'LURKABLE': 'Lurkable',
            'NEWS': 'News Channels',
            'ANIMATED_ICON': 'Animated Icon',
            'BANNER': 'Banner'
        }

        for feature, label in all_features.items():
            if feature in features:
                info.append(f'{yes}: {label}')

        if info:
            embed.add_field(name='__Features:__', value='\n'.join(info))

        embed.set_thumbnail(url = f'{ctx.guild.icon_url}')
        embed.set_author(name = f'{ctx.author.name}',icon_url = f'{ctx.author.avatar_url}')
        embed.set_footer(text = f'Requested by {ctx.author.name} • {datetime.utcnow()}')

        await ctx.send(embed=embed)

    @commands.command(aliases=['ui'])
    @commands.cooldown(1, 10)
    async def userinfo(self, ctx, member: discord.Member = None):



        if member is None:
            member = ctx.author
        
        if member == self.bot.user:
            return

        inf  = []

        if member.bot:
            inf.append(f'{yes}')
        else:
            inf.append(f'{no}')

        final_info = '\n'.join(inf)

        joined = member.joined_at.strftime("%B %d, %Y, %I:%M %p")
        creation = member.created_at.strftime("%B %d, %Y, %I:%M %p")

        embed = discord.Embed(description = f"{ss} **Name:** {member.display_name}\n{ss} **Id:** {member.id}\n{ss} **Mutual:** {len(member.mutual_guilds)}\n{ss} **Bot:** {final_info}\n{ss} **Join Date:** {joined}\n{ss} **Creation Date:** {creation}",color = color)


        perms = ", ".join(k.replace("_", " ").title() for k,v in member.guild_permissions if v)

        embed.add_field(name = "__Member perms:__",value = f'```py\n{perms}\n```')


        embed.set_thumbnail(url = f'{member.avatar_url}')
        embed.set_author(name = f'{member}',icon_url = f'{member.avatar_url}')

        await ctx.reply(embed=embed,mention_author = False)

    @commands.command(aliases=['info','about','whoami'])
    @commands.cooldown(1, 10)
    async def botinfo(self, ctx):

        status = []

        if ctx.guild.me.status == discord.Status.online:
            status.append(onlinest)

        if ctx.guild.me.status == discord.Status.offline:
            status.append(offlinest)

        if ctx.guild.me.status == discord.Status.do_not_disturb:
            status.append(dndst)

        if ctx.guild.me.status == discord.Status.idle:
            status.append(idlest)

        final_stat = ' '.join(status)



        embed = discord.Embed(title = f"{final_stat} __Bot's Info:__",description = f"{ss} **Name:** {self.bot.user}\n{ss} **Id:** {self.bot.user.id}\n{ss} **Developer:** シャドー#8348\n{ss} **Library:** discord.py\n{ss} **Members:** {len(self.bot.users)}\n\n__**Credits**__\n{ss} Help command credits go to moonie, Dutchy",color = color)

        embed.set_thumbnail(url = f'{self.bot.user.avatar_url}')
        embed.set_author(name = f'{ctx.author}',icon_url = f'{ctx.author.avatar_url}')
        embed.set_image(url = 'https://media.discordapp.net/attachments/559455534965850142/846491555711942656/unknown.png?width=1090&height=362')
        embed.set_footer(text = f'Requested by: {ctx.author}')

        await ctx.reply(embed=embed,mention_author = False)

    @commands.command()
    @commands.cooldown(1, 10)
    async def roleinfo(self, ctx, role: discord.Role = None):

        if role is None:
            role = ctx.author.top_role

        embed = discord.Embed(description = f'{ss} **Role:** {role.mention}\n{ss} **Role Id:** {role.id}\n{ss} **Creation:** {role.created_at}\n{ss} **Color:** {role.color}'.format(ss, role),color = color)

        embed.set_author(name = ctx.author,icon_url = ctx.author.avatar_url)
        embed.set_thumbnail(url = ctx.guild.icon_url)
        embed.set_image(url = 'https://media.discordapp.net/attachments/559455534965850142/846491555711942656/unknown.png?width=1090&height=362')

        await ctx.reply(embed=embed,mention_author = False)

    @commands.command(aliases = ['perms'])
    @commands.cooldown(1, 10)
    async def permissions(self, ctx, member: discord.Member = None):

        if member is None:
            member = ctx.author

        perms = ", ".join(k.replace("_", " ").title() for k,v in member.guild_permissions if v)
        embed = discord.Embed(title = member,description = '```\n{}\n```'.format(perms),color = color)

        await ctx.reply(embed=embed,mention_author = False)

# setup the cog class

def setup(bot):
    bot.add_cog(utils(bot))
