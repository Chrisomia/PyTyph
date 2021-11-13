import os
import discord
import random
import aiohttp
import asyncio
from discord.ext import commands, tasks
from pyrandmeme import *
from prsaw import RandomStuff
from dotenv import load_dotenv
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from itertools import cycle
from youtube_dl import YoutubeDL
import time
from cowpy import cow
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button, ButtonStyle, InteractionType
#Thank you very much yumyum for helping me creat dis
#   yum - np <3 😋


intents = discord.Intents.default()
description = "Python bot made by Angel, Prefix '+', Have a beautiful and relaxing day"
bot = commands.Bot(owner_id=902337698663116810,
                   description=description,
                   intents=intents,
                   command_prefix="+")


#bred ps. yum was here
@bot.event
async def on_ready():
	print('connecting...')
	print('-------------------------------------')
	print(f'username : {bot.user}')
	print(f'user id  : {bot.user.id}')
	print('-------------------------------------')

	await bot.wait_until_ready()
	print('online!')
	await bot.change_presence(status=discord.Status.online,
	                          activity=discord.Activity(
	                              name="chill out | prefix'+'",
	                              type=discord.ActivityType.listening))


#AYO I'M IN
#basic hello command
@bot.command(name="hello", help="reply test")
async def hello(ctx):
	async with ctx.channel.typing():
		await asyncio.sleep(3)
		await ctx.reply(content="Hi!, I'm moonrunes. Bot made in Python by Chris Ki! My prefix is +", mention_author=False)


#shows bot ping
@bot.command(name="ping", help="shows current bot ping")
async def ping(ctx):
	bed = discord.Embed(description=(f"Pong! {round(bot.latency * 1000)}ms"))
	bed.set_footer(text="Ping test", icon_url=ctx.author.avatar_url)
	bed.set_image(
	    url=
	    "https://media1.giphy.com/media/fvA1ieS8rEV8Y/giphy.gif?cid=6c09b9529236fdd69005de10fc4ab1efde32902c66643e24&rid=giphy.gif&ct=g"
	)
	await ctx.send(embed=bed, delete_after=3)


#shows mentioned user avatar
@bot.command(name='av', help='fetch avatar of a user')
async def avatar(ctx, member: discord.Member = None):
	if member == None:
		member = ctx.author
	else:
		member = member
	bed = discord.Embed(title=member.display_name)
	bed.set_image(url=member.avatar_url)
	await ctx.send(embed=bed)


#SHEEEEESH
@bot.command(name="sheeesh", help="displays Sheeesh gif")
async def sheeesh(ctx):
	bed = discord.Embed(description=(f"Sheeesh"))
	bed.set_footer(text="das realy cool bro", icon_url=ctx.author.avatar_url)
	bed.set_image(
	    url=
	    "ttps://media1.tenor.com/images/7627864f2888cead2c6d5c94dd142126/tenor.gif?itemid=21479305"
	)
	await ctx.send(embed=bed)


#sandwich
@bot.command(name="sandwich", help="moonrunes makes u a sandwich")
async def sandwich(ctx):
	bed = discord.Embed(description=(f"Here u go m8"))
	bed.set_footer(text="epic", icon_url=ctx.author.avatar_url)
	bed.set_image(
	    url=
	    "https://media.tenor.com/images/25ccab8b7aee79d8475ecb8dcb465f6a/tenor.gif"
	)
	await ctx.send(embed=bed)


#caught in 4k meme
@bot.command(name="uhd", help="caught in 4k gif")
async def uhd(ctx):
	bed = discord.Embed(colour=0x6b9aba, timestamp=ctx.message.created_at)
	bed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	bed.set_footer(text="less go", icon_url=ctx.author.avatar_url)
	bed.set_image(
	    url=
	    "https://media1.tenor.com/images/37e56f0349e09f17c890c1503b7655fd/tenor.gif"
	)
	await ctx.send(embed=bed)
	await ctx.message.add_reaction("✔️")


#template embed for future use
@bot.command(name="embed-template", help="embed template for future use")
async def embed(ctx):
	bed = discord.Embed(title="test embed",
	                    description="still nid to learn ~Insomia",
	                    colour=0x6b9aba,
	                    timestamp=ctx.message.created_at)
	bed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	bed.set_footer(text="footer", icon_url=ctx.author.avatar_url)
	bed.add_field(name="name of the field 1",
	              value="it's value 1",
	              inline=False)
	bed.add_field(name="name of the field 2",
	              value="it's value 2",
	              inline=False)
	bed.add_field(name="name of the field 3",
	              value="it's value 3",
	              inline=False)
	bed.set_thumbnail(
	    url="https://media.giphy.com/media/gkpnGTiy8Sq08/giphy.gif")
	bed.set_image(
	    url=
	    "https://media0.giphy.com/media/6C9CMGMFtzzbO/giphy.gif?cid=ecf05e47cy0uir5limq6ku5wqbyui7p8b6txqs3bbd9klw3s&rid=giphy.gif"
	)

	await ctx.send(embed=bed)


#cowsay
@bot.command(name="cowsay", help="is cowsay, u know this cow")
async def cowsay(ctx, *, message):
	moo = cow.Cowacter(eyes="default", thoughts=True, tongue=True, body=None)
	msg = moo.milk(msg=message)
	fun_bed = discord.Embed(
	    title="cowsay 🐮",
	    description=
	    f"mooo! \n```{msg}                                                                                       ```"
	)

	await ctx.send(embed=fun_bed)


#Mute command by The World Of PC
@bot.command(description="Mutes the specified user.",
             help="mutes the desired user")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
	guild = ctx.guild
	mutedRole = discord.utils.get(guild.roles, name="Muted")

	if not mutedRole:
		mutedRole = await guild.create_role(name="Muted")

		for channel in guild.channels:
			await channel.set_permissions(mutedRole,
			                              speak=False,
			                              send_messages=False,
			                              read_message_history=True,
			                              read_messages=False)
	embed = discord.Embed(title="Muted",
	                      description=f"{member.mention} was muted ",
	                      colour=discord.Colour.light_grey())
	embed.add_field(name="reason:", value=reason, inline=False)
	await ctx.send(embed=embed)
	await member.add_roles(mutedRole, reason=reason)
	await member.send(
	    f" you have been muted from: {guild.name} reason: {reason}")


#connected to mute command, displays the error if something is wrong
@mute.error
async def mute_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		embed = discord.Embed(color=discord.Color.green())
		embed.set_image(
		    url=
		    'https://img-comment-fun.9cache.com/media/a8bq7Yp/aXPjQ0qP_700w_0.jpg'
		)
		await ctx.send(f'pff u thought {ctx.author.mention}')
		await ctx.send(embed=embed)


#ban command
@bot.command(name="ban", help="bans the mentioned user with reason")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)
	embed = discord.Embed(title="User Banned!",
	                      description="**{0}** was banned by **{1}**!".format(
	                          member, ctx.message.author),
	                      color=0xBC0000)
	await ctx.send(embed=embed)


#kick command
@bot.command(name="kick", help="kicks the mentioned user with reason")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	embed = discord.Embed(title="User Kicked!",
	                      description="**{0}** was kicked by **{1}**!".format(
	                          member, ctx.message.author),
	                      color=0xff00f6)
	await ctx.send(embed=embed)


#shows random memes
@bot.command(name="meme", help="shows random memes")
async def meme(ctx):
	await ctx.send(embed=await pyrandmeme())


#displays informations about the mentioned user
@bot.command(aliases=["whois"], help="who is dat command")
async def userinfo(ctx, member: discord.Member = None):
	if not member:  # if member is no mentioned
		member = ctx.message.author  # set member as the author
	roles = [role for role in member.roles]
	embed = discord.Embed(colour=discord.Colour.purple(),
	                      timestamp=ctx.message.created_at,
	                      title=f"User Info - {member}")
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_footer(text=f"Requested by {ctx.author}")

	embed.add_field(name="ID:", value=member.id)
	embed.add_field(name="Display Name:", value=member.display_name)

	embed.add_field(
	    name="Created Account On:",
	    value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
	embed.add_field(
	    name="Joined Server On:",
	    value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

	embed.add_field(name="Roles:",
	                value="".join([role.mention for role in roles]))
	embed.add_field(name="Highest Role:", value=member.top_role.mention)
	print(member.top_role.mention)
	await ctx.send(embed=embed)


#basic clear command
@commands.bot_has_guild_permissions(manage_messages=True)
@commands.has_guild_permissions(manage_messages=True)
@bot.command(name="clear", help="clears set ammount of messanges")
async def clear(ctx, amount=0):
	if (ctx.message.author.permissions_in(
	    ctx.message.channel).manage_messages):
		await ctx.channel.purge(limit=amount + 1)
		await ctx.send("**Messages has been yeeted!**", delete_after=3)


#basic clear error, displays if user has no premissions
@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('**Bruh, No.**')



load_dotenv()

players = {}

#Join Command
@bot.command()
async def join(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send('Alright, I joined what now?, (btw currently you can only play music by pasting yt links, will be fixed later)')
        await ctx.message.add_reaction('🎧')


#YT URL Play Command
@bot.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Playing your vibes.....')
        await ctx.message.add_reaction('▶️')

# check if the bot is already playing
    else:
        await ctx.send("Bot is already playing")
        return


#Resume Command
@bot.command()
async def resume(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        voice.resume()
        await ctx.send('Welcome back!, Resuming... ')
        await ctx.message.add_reaction('▶️')


#Pause Command
@bot.command()
async def pause(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.pause()
        await ctx.send('*vibing pauses*')
        await ctx.message.add_reaction('⏸️')



#Stop Command
@bot.command()
async def stop(ctx):
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice.is_playing():
        voice.stop()
        await ctx.send('Aight, no vibe it is.')
        await ctx.message.add_reaction('⏸️')

#Leave Command
@bot.command(name='leave', help='This command stops makes the bot leave the voice channel')
async def leave(ctx):
    voice_bot = ctx.message.guild.voice_client
    await voice_bot.disconnect()
    await ctx.send('Aight Disconecting...')
    await ctx.message.add_reaction('👋')






#Create a key named "TOKEN" if in Replit and add token as the value, and if you're working on local IDE use bot.run('TOKEN') where 'TOKEN' is your discord bot token
bot.run(os.environ['TOKEN'])


