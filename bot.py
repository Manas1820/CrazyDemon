import requests
from bs4 import BeautifulSoup
import random
import numpy
import discord 
from discord.ext import commands,tasks
client = commands.Bot(command_prefix = '$')

TOKEN='' # your bot token

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

@client.command(aliases=['Quote','quotes','Quotes','quote'])
async def _quote(ctx):
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

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send('Invalid Request , You do not have the permission to proceed')
        pass   
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('Invalid Command , Please use $help to know more')
     

@client.command()
@commands.has_permissions(manage_messages=True)      
async def clear(ctx,amount:int):
    await ctx.channel.purge(limit=amount)

@clear.error
async def clear_error(ctx,error):
    if isinstance(error,commands.MissingRequiredArgument):
        await ctx.send('Please pass in all required argument')


@client.command()
async def assist(ctx):
    await ctx.send('''
     $assist - Displays all the function with its use .
    $quotes- Display Random quotes daily. 
    $clear int-clears the int amount of lines specified .
    $ping - to know the current ping
    ''')



client.run(TOKEN)




