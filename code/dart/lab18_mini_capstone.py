# Bot is short for robot and is a software application that performs automated, repetitive and pre-defined tasks. 
# Bots typically imitate or replace human behavior. As they are automated, they operate much faster than human users.

import os
import time
import random
import discord
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents = intents) # discord.Client() creates a connection to Discord. This class is used to interact with Discord.

# load bot's token
load_dotenv()
TOKEN = os.getenv("TOKEN")

@client.event
async def on_ready(): # as far as I understand it, asynchronous functions or programs allow functions to run out of order while say a different function is waitng on something to happen
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
    if any(word in user_message for word in "Sup".lower()) or any(word in user_message for word in "Hello".lower()) \
    or any(word in user_message for word in "Hey".lower()) or any(word in user_message for word in "What's up".lower()) \
    or any(word in user_message for word in "Whats up".lower()):
    # if user_message == "Hello".lower() or user_message == "Hey".lower() or user_message == "Whats up".lower() or user_message == "What's up".lower() or user_message == "Sup".lower():
      await message.channel.send(f"Hello {username}. I'm glad to have you on our team. What do you say we destroy Harry Potter.")
      return
    elif user_message == "Bye".lower() or user_message == "see you later".lower():
      await message.channel.send(f"See you later {username}. Keep practicing your wand skills.")
    elif user_message == "Harry Potter".lower():
      await message.channel.send(f"Did someone say Harry Potter? Ugh, I hate that guy.")
    elif any(word in user_message for word in "Harry") or any(word in user_message for word in "Hairy"):
      await message.channel.send(f"Did someone say Harry? As in Harry Potter? Yeah, we don't talk about him here.")
    elif any(word in user_message for word in "Potter"):
      await message.channel.send(f"Did you say Potter? If you're talking about Harry Potter, STOP.")

# runs bot when file is ran
client.run(TOKEN)
