import discord
from discord.ext import commands

import os
import json

client = commands.Bot(command_prefix=".")
client.remove_command('help')


# Open JSON file to get the list of keywords that aren't built in
if os.path.exists('words.json'):
    with open('words.json', 'r') as file:
        words = json.load(file)
else:
    words = {}

# List and string check function
def check(_list: list, _string: str):
    for item in _list:
        if item in _string:
            return True 

# Turn list into a pretty string
def unlistify(_list: list):
    string = ""
    for item in _list:
        string += f"`{item}` "
    if string == "":
        return "N/A"
    else:
        return string

# Help command
@client.command()
async def help(ctx):
    embed = discord.Embed(title="Words I Respond To", color=discord.Color.magenta())
    embed.add_field(name="Permanant Ones", value="`slay` `anti slay` `sleigh` `bad bot` `good bot`", inline=False)
    embed.add_field(name="Not Permanant Ones", value=unlistify(words), inline=False)
    embed.add_field(name="Other Commands", value="`add [word]`: To add a word\n`remove [word]`: To remove a word")
    await ctx.send(embed=embed)

@client.command()
async def add(ctx, word: str):
    await ctx.author.send(f"How would you like the bot to respond to the word `{word}`?")
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    await ctx.author.send(f"The bot will respond with `{msg.content}` when `{word}` is entered. `Type confirm` to confirm.")
    confirm = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if confirm.content == "confirm" or confirm.content == "Confirm":
        words[word] = msg.content
        with open("words.json", "w+") as i:
            json.dump(words, i)
        await ctx.send(f"Added `{word}`")

@client.command()
async def remove(ctx, word: str):
    await ctx.send(f"Are you sure you would like to remove the word `{word}`? [y/n]")
    msg = await client.wait_for('message', check=lambda message: message.author == ctx.author)
    if msg.content == "y" or msg.content == "Y":
        words.pop(word)
        with open("words.json", "w+") as i:
            json.dump(words, i)
        await ctx.send(f"Deleted `{word}`")
        
        

# Check for keywords
@client.event
async def on_message(message):

    # Create Shortcuts
    send = message.channel.send
    msg = message.content

    # Make sure that the message author isn't the bot
    await client.process_commands(message)
    if message.author == client.user:
        return

    if check(["anti slay", "Anti slay", "Anti Slay"], msg) == True: 
        await send("electric chair :zap::zap:")

    elif check(["slay", "Slay"], msg) == True:
        await send("go best friend:raised_hands::raised_hands::raised_hands::raised_hands:!!")
            
    elif check(["sleigh", "Sleigh"], msg) == True:
        await send("Ho! Ho! Ho!  :santa::deer::deer::deer:")

    elif check(["bad bot", "Bad bot", "Bad Bot"], msg) == True:
        await send("bad human")

    elif check(["good bot", "Good bot", "Good Bot"], msg) == True:
        await send("thx")

    elif check(["s l e i g h", "S l e i g h"], msg) == True:
        await send("H o !  H o !  H o !  :santa: :deer: :deer: :deer:")

    elif check(["s l a y", "S l a y"], msg) == True:
        await send("g o  b e s t  f r i e n d :raised_hands: :raised_hands: :raised_hands: :raised_hands: ! !")

    elif check(words.keys(), msg) == True:
        if not msg.startswith(".remove"):
            await send(words[msg])

client.run(" ")
