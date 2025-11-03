import discord
import os
import datetime

# Optionally load environment variables from a .env file. This requires
# installing python-dotenv (added to requirements.txt).
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # If python-dotenv isn't installed, we simply continue and rely on real
    # environment variables. This keeps the script working without forcing
    # a new dependency at runtime.
    pass

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

client = discord.Client(intents=intents)
active_recordings = {}  # Using a dictionary to store notified users
LOG_CHANNEL_NAME = "recording-log"

async def log_action(guild, message):
    """Finds the log channel and sends a message."""
    log_channel = discord.utils.get(guild.text_channels, name=LOG_CHANNEL_NAME)
    if log_channel:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        await log_channel.send(f"[{timestamp}] {message}")
    else:
        print(f"Could not find the log channel #{LOG_CHANNEL_NAME}")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_voice_state_update(member, before, after):
    # Check if the user is the Craig bot
    if member.bot and "craig" in member.name.lower():
        # Craig joined a voice channel
        if after.channel and after.channel.id not in active_recordings:
            print(f"Craig has joined {after.channel.name}, starting recording notification.")
            active_recordings[after.channel.id] = set()  # Initialize a set for notified users
            await log_action(member.guild, f"Craig started recording in {after.channel.name}.")
            await notify_channel_members(after.channel)

        # Craig left a voice channel
        elif before.channel and not after.channel:
            if before.channel.id in active_recordings:
                print(f"Craig has left {before.channel.name}, stopping recording notification.")
                del active_recordings[before.channel.id]
                await log_action(member.guild, f"Craig stopped recording in {before.channel.name}.")

    # Check if a user joins a channel that is being recorded
    elif after.channel and after.channel.id in active_recordings:
        if not member.bot and member.id not in active_recordings[after.channel.id]:
            print(f"{member.name} has joined the recorded channel {after.channel.name}.")
            await notify_user(member, after.channel)

async def notify_channel_members(channel):
    """Notifies all members in a voice channel that recording has started."""
    message = (
        f"⚠️ Notice: The voice channel {channel.name} is currently being recorded by Craig Bot.\n"
        "If you do not consent, please leave immediately.\n"
        "If you wish your recording removed, open a ticket within 24 hours at #support."
    )
    for member in channel.members:
        if not member.bot:
            await notify_user(member, channel, message)

async def notify_user(member, channel, message=None):
    """Sends a DM to a user about the recording."""
    if message is None:
        message = (
            f"⚠️ Notice: The voice channel {channel.name} is currently being recorded by Craig Bot.\n"
            "If you do not consent, please leave immediately.\n"
            "If you wish your recording removed, open a ticket within 24 hours at #support."
        )
    try:
        await member.send(message)
        print(f"Sent recording notification to {member.name}")
        if channel.id in active_recordings:
            active_recordings[channel.id].add(member.id)
        await log_action(member.guild, f"User {member.name} notified about recording in {channel.name}.")
    except discord.Forbidden:
        print(f"Could not send DM to {member.name}. They may have DMs disabled.")
    except Exception as e:
        print(f"An error occurred while sending a DM to {member.name}: {e}")

if __name__ == '__main__':
    # To run this bot, you must set the DISCORD_TOKEN environment variable.
    # For example:
    # export DISCORD_TOKEN='your_bot_token'
    # python src/main.py

    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("Error: The DISCORD_TOKEN environment variable is not set.")
        print("Options to provide it:")
        print(" - For the current PowerShell session: $env:DISCORD_TOKEN = 'your_token_here' ; python .\\main.py")
        print(" - Persist for your user: setx DISCORD_TOKEN \"your_token_here\" (then open a new shell)")
        print(" - Create a .env file in the project root with: DISCORD_TOKEN=your_token_here and install python-dotenv")
    else:
        print("Starting bot...")
        client.run(token)
