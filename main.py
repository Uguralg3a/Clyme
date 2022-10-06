import discord
from discord.commands import Option

intent = discord.Intents.default()
intent.message_content = True

bot = discord.Bot(intents = intent)

@bot.event
async def on_ready():
    print(f"{bot.user} ist Online!")

@bot.slash_command(description="Grüße einen User")
async def greet(ctx, user: Option(discord.Member, "Der User, den du Grüßen willst"))

bot.run("MTAyNzQ4NzUwNDQzNTI2NTU5Nw.G2-v03.5S-oaA2U0eKO7ozG1NiswfldD01zm9TFLk0Ztg")