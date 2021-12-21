# Bot is short for robot and is a software application that performs automated, repetitive and pre-defined tasks. 
# Bots typically imitate or replace human behavior. As they are automated, they operate much faster than human users.

import os
import time
import random
import discord # pip installed
from dotenv import load_dotenv # pip installed

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents) # discord.Client() creates a connection to Discord. This class is used to interact with Discord.

# load bot's token
load_dotenv()
TOKEN = os.getenv("TOKEN")

# asynchronous functions or programs allow functions to run out of order while say a different function is waitng on something to happen
@client.event
async def on_ready():
  await client.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name = "Lo-Fi"))
  print("Bot is ready and logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
  channel = client.get_channel(920409186674819086)
  # embed = discord.Embed(title = f"Yo what's up {member.name}!", description = f"Thanks for joining {member.guild.name}. 
  # I'm Lord V, formally known as Tom Riddle, you may have heard of me. Ready to defeat Harry Potter once and for all?")
  # embed.set_thumbnail(url = member.avatar_url) # Set the embed's thumbnail to the member's avatar image!
  welcome_messages = [
    f"Welcome, {member.name}! Together we're going to destory Harry Potter!",
    f"What's going on {member.name}?, I heard you hate Harry Potter just as much as I do. I think you'll be a valuable asset to the team.",
    f"Yo what's up {member.name}. I'm Lord V, but you can call me Tom. How're your wand skills?",
  ]

  time.sleep(1)
  random_message = random.choice(welcome_messages)

  await channel.send(random_message)
  # await channel.send(embed = embed)
  if not channel:
    return

@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f"{username}: {user_message} ({channel})")

  # bot won't reply to its own messages  
  if message.author == client.user:
    return

  if message.channel.name == "general":
    hello_responses = [
    f"Hey {username}! How're you doing? What do you say we destroy Harry Potter?",
    f"What's going on {username}? It's a fine day to finally defeat Harry Potter.",
    f"Yo what's up {username}. I feel like defeating Harry Potter today. You with me?",
  ]
    random_hello_responses = random.choice(hello_responses)

    if user_message == "Hello".lower() or user_message == "Hey".lower() or user_message == "Heyy".lower() or \
    user_message == "What's up".lower() or user_message == "Whats up".lower() or user_message == "Sup".lower() or user_message == "Yo".lower():
      await message.channel.send(random_hello_responses)
      return
    # if user_message == 'bye'
    if user_message == "Bye".lower() or user_message == "See you later".lower(): # if user_message.lower() == 'bye'
      await message.channel.send(f"See you later {username}. Keep practicing your wand skills.")
    if "Harry Potter".lower() in user_message:
      await message.channel.send(f"Did someone say Harry Potter? Ugh, I hate that guy.")
    elif "Potter".lower() in user_message or "Pot".lower() in user_message or "Pottery".lower() in user_message:
      await message.channel.send(f"Did you say Potter? If you're talking about Harry Potter, STOP.")
    elif "Harry".lower() in user_message or "Hairy".lower() in user_message:
      await message.channel.send(f"Did someone say Harry? As in Harry Potter? Yeah, we don't talk about him here.")

# runs bot when file is ran
client.run(TOKEN)
