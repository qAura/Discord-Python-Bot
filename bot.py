import discord
import random
import os
import time
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='$')
status = cycle(['$commands', 'Bot By Aura', 'Fixing Bugs', 'Im Asleep'])
class Slapper(commands.Converter):
    async def convert(self, ctx, argument):
        to_slap = random.choice(ctx.guild.members)
        return '*{0.author}* hugged *{2}*'.format(ctx, to_slap, argument)

@client.event
async def on_ready():
    



   change_status.start()
print('Bot By Aura')

@tasks.loop(seconds=3.5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

@client.command()
async def load(ctx, extension):
        client.load_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endwith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send('Successfully Purged This Channels Messages!')
    #Purge Command

    
@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member):
    await member.kick()
    await ctx.send("The Kicking Hammer Has Awoken! Someone Has Been Banished")
    #kick command

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member ):
    await member.ban()
    await ctx.send("The Ban Hammer Has Awoken! Someone Has Been Banished")
    #ban command

@client.event
async def warn(ctx):
    await ctx.send("Warned :ghost:")
    #Fake Warm Command I Will Fix Next Update

@client.command(aliases=['8ball'])
async def eightball(ctx, *, question):
  responses = ['It is certain.',
               'It is decidedly so.',
               'Without a doubt.',
               'Yes - definitely.',
               'You may rely on it.',
               'As I see it, yes.',
               'Most likely.',
               'Outlook good.',
               'Yes.',
               'Signs point to yes.',
               'Reply hazy, try again.',
               'Ask again later.',
               'Better not tell you now.',
               'Cannot predict now.',
               'Concentrate and ask again.',
               'Dont count on it.',
               'My reply is no.',
               'My sources say no.',
               'Outlook not so good.',
               'Very doubtful.',]

  
  await ctx.send(f'Question : {question}\n\nAnswer : {random.choice(responses)}')

  #8ball command

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')
    #ping pong command responds with response time next update

@client.command()
async def slap(ctx, members: commands.Greedy[discord.Member], *, reason='no reason'):
    slapped = ", ".join(x.name for x in members)
    await ctx.send('*{}* just got slapped for {}'.format(slapped, reason))


@client.command()
async def anime(ctx):
    responses = ['https://media.giphy.com/media/f0yOYF0EtwSVa/giphy.gif',
                 'https://media.giphy.com/media/UYzNgRSTf9X1e/giphy.gif',
                 'https://media.giphy.com/media/DeBBINXN86r8Q/giphy.gif',
                 'https://media.giphy.com/media/7hW7hXXri33NK/giphy.gif',
                 'https://media1.tenor.com/images/42922e87b3ec288b11f59ba7f3cc6393/tenor.gif',
                 'https://media.discordapp.net/attachments/561513392402202636/599655606617636864/1520666958_violet_3.gif?width=400&height=226',
                 'https://media.discordapp.net/attachments/590265983248236575/599655841188020225/rage_quit.gif?width=400&height=225',
                 'https://cdn.discordapp.com/attachments/590265983248236575/599655905554071602/tohru.gif',
                 'https://media.discordapp.net/attachments/590265983248236575/599655718991298570/anime_violet.gif?width=400&height=215',
                 'https://media.discordapp.net/attachments/590265983248236575/599655722984275972/cute.gif?width=400&height=225',
                 'https://media.discordapp.net/attachments/590265983248236575/599657446067273760/kyokai.gif',
                 'https://media.discordapp.net/attachments/590265983248236575/599655989268185088/violet.gif?format=png&width=267&height=300',]
                 
                 
                 

    await ctx.send(f'Here You Go! <3\n{random.choice(responses)}')
    #anime pictures cause yano

@client.command()
async def commands(ctx):
    await ctx.send('```\n︵‿︵‿୨♡୧‿︵‿︵\nNormal Users Commands\n$hug hug somebody!\n$slap slap someone!\n$ping Says Pong!\n$anime Gives otakus some sweet anime gifs, to bless their eyes.\n$8ball Ask Bot Questions!\n$say make the bot say something provide an argument!\n︵‿︵‿୨♡୧‿︵‿︵\nStaff Commands\n$purge purges the current channel.\n$kick kicks a pinged user\n$ban bans a pinged user\n︵‿︵‿୨♡୧‿︵‿︵\n```')

    #help command very long <3

@client.command()
async def hug(ctx, *, reason: Slapper):
    await ctx.send(reason)

@client.command()
async def say(ctx, *, arg):
    await ctx.send(arg)







                 
    
    



client.run("token here")

#run your bots token
