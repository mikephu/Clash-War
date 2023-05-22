import os 
import discord
import requests 
import logging
from discord.ext import commands 
import asyncio
from app import keep_alive


def main():
  
  # Loading bot token + cog names
  bot_token = os.environ['DISCORD_TOKEN']
  cogs = ['cogs.clash','cogs.test']
  
  # Enabling intents and creating the client.
  intents = discord.Intents().all()
  bot = commands.Bot(intents=intents)
  
  # Loading Cogs 
  for cog in cogs:
    bot.load_extension(cog)
  
  # Starting thread and bot 
  keep_alive()
  bot.run(bot_token)

if __name__ == '__main__':
  main()




# # COMMAND: 
# # Adds the role 'X' to a member
# @bot.command()
# @commands.bot_has_permissions(manage_roles=True)
# async def addrole(ctx, member: discord.Member):
#     await ctx.send(member)
#     role = discord.utils.find(lambda r: r.name == 'X', ctx.guild.roles)
#     await member.add_roles(role)

# # Command: CWL
# # Sends an embed to check if obtain a user response
# @bot.command()
# async def cwl(ctx):
#   embed = discord.Embed(title="Clan War League Check-in", color=0x00ff00)
#   embed.add_field(name="----------------------",value="Set War Status",inline=True)
#   cwl = await ctx.channel.send(embed=embed)
#   await cwl.add_reaction("✅")
#   await cwl.add_reaction("❌")

# # Command: CWL_Reset
# @bot.command()
# async def cwlreset(ctx):
#   hasAttacked = discord.utils.find(lambda r: r.name == 'CW ✓', ctx.guild.roles)
#   hasNotAttacked = discord.utils.find(lambda r: r.name == 'CW X', ctx.guild.roles)
#   for member in ctx.guild.members:
#     if not member.bot:
#       await member.add_roles(hasNotAttacked)
#       await member.remove_roles(hasAttacked)
#   await ctx.channel.send("Reset Completed")

# # Command: War_List
# @bot.command()
# async def warlist(ctx): 
#   embed = discord.Embed(title="WAR CHECKLIST",description="-------------------------",color=0x0000FF)
  
#   hasAttacked = discord.utils.find(lambda r: r.name == 'CW ✓', ctx.guild.roles)
#   userRoles = []

#   for member in ctx.guild.members:
#     if not member.bot:
#       uName = member.name

#       for role in member.roles:
#         userRoles.append(role.name)

#       if hasAttacked.name in userRoles:
#         string = uName + "    ✓"
#         embed.add_field(name=string,value="---",inline=False)
#       else:
#         string = uName + "    X"
#         embed.add_field(name=string,value="---",inline=False)

#       userRoles = []

#   await ctx.channel.send(embed=embed)

# @bot.command()
# async def remind(ctx):

#   hasAttacked = discord.utils.find(lambda r: r.name == 'CW ✓', ctx.guild.roles)
#   userRoles = []

#   for member in ctx.guild.members:

#     for role in member.roles:
#       userRoles.append(role.name)

#     if hasAttacked.name not in userRoles:
#       await member.send("You have not attacked in war yet!")

#     userRoles.clear() # Reset

#---Events--- 

# @bot.event 
# async def on_message(message):
#   if message.author == bot.user:
#     return 

#   if message.content.startswith('help'):
#     embed = discord.Embed(title="Command List", color=0xFF0000)
#     embed.add_field(name="----------------------",value="\n$cwl - Asks if you have attacked\n\n$cwlreset - Reset for a new war day\n\n$warlist - Shows war status\n\n$nic - Notifies nic",inline=True)
#     channel = message.channel
#     await channel.send(embed=embed)
#   await bot.process_commands(message)

# @bot.event  
# async def on_reaction_add(reaction, user):  
#   channel = reaction.message.channel
#   if not user.bot and reaction.emoji == "✅":
#     userRoles = []
#     hasAttacked = discord.utils.find(lambda r: r.name == 'CW ✓', channel.guild.roles)
#     hasNotAttacked = discord.utils.find(lambda r: r.name == 'CW X', channel.guild.roles)
#     for role in user.roles:
#       userRoles.append(role.name)
#     if hasAttacked.name not in userRoles:
#       await user.add_roles(hasAttacked)
#       await user.remove_roles(hasNotAttacked)
#   else:
#     await user.send("Reminder Placeholder")

