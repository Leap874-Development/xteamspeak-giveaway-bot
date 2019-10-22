import discord
import json

with open('config.json', 'r') as f:
    config = json.load(f)

class ErrorEmbed(discord.Embed):
    def __init__(self, message):
        self.color = discord.Color.from_rgb(*config['embed_colors']['error'])
        self.message = message

        discord.Embed.__init__(self,
                color=self.color, title='An error occured',
                description=self.message)

class CommandErrorEmbed(discord.Embed):
    def __init__(self, err, ctx):
        self.color = discord.Color.from_rgb(*config['embed_colors']['error'])
        self.message = str(err)
        self.help = 'See %shelp %s' % (config['prefix'], ctx.command)

        discord.Embed.__init__(self,
                color=self.color, title='Invalid command usage',
                description=self.message)
        self.set_footer(text=self.help)

class SuccessEmbed(discord.Embed):
    def __init__(self, message):
        self.color = discord.Color.from_rgb(*config['embed_colors']['success'])
        self.message = message

        discord.Embed.__init__(self,
                color=self.color, title='Success',
                description=self.message)

class GiveawayEmbed(discord.Embed):
    def __init__(self, ga):
        self.color = discord.Color.from_rgb(*config['embed_colors']['info'])

        discord.Embed.__init__(self, color=self.color, title='Giveaway \'%s\' created' % ga['name'])
        self.set_footer(text='React to this message to join the giveaway')

class GiveawayInspectEmbed(discord.Embed):
    def __init__(self, ga, uses, users):
        self.color = discord.Color.from_rgb(*config['embed_colors']['info'])
        self.giveaway = ga
        self.uses = uses
        self.users = users
        self.desc = ''

        for inv in self.giveaway['invites']:
            uses = self.uses[inv['code']]
            user = self.users[inv['user']]
            if (user): self.desc += '%s - %s tickets\n' % (user.mention, uses)

        discord.Embed.__init__(self,
            color=self.color, title='Giveaway info for \'%s\' ' % ga['name'],
            description=self.desc)