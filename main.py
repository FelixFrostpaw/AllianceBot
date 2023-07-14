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

@bot.tree.command(name="version")
async def version(interaction: discord.Interaction):
  await interaction.response.send_message(__version__, ephemeral=True)

@bot.tree.command(name="repeat")
@app_commands.describe(thing_to_say = "What should I say?")
async def repeat(interaction: discord.Interaction, thing_to_say: str):
  await interaction.response.send_message(f"{interaction.user.name} said '{thing_to_say}'")

bot.run(__discord_bot_token__)
