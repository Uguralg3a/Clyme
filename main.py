import discord
import os
from dotenv import load_dotenv

intent = discord.Intents.default()
intent.message_content = True

status = discord.Status.dnd
activity = discord.Activity(type=discord.ActivityType.playing, name="Clyme")
bot = discord.Bot(
    intents = intent,
    status = status,
    activity = activity
)



@bot.event
async def on_ready():
    print(f"{bot.user} ist Online!")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

load_dotenv()
bot.run(os.getenv("TOKEN"))