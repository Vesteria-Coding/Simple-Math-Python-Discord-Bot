import discord
import time as t
from discord.ext import commands
from simpleeval import simple_eval

# Setup Credentials
BOT_TOKEN = 'Bot_Token_Here'

# Setup
intents = discord.Intents.all()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)
@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

# Commands
@bot.command(name='ping')
async def ping(ctx):
    latency = bot.latency * 1000  # Convert to ms
    await ctx.send(f'Pong! `{latency:.2f}ms`')

@bot.command(name='math')
async def ping(ctx, *, math_problem: str):
    start = t.time()
    try:
        output = simple_eval(math_problem)
    except Exception as e:
        output = f'Error: {e}'
    end = t.time()
    await ctx.send(output)
    t.sleep(0.1)
    time = (end - start) * 1000
    await ctx.send(f'{time:.2f}ms to do that equstion')

bot.run(BOT_TOKEN)
