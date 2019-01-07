"""
####################################################################
SETUP CONFIG FILE FOR INITIALIING THE DISCORD BOT ON A LINUX SERVER
####################################################################
"""

try:
    import asyncio
    import discord
    from discord.ext.commands import Bot
    from discord.ext import commands
    import time
    import random
    import sys

except ImportError:
    print("Failure")
    sys.exit()

client = commands.Bot(command_prefix = ".")

###Insert your authentication code from discord below to login as your bot...
auth = ''

@client.event
async def on_ready():
    print("\n######################################################"
          "\nMrPens ready for duty! LET'S GO PTTSBURGH PENGUINS!!!!"
          "\n######################################################")

@client.command(pass_context=True)
async def nhl(ctx):
    await client.send_typing(ctx.message.channel)
    await client.send_message(ctx.message.channel, "I support Pittsburgh Penguins!")


client.run(auth)
