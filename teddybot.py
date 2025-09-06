import discord, random, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True  # Needed to read message content
intents.guilds = True
intents.voice_states = True

client = commands.Bot(command_prefix="teddy.", intents=intents)

@client.event
async def on_ready():
    print("Teddy is ready for use!")
    await client.change_presence(activity=discord.Game(name="with my favorite chew toy!)"))
    
@client.event
async def on_member_join(member):
    print(member + " has joined the server.")

@client.event 
async def on_member_remove(member):
    print(member + " has left the server.")
    
@client.command(brief="Says Hello")
async def hello(ctx):
    await ctx.send("Hello friends I am Teddy I am here to make your lives easier.")

@client.command(brief="Check my internet connection")
async def ping(ctx):
    await ctx.send("My ping is: " + str(round(client.latency * 1000)) + "ms")

@client.command(brief="ask me a y/n question")
async def ask(ctx, *, question):
    responses = ["No", "Yes"]
    
    await ctx.send("Question: " + question + "\nAnswer: **" + random.choice(responses) + "**")

@client.command(breif="make me join the server")
async def join (ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    channel = ctx.author.voice.channel
    try:
        await channel.connect()
        await ctx.send("Woof I am back to assist you")
    except:
        pass

@client.command(brief="I get it you don't want me around")
async def leave(ctx):
    if (ctx.voice_client): 
        await ctx.guild.voice_client.disconnect() 
        await ctx.send('Bye its time for me to go')
    else: # But if it isn't
        await ctx.send("I'm not in a voice channel, lemme join first")

@client.command(brief="pick an RNRandomness league champ")
async def lolpick(ctx):
    champions = ["Aatrox", "Ahri", "Akali", "Akshan", "Alistar", "Amumu", "Anivia", "Annie", "Aphelios", "Ashe", "Aurelion Sol", "Azir", "Bard", "Blitzcrank", "Brand", "Braum", "Caitlyn", "Camile", "Cassiopeia", "Cho’Gath", "Corki", "Darius", "Diana", "Dr. Mundo", "Draven", "Ekko", "Elise", "Evelynn", "Ezreal", "Fiddlesticks", "Fiora", "Fizz", "Galio", "Gangplank", "Garen", "Gnar", "Gragas", "Graves", "Gwen", "Hecarim", "Heimerdinger", "Illaoi", "Irellia", "Ivern", "Janna", "Jarvan IV", "Jax", "Jayce", "Jhin", "Jinx", "Kai’Sa", "Kalista", "Karma", "Karthus", "Kassadin", "Katarina", "Kayle", "Kayn", "Kennen", "Kha’Zix", "Kindred", "Kled", "Kog’Maw", "LeBlanc", "Lee Sin", "Leona", "Lillia", "Lissandra", "Lucian", "Lulu", "Lux", "Malphite", "Malzahar", "Maokai", "Master Yi", "Miss Fortune", "Mordekaiser", "Morgana", "Nami", "Nasus", "Nautilus", "Neeko", "Nidalee", "Nocturne", "Nunu & Willump", "Olaf", "Oriana", "Ornn", "Pantheon", "Poppy", "Pyke", "Qiyana", "Quinn", "Rakan", "Rammus", "Rek’Sai", "Rell", "Renekton", "Rengar", "Riven", "Rumble", "Ryze", "Samira", "Sejuani", "Senna", "Seraphine", "Sett", "Shaco", "Shen", "Shyvana", "Singed", "Sion", "Sivir", "Skarner", "Sona", "Soraka", "Swain", "Sylas", "Syndra", "Tahm Kench", "Tayilah", "Talon", "Taric", "Teemo", "Thresh", "Tristana", "Trundle", "Tryndamere", "Twisted Fate", "Twitch", "Udyr", "Urgot", "Varus", "Vayne", "Veigar", "Vex", "Vel’Koz", "Vi", "Viktor", "Viego", "Vladimir", "Volibear", "Warwick", "Wukong", "Xayah", "Xerath", "Xin Zhao", "Yasuo", "Yone", "Yorick", "Yuumi", "Zac", "Zed", "Ziggs", "Zilean", "Zoe", "Zyra"]

    await ctx.send("The Champion you got from RNRandomness picker is **" + random.choice(champions) + "**")

@client.command(brief="Pick a game for the gang to play")
async def gamepick(ctx):

    games = ["League of Legends", "Valorant", "Rocket League", "Brawlhala", "Jackbox TV", "Krunker"]

    await ctx.send("The game we are playing is **" + random.choice(games) + "**")

client.run(DISCORD_TOKEN)

