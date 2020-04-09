import discord
from discord.ext import commands
import json
Cog = commands.Cog

jfile = json.loads("data.json")
class Level(Cog):
    





def setup(bot):
    bot.add_cog(Level(bot=bot))
