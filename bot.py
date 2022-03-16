from discord.ext import commands
from settings import DISCORD
import logging

# Logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


if __name__ == "__main__" and DISCORD is not None:
    bot = commands.Bot("!")
    bot.load_extension("commands")
    bot.run(DISCORD)
