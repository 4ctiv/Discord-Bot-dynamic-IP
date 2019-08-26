import discord
import GLOBALS  # Provide Variables

import requests  # Imports libary for ip

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is ready!")


@client.event
async def on_message(message):

#    id = client.get_guild(GLOBALS.serverId)

    if message.content == "-status":
        await message.channel.send("Everything is working fine!")

    if message.content == "-help":
        await message.channel.send("Commands: \n-help\n-status\n-ip")

    if message.content == "-ip":
        ip = requests.get('http://ip.42.pl/raw').text  # Gives the "public IP" of the Bot client PC
        await message.channel.send(ip)


client.run(GLOBALS.clientID)  # starts Bot
