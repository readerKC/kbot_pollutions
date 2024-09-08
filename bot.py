import discord
import random,os
from discord.ext import commands

def cevaplar ():
    random_cevap = random.randint(1,4)
    if random_cevap == 1:
        return 'Sosyal medyada bu konu hakkında bilgilendirici paylaşımlar yapabilirsiniz.'
    if random_cevap == 2:
        return 'Arkadaşlarımızla birlikte sokaktaki çöpleri toplayabiliriz. Yardımın büyüğü küçüğü olmaz.'
    if random_cevap == 3:
        return 'Çevreyi kirleten şirketleri protesto edebiliriz.'
    if random_cevap == 4:
        return 'Ağaç dikerek çevre sorunlarının azalmasında yardımcı olabiliriz'

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send("Selam")

@bot.command()
async def pollution(ctx):
    await ctx.send(f'Çevre kirliliği hakkında şunu yapabliriz: {cevaplar()}')

@bot.command()
async def pollutionphoto(ctx):
  folder_item = os.listdir('images')
  img = random.choice(folder_item)

  with open(f'images/{img}', 'rb') as f:
        picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def neyapmali(ctx):
  folder_item2 = os.listdir('images-2')
  img2 = random.choice(folder_item2)

  with open(f'images-2/{img2}', 'rb') as f:
        picture2 = discord.File(f)
        await ctx.send(file=picture2)


@bot.command()
async def khelp(ctx):
    with open('file.txt', 'r', encoding = 'UTF-8') as f:
        print(f.read())



bot.run("")
