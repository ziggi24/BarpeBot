import botToken
import sys
import random
import discord
import asyncio
import datetime
from datetime import timedelta
import urllib
import urllib.request
import urllib.error
from discord.ext.commands import Bot
from discord.ext import commands
from bs4 import BeautifulSoup


client = Bot(description="BarpeBot", command_prefix="!", pm_help = True)

anniversary = datetime.date(2017, 2, 14)

@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Use this link to invite {}:'.format(client.user.name))
	print('https://discordapp.com/oauth2/authorize?client_id={}&scope=bot&permissions=8'.format(client.user.id))
	print('--------')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    elif message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1
        await client.edit_message(tmp, 'You have {} messages.'.format(counter))

    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

    elif message.content.startswith('!kiss'):
        await  client.send_message(message.channel, ':smooch:')

    elif message.content.startswith('!hey'):
        msg = 'Hey {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!help'):
        await client.send_message(message.channel, 'Well hey there! \n' +
        'You can command me by typing messages with a ! in front. \n' +
        'Try typing !hey, !test, or !kiss to see what they do!')

    elif message.content.startswith('!howlong'):
        timeSince = datetime.date.today() - anniversary
        time = str(timeSince).split(',')
        await client.send_message(message.channel, "The Barpes have been together for " +
        time[0])


client.run(botToken.getCode())
