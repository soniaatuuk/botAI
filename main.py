import discord
from discord.ext import commands
import os, random
from get_model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check (ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            nama_file = file.filename
            url_file = file.url
            await file.save(f'./{nama_file}')
            await ctx.send(f'file telah disimpan dengan nama {nama_file}')

            nama, skor = get_class(image=nama_file, model='keras_model.h5', label='labels.txt')

            # inferensi
            if nama == 'healthy food\n' and skor >=0.65:
                await ctx.send('Makanan ini termasuk kategori healthy food')
                await ctx.send('Makanan sehat kaya akan nutrisi seperti vitamin, mineral, dan serat yang baik untuk pencernaan')
                await ctx.send('Konsumsi makanan sehat secara rutin mengurangi resiko penyakit kronis')
                await ctx.send('Konsumsi makanan sehat membantu menjaga berat badan ideal karena rendah kalori dan lemak jenuh')
            if nama == 'fast food\n' and skor >=0.65:
                await ctx.send('Makanan ini tergolong fast food')
                await ctx.send('Fast food mengandung banyak kalori dan lemak yang bisa meningkatkan resiko obesitas')
                await ctx.send('Sering mengonsumsi fast food dapat menyebabkan masalah jantung dan tekanan darah tinggi')
                await ctx.send('Fast food dapat menyebabkan kenaikan berat badan cepat karena tinggi kalori dan lemak jenuh')
            else:
                await ctx.send('GAMBAR YANG DIKIRIM TIDAK DIKENALI')

    else:
        await ctx.send("TIDAK ADA FILE YANG DIKIRIMKAN")

bot.run('YOUR TOKEN')
