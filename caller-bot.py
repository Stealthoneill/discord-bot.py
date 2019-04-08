import discord

TOKEN = 'NTY0OTEwODQzOTMwNzM4Njg5.XKuwjA.cT9yJiBR2o0Kggb9eVAWSj6LHf0'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print("This bot is ready to go!")
    await client.change_presence(game=discord.Game(name="Making a bot"))


client.run(TOKEN)