import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import traceback
import sys

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Create a bot instance
bot = commands.Bot(command_prefix='!')

# Function to load cogs
def load_cog(extension):
    try:
        bot.load_extension(f'cogs.{extension}')
        print(f'Loaded extension: {extension}')
    except Exception as e:
        print(f'Failed to load extension {extension}.')
        traceback.print_exc()

# Load all cogs from the 'cogs' directory
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        load_cog(filename[:-3])

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(YOUR_WELCOME_CHANNEL_ID)
    if channel is not None:
        # Create an embed for the welcome message
        embed = discord.Embed(
            title=f"Welcome to the server, {member.display_name}!",
            description="Please read the rules in #rules and enjoy your stay.",
            color=0x00ff00  # You can customize the color
        )

        # Add a thumbnail or image to the embed if desired
        embed.set_thumbnail(url="YOUR_IMAGE_URL")

        await channel.send(embed=embed)

# Run the bot with the loaded token
bot.run(BOT_TOKEN)
