import discord
from discord.ext import commands
import importlib
import sys
import time
import calendar
import util

token = "YOUR TOKEN HERE"
bot = commands.Bot(command_prefix="ain ")
bot.remove_command("help")
defcolor = 0xffffff
import cogs.general
from cogs.general import General
import cogs.dev
from cogs.dev import Dev
ts = calendar.timegm(time.gmtime())
def getainid(timestamp):
    timestr = str(timestamp)
    timelen = len(timestr)
    timeintf = int(timestr)
    finishedres = timeintf*timelen
    return finishedres
launchedwith = str(getainid(timestamp=ts))
@bot.event
async def on_ready():
    print("Bot is on, launched with id")
    print(launchedwith)
@bot.event
async def on_command_error(ctx,err):
    embed = discord.Embed(title="Uh oh! An error occured.", description="The following error occured: ```" + str(err) + "```")
    await ctx.send(embed=embed)
bot.add_cog(Dev(bot=bot))
bot.run(token)
