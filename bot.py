import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import random
from dnd_api_client import *


load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.command(name='roll', help='Roll a DnD die. Usage: !roll [number of sides]')
async def roll(ctx, sides=6):
	if sides <= 0:
		await ctx.send("Number of sides must be greater than 0.")
		return
	
	await ctx.send(random.randint(1,sides))
	

@bot.command(name='classes', help='List all DnD classes. Usage: !classes')
async def print_classes(ctx):
	await ctx.send('\n'.join(get_classes()))


@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("DnD Bot is in " + str(guild_count) + " guilds.")


bot.run(DISCORD_TOKEN)