from discord.ext import commands
from settings import DISCORD

if __name__ == "__main__" and DISCORD is not None:
    bot = commands.Bot("!")
    bot.load_extension("commands")
    bot.run(DISCORD)
