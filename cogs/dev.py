import discord
from discord.ext import commands
import datetime
import sys
import os
from os import walk
def getainid(timestamp):
    timestr = str(timestamp)
    timelen = len(timestr)
    timeintf = int(timestr)
    finishedres = timestr * timelen
    return finishedres
print("Developer cogs loaded")
Cog = commands.Cog
__name__ = "Developer Cogs"

class Dev(Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_Context=True)
    async def load(self,ctx,cogtoload):
        if ctx.message.author.display_name == "aindrigo":
            self.bot.load_extension(cogtoload)
            print("Loaded {}.".format(cogtoload))
            await ctx.send("Cog loaded.")
    @commands.command(pass_Context=True)
    async def unload(self,ctx,cogtoload):
        if ctx.message.author.display_name == "aindrigo":
            self.bot.unload_extension(cogtoload)
            print("Unloaded {}".format(cogtoload))
            await ctx.send("Cog unloaded.")

    @commands.command(pass_Context=True)
    async def refreshcog(self,ctx,cogtoreload):
        if ctx.message.author.display_name == "aindrigo":
            self.bot.unload_extension(cogtoreload)
            self.bot.load_extension(cogtoreload)
            print("Reloaded {}".format(cogtoreload))
            await ctx.send(f"Cog {cogtoreload} reloaded")

    @commands.command(pass_Context=True)
    async def exec(self,ctx,execscr):
        if ctx.message.author.display_name == "aindrigo":
            exec(execscr)
            await ctx.send("Executed")
        else:
            await ctx.send("You do not have permission to use this command.")
    @commands.command()
    async def stop(self,ctx):
        if ctx.message.author.display_name == "aindrigo":
            await ctx.send("Bot shut down.")
            sys.exit()
        else:
            await ctx.send("Don't try it hun")
    @commands.command()
    async def cogs(self,ctx):
        if ctx.message.author.display_name == "aindrigo":
            res = os.listdir("/var/discord/cogs")
            await ctx.send(res)
def setup(bot):
    bot.add_cog(Dev(bot=bot))
