import discord
from discord.ext import commands
import random
import string
import datetime
import calendar
import time
import numpy
import base64
import math
from math import modf
def randomstr(l):
    strlength = l
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(strlength))
Cog = discord.ext.commands.Cog
defcolor = 0xff0000
def getainid(timestamp):
    timestr = str(timestamp)
    timelen = len(timestr)
    timeintf = int(timestr)
    finishedres = timeintf*timelen
    return finishedres
class General(Cog):
    def __init__(self,bot):
        self.bot = bot
    print("General cogs loaded")

    @commands.command()
    async def help(self,ctx):
        emoji = "✔️"
        await ctx.message.add_reaction(emoji)
        embed = discord.Embed(title="Help", color=defcolor)
        embed.add_field(name="General", value="help, ping, randomstring [length], giverole [user] [role], removerole [user] [role], createinv [needs perms], generateid (generates ainID using algorithm), ain base64 [encode,decode] [text to encode/decode]", inline=False)
        embed.add_field(name="Fun", value="yesmeter", inline=False)
        embed.set_footer(text="Made by aindrigo#8038 on discord. IN PRE-ALPHA")
        await ctx.send(embed=embed)

    @commands.command(pass_Context=True, aliases=['b64', '64b', 'base'])
    async def base64(self,ctx,choice,string):
        if choice == "encode":
            message = string
            message_bytes = message.encode('utf-8')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('utf-8')
            await ctx.send(base64_message)
        if choice == "decode":
            base64_message2 = string
            base64_bytes2 = base64_message2.encode('utf-8')
            message_bytes2 = base64.b64decode(base64_bytes2)
            message2 = message_bytes2.decode('utf-8')
            await ctx.send(message2)

        
    @commands.command()
    async def generateid(self,ctx):
        ts = calendar.timegm(time.gmtime())
        await ctx.send(str(getainid(ts)))
    @commands.command(pass_Context=True)
    async def randomstring(self,ctx,length):
        if int(length) > 2000:
            await ctx.send("Discord at the moment doesn't support messages over 2000 letters. I am working on a bypass for this (includes some math if you wanna know).")
        await ctx.send(randomstr(l=int(length)))

    @commands.command()
    async def ping(self,ctx):
        embed = discord.Embed(title="Ping!", description=":ping_pong: Ping! " + str(self.bot.latency) + "ms.", color=defcolor)
        await ctx.send(embed=embed)

    @commands.command(pass_Context=True)
    @commands.has_permissions(administrator=True)
    async def giverole(self,ctx,user:discord.Member,role:discord.Role):
        try:
            await user.add_roles(role)
            await ctx.send("Role given!")
        except commands.errors.BadArgument:
            ctx.send("User or role doesn't exist.")
    @commands.command(pass_Context=True)
    @commands.has_permissions(administrator=True)
    async def removerole(self,ctx,user:discord.Member,role:discord.Role):
        try:
            await user.remove_roles(role)
            await ctx.send("Role removed!")
        except commands.errors.BadArgument:
            ctx.send("User or role doesn't exist.")
    @commands.command()
    async def createinv(self,ctx):
        link = await ctx.channel.create_invite()
        await ctx.send(link)

def setup(bot):
    bot.add_cog(General(bot=bot))
