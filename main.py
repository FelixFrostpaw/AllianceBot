from version import __version__
from secrets import __discord_bot_token__

import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())


@bot.event
async def on_ready():
  print("Starting Bot")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)


@bot.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
  await interaction.response.send_message("pong!", ephemeral=True)


@bot.tree.command(name="version")
async def version(interaction: discord.Interaction):
  await interaction.response.send_message(__version__, ephemeral=True)


bot.run(__discord_bot_token__)
