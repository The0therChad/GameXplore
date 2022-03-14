import os

import discord
from dotenv import load_dotenv

load_dotenv()

ID = os.getenv("CLIENT_ID")
TOKEN = os.getenv("ACCESS_TOKEN")
DISCORD = os.getenv("DISCORD_TOKEN")
