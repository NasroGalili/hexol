import discord
from discord.ext import commands
client = commands.Bot(command_prefix ='.')

@client.event
async def on_ready():
    print('I am ready!')

    client.run(os.environ['BOT_KEY'])
