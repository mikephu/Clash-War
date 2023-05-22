import discord
from discord.ext import commands

class Test(commands.Cog): 
  def __init__(self, bot):
      self.bot = bot

  # Ping
  @commands.slash_command(name="ping",description="Sends the bot's latency.") 
  @commands.is_owner()
  async def ping(self, ctx): 
      await ctx.respond(f"Pong! Latency is {self.bot.latency}")
  
  # Return all users in the server it is used 
  @commands.slash_command(name="users",description="List each server member.")
  @commands.is_owner()
  async def users(self, ctx):
     await ctx.respond(f"---{ctx.guild.name}: User List---")
     for member in ctx.guild.members: 
       await ctx.send(member)

  # List member roles
  @commands.slash_command(name="checkroles",description="List roles of each server member")
  @commands.is_owner()
  async def checkroles(self, ctx):
    await ctx.respond("vvv")
    for member in ctx.guild.members:
      await ctx.send(member.roles)
      
def setup(bot):
  bot.add_cog(Test(bot))