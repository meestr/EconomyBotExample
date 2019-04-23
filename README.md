# Economy Example
This is a simple economy example bot.

It features 5 trivial commands.

| Command               | Description                                   |
|-----------------------|-----------------------------------------------|
| balance               | Displays the user's balance.                  |
| create                | Registers a user in the database.             |
| coinflip [side] [bet] | Plays a coin-flip game.                       |
| slots [bet]           | Plays a slots machine game.                   |
| dice [side] [bet]     | Virtually the same as coinflip, but with dice |

## Setup:

#### Dependency installation
Dependencies:

 - Python 3.5 or higher.
 - Discord.py Rewrite

If you're on Windows, download the latest python from python.org/downloads.

If you're on Mac, open terminal and type in:
```bash
$ sudo apt-get update
$ sudo apt-get install python3 && sudo apt-get install python3-pip
```

Now install discord.py

### Windows:
Use CMD and type in:
```bash 
py -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
```

### Mac:
```bash
$ python -m pip install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
```

### Configuration and launch:
Open ``config.json`` with any text editor and replace ``token`` with your bot token ([Follow this guide if you need help](https://discordpy.readthedocs.io/en/rewrite/discord.html)) and ``currency`` for whatever you want your currency to be. ``color`` should be in RGB format and ``commandPrefix`` should be what you want your command to start off with.

After you're done, run the program. If all goes well, you've done it!
