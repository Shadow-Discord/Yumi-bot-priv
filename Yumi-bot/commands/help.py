# imports

import discord
from discord.ext import commands,menus

# variables

color = 0xECC1BA
later = 'embed.add_field(name = "<:panck:850835622185009162>  Facts",value = "```\nyumi help facts\n```") embed.add_field(name = "<:panck2:850835599782969374> ...",value = "```\nyumi help ...\n```")'

# ext menus

class MyMenu(menus.Menu):
    async def send_initial_message(self, ctx, channel):

        embed = discord.Embed(description = "Use `yumi help [command]` for more info on a command.",color = color)

        embed.add_field(name = "<:muffin1:848312410779418644> Moderation",value = "```yaml\nyumi help moderation\n```")
        embed.add_field(name = "<:cake1:848312436700348417> Misc",value = "```yaml\nyumi help misc\n```")
        embed.add_field(name = "<:cake2:848312381029220372> Fun",value = "```yaml\nyumi help fun\n```",inline = False)
        embed.add_field(name = "<:cake3:849367739574780014> Images",value = "```yaml\nyumi help images\n```")
        embed.add_field(name = "<:panck:850835622185009162> Fact's",value = "```yaml\nyumi help facts\n```")

        embed.set_footer(text = "Use the reaction to go through all modules. <3")
        embed.set_author(icon_url = ctx.author.avatar_url, name = "Yumi's help menu")
        embed.set_image(url = "https://images-ext-1.discordapp.net/external/pXTQu_8CDlNEuvmlRz1IIaVig_zr6wMH4omZGOuDtgk/https/images-ext-2.discordapp.net/external/9e6dq4-OjHSHQd-pfmsfhPI4-Fue7sk5zg7ARi4FgTc/https/media.discordapp.net/attachments/381963689470984203/850704674239938570/unknown.png")
        
        return await channel.send(embed=embed)

    @menus.button('<:muffin1:848312410779418644>')
    async def on_muffin(self, payload):

        embed = discord.Embed(title = '__Moderation Module:__',color = color)

        embed.add_field(name = "Ban",value = "`yumi ban [member] <reason>`",inline = False)
        embed.add_field(name = "Unban",value = "`yumi unban [member-id] <reason>`",inline = False)
        embed.add_field(name = "Kick",value = "`yumi kick [member] <reason>`",inline = False)
        embed.add_field(name = "Lockdown",value = "`yumi lockdown <channel>`",inline = False)
        embed.add_field(name = "Unlock",value = "`yumi unlock <channel>`",inline = False)
        embed.add_field(name = "Mute",value = "`yumi mute [member] <time> <reason>`",inline = False)
        embed.add_field(name = "Unmute",value = "`yumi unmute [member] <reason>`",inline = False)
        embed.add_field(name = "Purge",value = "`yumi purge <amount>`",inline = False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)
        
        await self.message.edit(embed=embed)

    @menus.button('<:cake1:848312436700348417>')
    async def on_cake1(self, payload):
        
        embed = discord.Embed(title = '__Misc Module:__',color = color)

        embed.add_field(name = "Ping",value = "`yumi ping`",inline = False)
        embed.add_field(name = "Avatar",value = "`yumi avatar <member>`",inline = False)
        embed.add_field(name = "Server Avatar",value = "`yumi serveravatar`",inline = False)
        embed.add_field(name = "Bot Avatar",value = "`yumi botavatar`",inline = False)
        embed.add_field(name = "Server Information",value = "`yumi serverinfo`",inline = False)
        embed.add_field(name = "Member Information",value = "`yumi userinfo <member>`",inline = False)
        embed.add_field(name = "Bot Information",value = "`yumi botinfo`",inline = False)
        embed.add_field(name = "Role info",value = "`yumi roleinfo <role>`",inline = False)
        embed.add_field(name = "Permissions",value = "`yumi permissions <member>`",inline = False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)

        await self.message.edit(embed=embed)

    @menus.button("<:cake3:849367739574780014>")
    async def on_cake3(self, payload):
        
        embed = discord.Embed(title = '__Images Module:__',color = color)

        embed.add_field(name = "Hug",value = "`yumi hug <member>`",inline = False)
        embed.add_field(name = "Pat",value = "`yumi pat <member>`",inline = False)
        embed.add_field(name = "Triggered",value = "`yumi triggered <member>`",inline = False)
        embed.add_field(name = "Wasted",value = "`yumi wasted <member>`",inline = False)
        embed.add_field(name = "Gay",value = "`yumi gay <member>`",inline = False)
        embed.add_field(name = "Dog",value = "`yumi dog`",inline = False)
        embed.add_field(name = "Car",value = "`yumi cat`",inline = False)
        embed.add_field(name = "Panda",value = "`yumi panda`",inline = False)
        embed.add_field(name = "Bird",value = "`yumi bird`",inline = False)
        embed.add_field(name = "Waifu",value = "`yumi waifu`",inline = False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)

    @menus.button('<:cake2:848312381029220372>')
    async def on_cake2(self, payload):
        
        embed = discord.Embed(title = '__Fun Module:__',color = color)
        embed.add_field(name = "Meme",value = "`yumi meme`",inline = False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)
        await self.message.edit(embed=embed)

    @menus.button('<:panck:850835622185009162>')
    async def on_panck(self, payload):

        embed = discord.Embed(title = '__Facts Module (not out yet...):__',color = color)
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        
        await self.message.edit(embed=embed)

    @menus.button('<:trashcan:846484978615058442>')
    async def on_trash(self, payload):
        await self.message.delete()

# commands class

class Help(commands.Cog):
    def __init__(self, bot):
       self.bot = bot

    @commands.group(invoke_without_command = True)
    @commands.cooldown(1,10) 
    async def help(self, ctx):

        m = MyMenu()
        await m.start(ctx)

    @help.command()
    async def moderation(self, ctx):

        embed = discord.Embed(title = '__Moderation Module:__',color = color)

        embed.add_field(name = "Ban",value = "`yumi ban [member] <reason>`",inline = False)
        embed.add_field(name = "Unban",value = "`yumi unban [member-id] <reason>`",inline = False)
        embed.add_field(name = "Kick",value = "`yumi kick [member] <reason>`",inline = False)
        embed.add_field(name = "Lockdown",value = "`yumi lockdown <channel>`",inline = False)
        embed.add_field(name = "Unlock",value = "`yumi unlock <channel>`",inline = False)
        embed.add_field(name = "Mute",value = "`yumi mute [member] <time> <reason>`",inline = False)
        embed.add_field(name = "Unmute",value = "`yumi unmute [member] <reason>`",inline = False)
        embed.add_field(name = "Purge",value = "`yumi purge <amount>`",inline = False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)

        await ctx.reply(embed = embed,mention_author = False)

    @help.command()
    async def misc(self, ctx):

        embed = discord.Embed(title = '__Misc Module:__',color = color)

        embed.add_field(name = "Ping",value = "`yumi ping`",inline = False)
        embed.add_field(name = "Avatar",value = "`yumi avatar <member>`",inline = False)
        embed.add_field(name = "Server Avatar",value = "`yumi serveravatar`",inline = False)
        embed.add_field(name = "Bot Avatar",value = "`yumi botavatar`",inline = False)
        embed.add_field(name = "Server Information",value = "`yumi serverinfo`",inline = False)
        embed.add_field(name = "Member Information",value = "`yumi userinfo <member>`",inline = False)
        embed.add_field(name = "Bot Information",value = "`yumi botinfo`",inline = False)
        embed.add_field(name = "Role info",value = "`yumi roleinfo <role>`",inline = False)
        embed.add_field(name = "Permissions",value = "`yumi permissions <member>`",inline = False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)

        await ctx.reply(embed = embed,mention_author = False)

    @help.command()
    async def images(self, ctx):

        embed = discord.Embed(title = '__Images Module:__',color = color)

        embed.add_field(name = "Hug",value = "`yumi hug <member>`",inline = False)
        embed.add_field(name = "Pat",value = "`yumi pat <member>`",inline = False)
        embed.add_field(name = "Triggered",value = "`yumi triggered <member>`",inline = False)
        embed.add_field(name = "Wasted",value = "`yumi wasted <member>`",inline = False)
        embed.add_field(name = "Gay",value = "`yumi gay <member>`",inline = False)
        embed.add_field(name = "Dog",value = "`yumi dog`",inline = False)
        embed.add_field(name = "Car",value = "`yumi cat`",inline = False)
        embed.add_field(name = "Panda",value = "`yumi panda`",inline = False)
        embed.add_field(name = "Bird",value = "`yumi bird`",inline = False)
        embed.add_field(name = "Waifu",value = "`yumi waifu`",inline = False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)

        await ctx.reply(embed = embed,mention_author = False)

    @help.command()
    async def fun(self, ctx):

        embed = discord.Embed(title = '__Fun Module:__',color = color)
        embed.add_field(name = "Meme",value = "`yumi meme`",inline = False)

        embed.set_thumbnail(url = self.bot.user.avatar_url)

        await ctx.reply(embed = embed,mention_author = False)

    @help.command()
    async def facts(self, ctx):

        embed = discord.Embed(title = '__Facts Module (not out yet...):__',color = color)
        embed.set_thumbnail(url = self.bot.user.avatar_url)

        await ctx.reply(embed = embed,mention_author = False)

# setup cog class

def setup(bot):
    bot.add_cog(Help(bot))
