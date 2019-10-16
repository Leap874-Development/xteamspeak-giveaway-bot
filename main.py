from discord.ext import commands

import discord
import json
import embeds
import database

with open('config.json', 'r') as f:
	config = json.load(f)

with open('secrets.json', 'r') as f:
	secrets = json.load(f)

bot = commands.Bot(command_prefix=config['prefix'])
db = database.Database('database.json')

async def on_ready():
	guild_names = ', '.join([ a.name for a in bot.guilds ])
	print('%s online and logged in as %s' % (config['bot_name'], bot.user))
	print('Connected to %s guild(s): %s' % (len(bot.guilds), guild_names))
	print('Now awaiting commands...')

async def on_command_error(ctx, err):
    if 'GiveawayExists' in str(err):
        await ctx.send(embed=embeds.ErrorEmbed('A giveaway already exists under that name'))
    else:
    	await ctx.send(embed=embeds.CommandErrorEmbed(err, ctx))

@bot.command(name=config['commands']['stop_bot'], help='stops the bot')
@commands.has_permissions(administrator=True)
async def stop_bot(ctx):
	print('Stop command called, bot shutting down')
	await bot.logout()

@bot.command(name=config['commands']['create_giveaway'], help='creates a new giveaway')
@commands.has_permissions(administrator=True)
async def create_giveaway(ctx, name : str):
    ga = db.create_giveaway(name)
    await ctx.send(embed=embeds.GiveawayEmbed(ga))

@bot.command(name=config['commands']['inspect_giveaway'], help='shows giveaway info')
@commands.has_permissions(administrator=True)
async def inspect_giveaway(ctx, name : str):
    raise NotImplemented()

@bot.command(name=config['commands']['list_giveaways'], help='lists all open giveaways')
@commands.has_permissions(administrator=True)
async def list_giveaways(ctx):
    raise NotImplemented()

@bot.command(name=config['commands']['list_all_giveaways'], help='lists all giveaways (including closed)')
@commands.has_permissions(administrator=True)
async def list_all_giveaways(ctx):
    raise NotImplemented()

@bot.command(name=config['commands']['close_giveaway'], help='closes a giveaway')
@commands.has_permissions(administrator=True)
async def close_giveaway(ctx, name : str):
    db.close_giveaway(name)
    await ctx.send(embed=embeds.SuccessEmbed('Giveaway closed'))

@bot.command(name=config['commands']['delete_giveaway'], help='permanently deletes a giveaway')
@commands.has_permissions(administrator=True)
async def delete_giveaway(ctx, name : str):
    raise NotImplemented()

@bot.command(name=config['commands']['draw_user'], help='draws winner(s) from giveaway')
@commands.has_permissions(administrator=True)
async def draw_user(ctx, name : str, quantity : int=1):
    raise NotImplemented()

bot.add_listener(on_ready)
bot.add_listener(on_command_error)
bot.run(secrets['token'])
