import os
import requests
import discord
from discord.ext.commands import Context, slash_command, Cog

class Clash(Cog):
  def __init__(self, bot):
    self.bot = bot
    self.header = {"Authorization":"Bearer " + os.environ['API_TOKEN']}

  """
  # Slash Commands
  """

  @slash_command(name="help",description="List of commands.")
  async def help(self, ctx: Context):
    embed = discord.Embed(title="Command List", color=0xFF0000)
    embed.add_field(name="/nic",value="Shows you a juicy pic", inline=True)
    await ctx.respond(embed=embed)
  
  @slash_command(name="nic",description="Sends a pic of nic.")
  async def nic(self, ctx: Context):
    embed = discord.Embed(url='https://www.youtube.com/watch?v=T5jip2vvI8s&ab_channel=Mica28-Topic')
    embed.set_image(url='https://i.imgur.com/9ythM6n.png')
    await ctx.respond(embed=embed)

  @slash_command(name="clan",description="Returns clan information.")
  async def clan(self, ctx: Context):
    try: 
      response = requests.get('https://api.clashofclans.com/v1/clans/%232L8UYLVG9', headers=self.header)
    except:
      print("Error has occured")
      
    await ctx.respond(response)
    
  """
  # Event Listeners 
  """
  
  @Cog.listener()
  async def on_ready(self):
    print('Clash War Online')

def setup(bot):
  bot.add_cog(Clash(bot))

# Clan Tag: #2L8UYLVG9

""" 
session = requests.Session()
  session.headers.update(header)
  response = session.get('https://api.clashofclans.com/v1/clans?name=AWESOMECLASHER')
  # response = requests.get('https://api.clashofclans.com/v1/clans?name=AWESOMECLASHER',headers=header)
  print(response.json())
"""