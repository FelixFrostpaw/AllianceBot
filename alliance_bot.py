from version import version
from secrets import required_api_key_name_string

import discord
from discord import app_commands
from discord.ext import commands

import gw2api
import gw2api_utils

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
async def version_command(interaction: discord.Interaction):
  await interaction.response.send_message(version, ephemeral=True)


@bot.tree.command(name="register")
@app_commands.describe(api_key="API Key")
async def register(interaction: discord.Interaction, api_key: str):
  api_key = api_key.strip()

  invalid_key_message = f"""Invalid Key. 
  A valid key must include the word "{required_api_key_name_string}" in its name, 
  and have the following permissions enabled: account, characters, guilds, and progression."""

  response = await gw2api.token_info(api_key)

  if not response["success"]:
    await interaction.response.send_message(invalid_key_message,
                                            ephemeral=True)
    return

  is_valid_key = gw2api_utils.valid_api_key(response["response"])

  if not is_valid_key:
    await interaction.response.send_message(invalid_key_message,
                                            ephemeral=True)
    return

  message = f"{interaction.user.name} has registered with the API Key: '{api_key}'"
  await interaction.response.send_message(message, ephemeral=True)
