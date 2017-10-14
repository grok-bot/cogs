import discord
from discord.ext import commands

class Testing:
    def __init__(self, bot):
        self.bot = bot
       
    @commands.command()
    async def hi(self, ctx):
        await ctx.send('hello!')
        
def setup(bot):
	return bot.add_cog(Testing(bot))
