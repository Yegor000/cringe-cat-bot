import discord
import random

TOKEN = 'MTA3MjYxNjg3OTEzMjI1MDI4Mw.GOklvB.OESUe5ZZJFZCXcjY7SxH9m61JcC2S-zlKE6hYU'
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'{client.user} is now running!')

@client.event
async def on_message(message):
    if message.author == client.user:
         return

    print('message received!')

    if message.content.startswith('пошутите'):
        randomFile = discord.File('cringes\cringe' + str(random.randint(0,99)) + '.webp')
        await message.channel.send(file = randomFile)

client.run(TOKEN)