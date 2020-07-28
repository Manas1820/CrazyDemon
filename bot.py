# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup
import random
import numpy
import discord 
from discord.ext import commands
client = commands.Bot(command_prefix = '$')

TOKEN='NzM3MDMwNTcyNDI1MzQ3MDcy.Xx3bNQ.ge7PeteW7GenQuGfQveYLu0xBM0'

@client.event

async def on_ready():
    print("bot is ready .")

@client.event

async def on_member_join(member):
    print(f"{member} joined the server !")

@client.event

async def on_member_remove(member):
    print(f"{member} left the server !")

@client.command()

async def ping(ctx):
    await ctx.send(f"Hey your ping is {round(client.latency*1000)} ms")

@client.command(aliases=['Quote','quotes','Quotes'])

async def quote(ctx):
    QUOTES=[]
    url='https://www.brainyquote.com/quote_of_the_day'
    headers={
    'accept-encoding': 'gzip, deflate, sdch',
    'accept-language': 'en-US,en;q=0.8',
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Mobile Safari/537.36',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer':'https://www.brainyquote.com/',
    'Connection':'keep-alive'
    }
    r=requests.get(url=url,headers=headers) 
    soup = BeautifulSoup(r.text,'html.parser')
    for x in soup.findAll('a',{'title':"view quote"}):
        QUOTES.append(x.text)

    await ctx.send(f"{random.choice(QUOTES)}")

client.run(TOKEN)



