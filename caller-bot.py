import discord
import random

TOKEN = 'NTY0OTEwODQzOTMwNzM4Njg5.XKu-Bg.r0AKB7QWEsIkVlcK2l921wi5FPQ'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!roll'):
        print("You rolled for a {}").format(random.randint(1,20))
        await client.send_message(message.channel)

@client.event
async def on_ready():
    print("This bot is ready to go!")
    await client.change_presence(game=discord.Game(name="Hanging Around"))


client.run(TOKEN)