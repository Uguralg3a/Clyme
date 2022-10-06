import discord
import os
from dotenv import load_dotenv

intent = discord.Intents.default()
intent.message_content = True

bot = discord.Bot(intents = intent)

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(" Clyme "))
    print(f"{bot.user} ist Online!")

for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")

load_dotenv()
bot.run(os.getenv("TOKEN"))
