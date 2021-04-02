import discord
import os
import requests
import io
import aiohttp
import asyncio
import logging
from mal import *

client = discord.Client()

@client.event 
async def on_ready(): 
  print ('Welcome to the Cult Bois {0.user}'.format(client))
  
newUserDMMessage = "WELCOME Fellow Weebs"

#Public Welcome
@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await client.send_message(member, newUserDMMessage)
    await client.send_message(discord.Object(id='CHANNELID'), 'Welcome!')
    print("Sent message to " + member.name)
    print("Sent message about " + member.name + " to #CHANNEL")

#Mod Leave Announcement
@client.event
async def on_member_remove(member):
    print("Recognized that " + member.name + " left")
    await client.send_message(discord.Object(id='CHANNELID'), '**' + member.mention + '** just left.')
    print("Sent message to #CHANNEL")





@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('Moshi'):
    await message.channel.send('Hi There!')
    await message.channel.send('https://play-lh.googleusercontent.com/sQ-dqWHr_OOXXdohI862USFJ6Wuq3kMMEFLsW6xwmUN0o7tzZLO6sl9mz0HCFAgoOaY')

  if message.content.startswith('Daisuki'):
    await message.channel.send('Hmmmm I like you too you know')
    await message.channel.send('https://danbooru.donmai.us/data/sample/sample-2038a8dd41ecead3f701f9ca764a26c6.jpg')
  
  if message.content.startswith('Thoughts about me'):
    await message.channel.send('You are special to me')
    await message.channel.send('https://i.imgur.com/5LEXOJi.jpg')
  
  if message.content.startswith('Are you free ?'):
    await message.channel.send('For you always,')
    await message.channel.send('https://i1.sndcdn.com/avatars-KrlczVU9XS0wyokr-Oni6nw-t500x500.jpg')
  
  if message.content.startswith('Cheer me up'):
    await message.channel.send('Are you feeling okay ?')
    await message.channel.send('https://static.wikia.nocookie.net/bakemonogatari1645/images/1/13/Nadeko1.png/revision/latest?cb=20161115034306')
  
  if message.content.startswith('You are cute'):
    await message.channel.send('What are you saying !')
    await message.channel.send('https://i.pinimg.com/originals/ac/72/1c/ac721cbdb486862d57573735c3f97bd9.gif')
  
  if message.content.startswith('Tell me about yourself'):
    await message.channel.send('Me, just a Waifu ')
    await message.channel.send('http://33.media.tumblr.com/dc55b48369cc36ce1d93a57eaa149159/tumblr_njuifnEVFm1timq39o1_500.gif')

  if message.content.startswith('Anything new'):
    await message.channel.send('Not really')
    await message.channel.send('https://i.pinimg.com/originals/7e/1d/20/7e1d200dad2c347b8f036d4e09d64584.gif')
    
client.run(os.getenv('TOKEN'))
