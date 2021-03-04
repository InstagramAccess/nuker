import asyncio,datetime,functools,io,json,os,random,re 
import string
import urllib.parse
import urllib.request
import time
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4
import aiohttp,colorama,discord,numpy,requests
from PIL import Image
from colorama import Fore
from discord.ext import commands
from discord.utils import get
from gtts import gTTS

with open('config.json') as f:
    config = json.load(f)
token = config.get('token')
password = config.get('password')
prefix = config.get('prefix')
nitro_sniper = config.get('nitro_sniper')
stream_url = "https://www.twitch.tv/skeezaroo"
tts_language = "en"
__author__ = "lones"
start_time = datetime.datetime.utcnow()
loop = asyncio.get_event_loop()
languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]

m_numbers = [
    ":one:",
    ":two:",
    ":three:",
    ":four:",
    ":five:",
    ":six:"
]

m_offets = [
    (-1, -1),
    (0, -1),
    (1, -1),
    (-1, 0),
    (1, 0),
    (-1, 1),
    (0, 1),
    (1, 1)
]


def Init():
    token = config.get('token')
    try:
        vlone.run(token, bot=False, reconnect=True)
        os.system(f'title (Vlone Selfbot) - Version')
    except discord.errors.LoginFailure:
        print(f"{Fore.CYAN}[ERROR] {Fore.RED}Improper token has been passed" + Fore.RESET)
        os.system('pause >NUL')


class Login(discord.Client):
    async def on_connect(self):
        guilds = len(self.guilds)
        users = len(self.users)
        print("")
        print(f"Connected to: [{self.user.name}]")
        print(f"Token: {self.http.token}")
        print(f"Guilds: {guilds}")
        print(f"Users: {users}")
        print("-------------------------------")
        await self.logout()


def async_executor():
    def outer(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            thing = functools.partial(func, *args, **kwargs)
            return loop.run_in_executor(None, thing)

        return inner

    return outer

toe = config.get('token')

@async_executor()
def do_tts(message):
    f = io.BytesIO()
    tts = gTTS(text=message.lower(), lang=tts_language)
    tts.write_to_fp(f)
    f.seek(0)
    return f


def Dump(ctx):
    for member in ctx.guild.members:
        f = open(f'Images/{ctx.guild.id}-Dump.txt', 'a+')
        f.write(str(member.avatar_url) + '\n')


def Nitro():
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return f'https://discord.gift/{code}'


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor


def RandString():
    return "".join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(14, 32)))


colorama.init()
vlone = discord.Client()
vlone = commands.Bot(description='Vlone Selfbot', command_prefix=prefix, self_bot=True)
vlone.msgsniper = True
vlone.slotbot_sniper = True
vlone.giveaway_sniper = True
vlone.yui_kiss_user = None
vlone.yui_kiss_channel = None
vlone.yui_hug_user = None
vlone.yui_hug_channel = None
vlone.sniped_message_dict = {}
vlone.sniped_edited_message_dict = {}
vlone.copycat = None
vlone.remove_command('help')

@vlone.event
async def on_connect():
    Clear()
    if nitro_sniper == True:
        nitro = "Active"
    else:
        nitro = "Disabled"    
    print(f'''{Fore.RESET}

        
                                        {Fore.MAGENTA} ██▒   █▓{Fore.BLUE} ██▓    {Fore.MAGENTA} ▒█████  {Fore.BLUE} ███▄    █{Fore.MAGENTA} ▓█████ 
                                        {Fore.MAGENTA}▓██░   █▒{Fore.BLUE}▓██▒    {Fore.MAGENTA}▒██▒  ██▒{Fore.BLUE} ██ ▀█   █{Fore.MAGENTA} ▓█   ▀ 
                                        {Fore.MAGENTA} ▓██  █▒░{Fore.BLUE}▒██░    {Fore.MAGENTA}▒██░  ██▒{Fore.BLUE}▓██  ▀█ ██{Fore.MAGENTA}▒▒███   
                                        {Fore.MAGENTA}  ▒██ █░░{Fore.BLUE}▒██░    {Fore.MAGENTA}▒██   ██░{Fore.BLUE}▓██▒  ▐▌██{Fore.MAGENTA}▒▒▓█  ▄ 
                                        {Fore.MAGENTA}   ▒▀█░  {Fore.BLUE}░██████▒{Fore.MAGENTA}░ ████▓▒░{Fore.BLUE}▒██░   ▓██{Fore.MAGENTA}░░▒████▒
                                        {Fore.MAGENTA}   ░ ▐░  {Fore.BLUE}░ ▒░▓  ░{Fore.MAGENTA}░ ▒░▒░▒░ {Fore.BLUE}░ ▒░   ▒ ▒{Fore.MAGENTA} ░░ ▒░ ░
                                        {Fore.MAGENTA}   ░ ░░  {Fore.BLUE}░ ░ ▒  ░{Fore.MAGENTA}  ░ ▒ ▒░ {Fore.BLUE}░ ░░   ░ ▒{Fore.MAGENTA}░ ░ ░  ░
                                        {Fore.MAGENTA}     ░░  {Fore.BLUE}  ░ ░   {Fore.MAGENTA}░ ░ ░ ▒  {Fore.BLUE}   ░   ░ ░{Fore.MAGENTA}    ░   
                                        {Fore.MAGENTA}     ░   {Fore.BLUE}   ░  ░ {Fore.MAGENTA}   ░ ░   {Fore.BLUE}        ░ {Fore.MAGENTA}   ░  ░
                                        {Fore.MAGENTA}    ░    {Fore.BLUE}        {Fore.MAGENTA}         {Fore.BLUE}          {Fore.MAGENTA}       
                                                         
                                                                                
   

                        
                                        {Fore.MAGENTA}Logged in as    | {Fore.BLUE}{vlone.user.name}#{vlone.user.discriminator}
                                        {Fore.MAGENTA}ID:             | {Fore.BLUE}{vlone.user.id}
                                        {Fore.MAGENTA}Prefix          | {Fore.BLUE}{vlone.command_prefix}
                                        {Fore.MAGENTA}discord.gg/vlone discord.gg/lones
    '''+Fore.RESET)


def Clear():
    os.system('cls')


Clear()

@vlone.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        await ctx.send('[ERROR]: You\'re missing permission to execute this command', delete_after=3)
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"[ERROR]: Missing arguments: {error}", delete_after=3)
    elif isinstance(error, numpy.AxisError):
        await ctx.send('Invalid Image', delete_after=3)
    elif isinstance(error, discord.errors.Forbidden):
        await ctx.send(f"[ERROR]: 404 Forbidden Access: {error}", delete_after=3)
    elif "Cannot send an empty message" in error_str:
        await ctx.send('[ERROR]: Message contents cannot be null', delete_after=3)
    else:
        ctx.send(f'[ERROR]: {error_str}', delete_after=3)


@vlone.event
async def on_message_edit(before, after):
    await vlone.process_commands(after)


@vlone.event
async def on_message(message):
    if vlone.copycat is not None and vlone.copycat.id == message.author.id:
        await message.channel.send(chr(173) + message.content)

    def GiveawayData():
        print(
            f"{Fore.CYAN} - CHANNEL: {Fore.BLUE}[{message.channel}]"
            f"\n{Fore.CYAN} - SERVER: {Fore.BLUE}[{message.guild}]"
            + Fore.RESET)

    def SlotBotData():
        print(
            f"{Fore.CYAN} - CHANNEL: {Fore.BLUE}[{message.channel}]"
            f"\n{Fore.CYAN} - SERVER: {Fore.BLUE}[{message.guild}]"
            + Fore.RESET)

    def NitroData(elapsed, code):
        print(
            f"{Fore.CYAN} - CHANNEL: {Fore.BLUE}[{message.channel}]"
            f"\n{Fore.CYAN} - SERVER: {Fore.BLUE}[{message.guild}]"
            f"\n{Fore.CYAN} - AUTHOR: {Fore.BLUE}[{message.author}]"
            f"\n{Fore.CYAN} - ELAPSED: {Fore.BLUE}[{elapsed}]"
            f"\n{Fore.CYAN} - CODE: {Fore.BLUE}{code}"
            + Fore.RESET)

    time = datetime.datetime.now().strftime("%H:%M %p")
    if 'discord.gift/' in message.content:
        if nitro_sniper:
            start = datetime.datetime.now()
            code = re.search("discord.gift/(.*)", message.content).group(1)
            token = config.get('token')

            headers = {'Authorization': token}

            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            elapsed = datetime.datetime.now() - start
            elapsed = f'{elapsed.seconds}.{elapsed.microseconds}'

            if 'This gift has been redeemed already.' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Already Redeemed]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'subscription_plan' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Success]" + Fore.RESET)
                NitroData(elapsed, code)

            elif 'Unknown Gift Code' in r:
                print(""
                      f"\n{Fore.CYAN}[{time} - Nitro Unknown Gift Code]" + Fore.RESET)
                NitroData(elapsed, code)
        else:
            return

    if 'Someone just dropped' in message.content:
        if Murda.slotbot_sniper:
            if message.author.id == 788470631968145411:
                try:
                    await message.channel.send('~grab')
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - SlotBot Couldnt Grab]" + Fore.RESET)
                    SlotBotData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Slotbot Grabbed]" + Fore.RESET)
                SlotBotData()
        else:
            return

    if 'GIVEAWAY' in message.content:
        if vlone.giveaway_sniper:
            if message.author.id == 788470631968145411:
                try:
                    await message.add_reaction("🎉")
                except discord.errors.Forbidden:
                    print(""
                          f"\n{Fore.CYAN}[{time} - Giveaway Couldnt React]" + Fore.RESET)
                    GiveawayData()
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Sniped]" + Fore.RESET)
                GiveawayData()
        else:
            return

    if f'Congratulations <@{vlone.user.id}>' in message.content:
        if vlone.giveaway_sniper:
            if message.author.id == 788470631968145411:
                print(""
                      f"\n{Fore.CYAN}[{time} - Giveaway Won]" + Fore.RESET)
                GiveawayData()
        else:
            return

    await vlone.process_commands(message)

@vlone.command(pass_contex=True)
async def help1(ctx):
  await ctx.message.delete()
  e = discord.Embed(colour=discord.Colour.from_rgb(128,0,128), description="⸼ 𝐀𝐥𝐥 𝐨𝐟 𝐭𝐡𝐞 𝐜𝐨𝐦𝐦𝐚𝐧𝐝𝐬 ⸼", timestamp=ctx.message.created_at)
 
  e.set_author(name="Vlone Selfbot From 11lone", icon_url=ctx.author.avatar_url)
  e.add_field(name="**𝐏𝐢𝐧𝐠 🧪**", value="𝕾𝖍𝖔𝖜𝖘 𝖙𝖍𝖊 𝖇𝖔𝖙’𝖘 𝖑𝖆𝖙𝖊𝖓𝖈𝖞.", inline=False)
  e.add_field(name="**𝐏𝐮𝐫𝐠𝐞 🧪**", value="𝕻𝖚𝖗𝖌𝖊𝖘 𝖌𝖎𝖛𝖊𝖓 𝖆𝖒𝖔𝖚𝖓𝖙 𝖔𝖋 𝖒𝖊𝖘𝖘𝖆𝖌𝖊𝖘.", inline=False)
  e.add_field(name="**𝐒𝐩𝐚𝐦 🧪**", value="𝕾𝖕𝖆𝖒𝖘 𝖙𝖍𝖊 𝖌𝖎𝖛𝖊𝖓 𝖒𝖊𝖘𝖘𝖆𝖌𝖊.", inline=False)
  e.add_field(name="**𝐊𝐢𝐜𝐤 🧪**", 
  value="𝕶𝖎𝖈𝖐𝖘 𝖒𝖊𝖓𝖙𝖎𝖔𝖓𝖊𝖉 𝖚𝖘𝖊𝖗.",inline=False)
  e.add_field(name="**𝐁𝐚𝐧 🧪**",
  value="𝕭𝖆𝖓𝖘 𝖒𝖊𝖓𝖙𝖎𝖔𝖓𝖊𝖉 𝖚𝖘𝖊𝖗.",inline=False)
  e.add_field(name="**𝐀𝐯 🧪**",
  value="𝕸𝖊𝖓𝖙𝖎𝖔𝖓𝖊𝖉 𝖆𝖛𝖆𝖙𝖆𝖗", inline=False)
  e.set_thumbnail(url="https://images-ext-2.discordapp.net/external/4-BOisfOQ2S8Y6BPZbKWolnVenQAaU3YdJvP69nVZ-A/https/data.whicdn.com/images/320521679/original.gif")
  e.set_image(url="https://images-ext-1.discordapp.net/external/rrSWLkE5dF1PtT6lGQ0JRdaW_RgLQ3OUMZ6wd_5pO8Q/%3Ffit%3D549%252C309%26ssl%3D1/https/i2.wp.com/dailyreup.com/wp-content/uploads/2015/05/asap-rocky-lsd.gif")
  e.set_footer(text="(Vlone Selfbot) Finger on the trigger, take a tap just to kill a man ")

  await ctx.send(embed=e)

@vlone.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()    
    for x in range(amount):
        await ctx.send(message)


@vlone.command(pass_centex=True)
async def kick(ctx, member : discord.Member):
    await member.kick()
    await ctx.message.delete()


@vlone.command(pass_centex=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()


@vlone.command()
async def av(ctx, member: discord.Member):
        embed = discord.Embed(color = discord.Color.from_rgb(128,0,128), timestamp=ctx.message.created_at)
        embed.set_author(name=f"{member}'s AV") 
        embed.set_image(url='{}'.format(member.avatar_url))
        embed.set_footer(text=member.id)
        await ctx.send(embed=embed)
        await ctx.message.delete()

@vlone.command()
async def stream(ctx, *, text):
  await ctx.message.delete()
  await bot.change_presence(activity=discord.Streaming(url = "vlone on top", name = text))

@vlone.command()
async def game(ctx, *, text):
  await ctx.message.delete()
  await bot.change_presence(activity=discord.Game (name = text))


if __name__ == '__main__':
    Init()
