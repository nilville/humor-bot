import discord
from discord.ext import commands
import requests
import json

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

based_url = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,racist,sexist'

def get_joke():
    try:
        response = requests.get(based_url)
        if response.status_code == 200:
            joke_data = response.json()
            if joke_data['type'] == 'twopart':
                return f"**1:** {joke_data.get('setup', '')}\n**2:** {joke_data.get('delivery', '')}"
            elif joke_data['type'] == 'single':
                return f"**1:** {joke_data.get('joke', '')}"
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
    print(f'Logged in as {bot.user}')

@bot.command()
async def joke(ctx):
    joke_text = get_joke()
    await ctx.send(joke_text)

# Replace with your actual bot token
bot.run('000000000000000000')