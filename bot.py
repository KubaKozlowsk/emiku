# bot.py
import os

import discord

import asyncio

import random

import time

from dotenv import load_dotenv

from discord.ext import commands

from discord.ext.commands import Bot

client=commands.Bot(command_prefix="epic ")

load_dotenv()
TOKEN = '*************'
GUILD = 'EmeryciGaming'
#setup

intents = discord.Intents.all()
client = discord.Client(intents=intents)
########################################################################

aslist=["as1.png", "as2.png ", "as3.png", "as4.png", "as5.png"]
milist=["mi1.png", "mi2.png", "mi3.png", "mi4.png", "mi5.png", ]

#obrazki
@client.event
async def on_message(message):
    if message.content.lower() == ("epic emeryt"):
        await message.channel.send('', file=discord.File('emeryt.png'))
    elif message.content.lower() == ("epic bunia 1"):
        await message.channel.send('', file=discord.File('bunia1.png'))
    elif message.content.lower() == ("epic bunia 2"):
        await message.channel.send('', file=discord.File('bunia2.png'))
    elif message.content.lower() == ("epic stachu 1"):
        await message.channel.send('', file=discord.File('stachu1.png'))
    elif message.content.lower() == ("epic stachu 2"):
        await message.channel.send('', file=discord.File('stachu2.png'))
    elif message.content.lower() == ("epic kubus"):
        await message.channel.send('', file=discord.File('kubus.png'))
    elif message.content.lower() == ("epic pilot"):
        await message.channel.send('', file=discord.File('pilot.png'))
    elif message.content.lower() == ("epic zle"):
        await message.channel.send('', file=discord.File('zle.png'))
    elif message.content.lower() == ("epic grziby"):
        await message.channel.send('', file=discord.File('grziby.png')) 

#poke
#poke kubus
    elif message.content.lower() == ("poke kubus"):
          await message.channel.send("<@478611869310124032> 1")
          await message.channel.send("<@478611869310124032> 2")
          await message.channel.send("<@478611869310124032> 3")
          await message.channel.send("<@478611869310124032> 4")
          await message.channel.send("<@478611869310124032> 5")
          
#poke bunia
    elif message.content.lower() == ("poke bunia"):
          await message.channel.send("<@341569153930493952> 1")
          await message.channel.send("<@341569153930493952> 2")
          await message.channel.send("<@341569153930493952> 3")
          await message.channel.send("<@341569153930493952> 4")
          await message.channel.send("<@341569153930493952> 5")
          
#poke stachu
    elif message.content.lower() == ("poke stachu"):
          await message.channel.send("<@314850261841477634> 1")
          await message.channel.send("<@314850261841477634> 2")
          await message.channel.send("<@314850261841477634> 3")
          await message.channel.send("<@314850261841477634> 4")
          await message.channel.send("<@314850261841477634> 5")

#nsfw

    elif message.content.lower() == ("epic as"):
        await message.channel.send('Here, take some as', file=discord.File(random.choice(aslist)))
    elif message.content.lower() == ("epic mi"):
        await message.channel.send('Here, take some mi', file=discord.File(random.choice(milist)))

#odpowiedzi na wiadomosci
    elif ((" kys") in message.content.lower()) or (("kys ") in message.content.lower()) or (message.content.lower() == ("kys")):
        await message.channel.send("oj nieładnie")
        await message.channel.send("przeproś")
        await message.channel.send(message.author.mention + " bandyto")
    elif ((" serwus") in message.content.lower()) or (("serwus ") in message.content.lower()) or (message.content.lower() == ("serwus")):   
        await message.channel.send("suwres")
        await message.channel.send(message.author.mention + "")

#clear
    elif message.content.lower() == ("epic clear"):
        await message.channel.purge(limit=5)

#help
    elif message.content.lower() == ("epic pomoc"):       
        embed = discord.Embed(title="Lista komend")         
        embed.add_field(name="epic emeryt",          value="\u200b")
        embed.add_field(name="epic bunia 1",         value="\u200b")
        embed.add_field(name="epic bunia 2",         value="\u200b")
        embed.add_field(name="epic stachu 1",        value="\u200b")
        embed.add_field(name="epic stachu 2",        value="\u200b")
        embed.add_field(name="epic kubus",           value="\u200b")
        embed.add_field(name="epic pilot",           value="\u200b")
        embed.add_field(name="epic zle",           value="\u200b")
        embed.add_field(name="epic grziby",          value="\u200b")
        embed.add_field(name="poke kubus",           value="\u200b")
        embed.add_field(name="poke bunia",           value="\u200b")
        embed.add_field(name="poke stachu",          value="\u200b")
        embed.add_field(name="epic as",             value="\u200b")
        embed.add_field(name="epic mi",            value="\u200b")
        embed.add_field(name="epic clear",           value="\u200b")
        await message.channel.send(content=None, embed=embed)   
#######################################################################
#members list
@client.event
async def on_ready():
   await client.change_presence(activity=discord.Game("epic pomoc"))
   for guild in client.guilds:
       if guild.name == GUILD:
           break

   print(
       f'{client.user} is connected to the following guild:\n'
       f'{guild.name}(id: {guild.id})\n'
   )

   members = '\n - '.join([member.name for member in guild.members])
   print(f'Guild Members:\n - {members}')

   print(discord.VoiceChannel.name)

client.run(TOKEN)