import discord

token = "OTIwNDA5NTM2MzU4MTI1NTY4.Ybj8LQ.vvculqtxtheAHuG0TtYUSZE9fQM"

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  print(f"{username}: {user_message} ({channel})")

  if message.author == client.user:
    return

  if message.channel.name == "general":
    if user_message == "Hello".lower():
      await message.channel.send(f"Hello {username}. I hope you're ready to join the Death Eaters and destroy Harry Potter.")
      return
    elif user_message == "Bye".lower():
      await message.channel.send(f"See you later {username}")

client.run(token)

