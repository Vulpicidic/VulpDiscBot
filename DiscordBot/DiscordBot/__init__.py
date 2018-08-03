import discord
from discord.ext import commands

import chatCommands
import settings.config 


bot = commands.Bot("!")

@bot.event
async def on_ready():
    print("Vulpicidic Bot engaged.")
    

@bot.command(pass_context=True)
async def commands(ctx):
    await bot.say(chatCommands.getHelp())


@bot.command(pass_context=True)
async def coin(ctx):
    await bot.say(chatCommands.getCoinFlip())
    
@bot.command(pass_context=True)
async def roll(ctx, *args):
    await bot.say(chatCommands.getDiceRoll(*args))

    
@bot.command(pass_context=True)
async def kill(ctx):
    await bot.close()

bot.run(settings.config.TOKEN)