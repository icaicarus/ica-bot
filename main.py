import random, math, discord, os, dotenv, mysql.connector, datetime
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("TOKEN")

class Client(discord.Client):

    async def on_ready(self):
        print(f'Logged on as {self.user}')

intents = discord.Intents.all()

client = Client(intents=intents)
client.run(token)