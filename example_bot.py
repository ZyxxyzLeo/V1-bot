import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == ('ping'):
        await message.channel.send('pong')

client.run('OTA0MjEyNjIwNjYyNDExMjc3.YX4PoA.YbdxN-YtyWitFdXkqLKZoL6HPj8')
