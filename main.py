from version import __version__
from secrets import __discord_bot_token__

import discord
from discord import app_commands
from discord.ext import commands

import gw2api

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
  print("Starting Bot")
  try:
    synced = await bot.tree.sync()
    print(f"Synced {len(synced)} command(s)")
  except Exception as e:
    print(e)

@bot.tree.command(name="version")
async def version(interaction: discord.Interaction):
  await interaction.response.send_message(__version__, ephemeral=True)

@bot.tree.command(name="register")
@app_commands.describe(api_key="API Key")
async def register(interaction: discord.Interaction, api_key: str):
  api_key = api_key.strip()

  await gw2api.token_info(api_key)
  
  message = f"{interaction.user.name} has registered with the API Key: '{api_key}'"
  await interaction.response.send_message(message, ephemeral=True)

bot.run(__discord_bot_token__)
