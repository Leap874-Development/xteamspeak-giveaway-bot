# Giveaway Bot v1.0
By [William Gardner](https://github.com/wg4568/), written for _@xteamspeak_ on Fiverr

## Installation

To set up your system, you will need to do the following

- Install Python3.7 from their [website](https://www.python.org/)
- Install requirements by running `python -m pip install -r requirements.txt`

You will also need to create an application, through the [Discord dev website](https://discordapp.com/developers/) then give it a bot. You will need the bot token in the `config.json` file for the bot to work!

See [this](https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token) step by step guide for help creating a bot, and obtaining a token.

## Files

### Most important

You will need to use these files!

- `README.md` this file, for help and info
- `config.json` options and configuration
- `requirements.txt` required packages
- `main.py` run this to start the bot

### Secrets file

You will need to create a secrets file, called `secrets.json` in the same folder as `main.py`. In this file, put the following-- however replace BOT_TOKEN with your bot token generated from the [discord dev website](https://discordapp.com/developers/).

```
{
	"token": "BOT_TOKEN"
}
```

### Other files

Don't touch these unless you know what you're doing!

- `database.json` where list data is stored
- `embeds.py` discord embed classes

## Configuration

See `config.json` to configure the bot.

The config file is formatted with the parameter name on the left, and it's value on the right. Do NOT touch the name on the left! This will break the bot. Instead change the value on the right to tweak your bot.

    "name": "value (change this!)"

Values that are text (as opposed to a number) should be surrounded by double quotes, as shown above.

 Configuration parameters are described below.

- `prefix` bot command prefix
- `bot_name` the name of your bot, can be anything
- `embed_colors` side-color of the bot messages (in rgb)
- `commands` command names, and the actual command itself-- use this if you want to rename a command