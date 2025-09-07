import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! 👋")

bot.run("YOUR_BOT_TOKEN")
