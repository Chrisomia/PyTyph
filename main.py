import asyncio
from cowpy import cow
from pyrandmeme import *
import os
#Thank you very much yumyum, and The World Of PC for helping me creat dis
#   yum - np <3 😋
import discord
from discord.ext import commands

intents = discord.Intents.default()
description = "Bot made while my Insomia was kickin in"
bot = commands.Bot(owner_id=327160726181511171,
                   description=description,
                   intents=intents,
                   command_prefix="+")


@bot.event
async def on_ready():
	print('connecting...')
	print('-------------------------------------')
	print(f'username : {bot.user}')
	print(f'user id  : {bot.user.id}')
	print('-------------------------------------')

	await bot.wait_until_ready()
	print('online!')
	await bot.change_presence(status=discord.Status.dnd,
	                          activity=discord.Activity(
	                              name="Insomia <.<",
	                              type=discord.ActivityType.watching))


@bot.command(name="hello")
async def hello(ctx):
	async with ctx.channel.typing():
		await asyncio.sleep(5)
		await ctx.reply(content="Hey", mention_author=False)

@bot.command(name="ping")
async def ping(ctx):
	bed = discord.Embed(description=(f"Pong! {round(bot.latency * 1000)}ms"))
	bed.set_footer(text="Ping test", icon_url=ctx.author.avatar_url)
	bed.set_image(url="https://media1.giphy.com/media/fvA1ieS8rEV8Y/giphy.gif?cid=6c09b9529236fdd69005de10fc4ab1efde32902c66643e24&rid=giphy.gif&ct=g"
	)
	await ctx.send(embed=bed, delete_after=3)

@bot.command(name="sheeesh")
async def sheeesh(ctx):
	bed = discord.Embed(description=(f"Sheeesh"))
	bed.set_footer(text="das realy cool bro", icon_url=ctx.author.avatar_url)
	bed.set_image(url="https://media1.tenor.com/images/7627864f2888cead2c6d5c94dd142126/tenor.gif?itemid=21479305"
	)
	await ctx.send(embed=bed, delete_after=5)

@bot.command(name="uhd")
async def uhd(ctx):
	bed = discord.Embed(colour=0x6b9aba, timestamp=ctx.message.created_at)
	bed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
	bed.set_footer(text="less go", icon_url=ctx.author.avatar_url)
	bed.set_image(url="https://media1.tenor.com/images/37e56f0349e09f17c890c1503b7655fd/tenor.gif"
	)
	await ctx.send(embed=bed)
	await ctx.message.add_reaction("✔️")


@bot.command(name="embed")
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


@bot.command(name="cowsay")
async def cowsay(ctx, *, message):
	moo = cow.Cowacter(eyes="default", thoughts=True, tongue=True, body=None)
	msg = moo.milk(msg=message)
	fun_bed = discord.Embed(
	    title="cowsay 🐮",
	    description=
	    f"mooo! \n```{msg}                                                                                       ```"
	)

	await ctx.send(embed=fun_bed)


@bot.command(description="Mutes the specified user.")
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


@bot.command(name="ban")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
	await member.ban(reason=reason)
	embed = discord.Embed(title="User Banned!",
	                      description="**{0}** was banned by **{1}**!".format(
	                          member, ctx.message.author),
	                      color=0xBC0000)
	await ctx.send(embed=embed)


@bot.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
	await member.kick(reason=reason)
	embed = discord.Embed(title="User Kicked!",
	                      description="**{0}** was kicked by **{1}**!".format(
	                          member, ctx.message.author),
	                      color=0xff00f6)
	await ctx.send(embed=embed)


@bot.command(name="meme")
async def meme(ctx):
	await ctx.send(embed=await pyrandmeme())


@bot.command(aliases=["whois"])
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


@commands.bot_has_guild_permissions(manage_messages=True)
@commands.has_guild_permissions(manage_messages=True)
@bot.command(name="clear")
async def clear(ctx, amount=0):
	if (ctx.message.author.permissions_in(
	    ctx.message.channel).manage_messages):
		await ctx.channel.purge(limit=amount + 1)
		await ctx.send("**Messages has been yeeted!**", delete_after=3)


@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send('**Bruh, No.**')


bot.run(os.environ['TOKEN'])
