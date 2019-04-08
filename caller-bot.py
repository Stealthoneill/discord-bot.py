import discord

client = discord.Client()

@client.event
async def on_ready():
    print("This bot is ready to go!")
    await client.change_presence(game=discord.Game(name="Making a bot"))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "World")



        client.run('NTY0OTEwODQzOTMwNzM4Njg5.XKuwjA.cT9yJiBR2o0Kggb9eVAWSj6LHf0')