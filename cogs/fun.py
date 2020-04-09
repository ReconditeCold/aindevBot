import discord
from discord.ext import commands
import random
import datetime
from random import randint
Cog = commands.Cog
defcolor = 0xff0000
__name__ = "Fun"

class Fun(Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command(pass_Context=True)
    async def yesmeter(self,ctx):
        await ctx.send(str(randint(1,100)) + " percent yes.")


def setup(bot):
    bot.add_cog(Fun(bot=bot))
