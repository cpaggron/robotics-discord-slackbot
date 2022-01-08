import discord
from discord.ext import commands

client = commands.Bot(command_prefix=".")

# List and string check function
def check(_list: list, _string: str):
    for item in _list:
        if item in _string:
            return True 

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


client.run(" ")
