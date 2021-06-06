import discord
from discord.ext import commands

import json 
import os

# config.json

with open('./utils/yumi.json', 'r') as yumijson:
    config = json.load(yumijson)

# intents

intents = discord.Intents.default()
intents.members = True
intents.presences = True

#prefix/jsk


bot = commands.Bot(command_prefix = commands.when_mentioned_or('yumi ','yumi','Yumi ','Yumi'),intents = intents, case_insensitive = True,activity=discord.Activity(type=discord.ActivityType.listening, name="yumi help | love you <3"), status = discord.Status.idle)
bot.remove_command('help')
bot.load_extension('jishaku')
os.environ["JISHAKU_NO_UNDERSCORE"] = "True"

# logging in

if __name__ == '__main__':
    
    for filename in os.listdir("./commands"):
        if filename.endswith(".py") and not filename.startswith("_"):
            bot.load_extension(f"commands.{filename[:-3]}")

    bot.run(config["token"], reconnect=True)