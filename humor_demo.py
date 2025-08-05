import discord
from discord.ext import commands
import random
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

based_url = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,racist,sexist'

def get_joke():
    try:
        response = requests.get(based_url)
        if response.status_code == 200:
            joke_data = response.json()
            if joke_data['type'] == 'twopart':
                return f"# **1:** {joke_data.get('setup', '')}\n # **2:** {joke_data.get('delivery', '')}"
            elif joke_data['type'] == 'single':
                return f"# **1:** {joke_data.get('joke', '')}"
            else:
                return "Unknown joke type."
        else:
            return f"Error fetching joke: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Error connecting to joke API: {str(e)}"
    except json.JSONDecodeError:
        return "Error parsing joke data."

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def joke(ctx):
    joke_text = get_joke()
    await ctx.send(joke_text)
    
@bot.command()
async def yo(ctx):
    await ctx.send(f"# **<@{ctx.author.id}> nikmok azbi, neyek wjh zbi**")

@bot.command()
async def demo(ctx):
    await ctx.send("● █▀█▄ Ɑ͞ ̶͞ ̶͞ ̶͞ لں͞ ")
    

# Replace with your actual bot token
bot.run(os.getenv("DISCORD_BOT_TOKEN"))