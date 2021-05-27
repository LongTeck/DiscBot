import os
import random
from discord import embeds
import requests
import discord
from discord.ext import commands
from discord_slash import SlashCommand

bot = commands.Bot(command_prefix='>')
slash = SlashCommand(bot, sync_commands=True)


#This event is run when this app is connected to the discord servers!
@bot.event
async def on_ready():
    print("Logged in as {}".format(bot.user))



#Ping Command





#Repeat after me command





#Play Rock Paper Scissors
#Algorithm info: https://learningpenguin.net/2020/02/06/
emojis = [u"\U0001f5ff", u"\U0001f4f0", u"\u2702"]





#Slash Commands





#Combining APIs!





#Music Bot!





try:
    bot.run(open("Token.txt", 'r').readline())
except:
    print("Please ensure there's a Token.txt file!!")
