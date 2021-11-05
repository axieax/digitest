import re
import discord

client = discord.Client()
ECHO_COMMAND = "!echo "


@client.event
async def on_ready():
    print(f"{client.user} online")


@client.event
async def on_message(message):
    author = message.author
    # bad bot -> it's a bot, but it ain't me
    if author.bot and author == client.user:
        print("bad bot")
        return

    # ignore bot messages
    if author.bot:
        return

    # echo message back to channel
    channel = message.channel
    text = message.content
    if text.startswith(ECHO_COMMAND):
        await echo_command(message)


async def echo_command(message):
    channel = message.channel
    text = message.content
    await channel.send(text[len(ECHO_COMMAND) :])


if __name__ == "__main__":
    client.run("")
