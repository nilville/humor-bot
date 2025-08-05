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

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command()
async def test(ctx):
    await ctx.send(f"<@{ctx.author.id}> \n- **USERNAME** : {ctx.author.name} \n- **NICKNAME** : {ctx.author.display_name} \n- **ID** : {ctx.author.id} \n- **GUILD** : {ctx.guild.name} \n- **GUILD ID** : {ctx.guild.id}")

@bot.command(name='members')
async def list_members(ctx):
    guild = ctx.guild

    if guild is None:
        await ctx.send("This command can only be used in a server.")
        return

    members = guild.members
    member_count = len(members)

    member_list = []
    for member in members:
        if member.display_name != member.name:
            member_info = f" - **{member.name} ({member.display_name})**"
        else:
            member_info = f" - **{member.name}**"
        member_list.append(member_info)

    message = f"# **Members in {guild.name} ({member_count} total):**\n"
    
    current_message = message
    for member_info in member_list:
        test_message = current_message + member_info + "\n"
        
        if len(test_message) > 1900:
            await ctx.send(current_message)
            current_message = member_info + "\n"
        else:
            current_message = test_message

    if current_message.strip():
        await ctx.send(current_message)

@bot.command(name="buy")
async def random_member(ctx):
    guild = ctx.guild
    if guild is None:
        await ctx.send("This command can only be used in a server.")
        return
    chosen_member = random.choice(guild.members)
    cost = random.uniform(50, 100)
    await ctx.send(f" - THIS NIGGA **{chosen_member.mention}** COST : **{round(cost, 2)} $** ")


# Replace with your actual bot token
bot.run(os.getenv("DISCORD_BOT_TOKEN"))