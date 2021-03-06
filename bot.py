import asyncio
import time
import discord
import pandas
import json
from discord.ext import commands
from graph import *
from dropbase import *
from settings import *

# discord gateway intents
intents = discord.Intents.default()
allowed_mentions = discord.AllowedMentions(everyone=False,
                                           users=True,
                                           roles=False)

# bot instance
bot = discord.ext.commands.Bot(command_prefix=prefix,
                               intents=intents,
                               description=description,
                               case_insensitive=True,
                               allowed_mentions=allowed_mentions)


@bot.command()
async def graph(ctx, graph_type):
    """
    {graph_type} Renders a desired graph type from a csv dataset
    """
    await ctx.send(f"Send a file to be a graphed. It must be a {', '.join(supported_file_types)}")

    def check(message):
        return message.author == ctx.author and len(message.attachments) == 1

    msg = discord.Message
    try:
        msg = await bot.wait_for('message', check=check, timeout=60)
    except asyncio.TimeoutError:
        await ctx.send('Timed out. Please try again')

    # check if file is supported
    # FIXME: check for all in the supported file types list, not just .csv
    if ".csv" not in msg.attachments[0].filename:
        await ctx.send(f"That's not a valid file type. It must be a {', '.join(supported_file_types)}")
    else:
        # saves with filename
        await msg.attachments[0].save("temp/file.csv")

        # run the pipeline job
        if graph_type.lower()[0:2] == 'yy':
            job = Job('X VS YY TABLE')
            job.run_pipeline()
            time.sleep(5)

            # saves query as temp json
            with open('temp/file.json', 'w', encoding='utf-8') as outfile:
                json.dump(database_query('x_vs_yy', 'x,y1,y2'), outfile,
                          ensure_ascii=False, indent=4)
        elif graph_type.lower()[0:2] == 'y-':
            job = Job('NAME VS COUNT TABLE')
            job.run_pipeline()
            time.sleep(5)

            # saves query as temp json
            with open('temp/file.json', 'w', encoding='utf-8') as outfile:
                json.dump(database_query('name_vs_count', 'name,count'),
                          outfile, ensure_ascii=False, indent=4)

        elif graph_type.lower() == 'geodot':
            job = Job('GEODOT TABLE')
            job.run_pipeline()
            time.sleep(5)

            # saves query as temp json
            with open('temp/file.json', 'w', encoding='utf-8') as outfile:
                json.dump(database_query('geodot', 'name,lat,lon'),
                          outfile, ensure_ascii=False, indent=4)

        elif graph_type.lower() == 'geospatial':
            job = Job('GEOSPATIAL TABLE')
            job.run_pipeline()
            time.sleep(10)

            # saves query as temp json
            with open('temp/file.json', 'w', encoding='utf-8') as outfile:
                json.dump(database_query('geospatial', 'lon_departure,lat_departure,lon_arrival,lat_arrival'),
                          outfile, ensure_ascii=False, indent=4)

        # converts json to csv
        file = pandas.read_json('temp/file.json')
        file.to_csv('temp/new_file.csv', index=False)

    if graph_type.lower() == 'yy-bar':
        # bar graph for csv
        basic_bar('temp/new_file.csv')
        await ctx.send(file=discord.File(open('temp/bar.png', 'rb'), 'bar.png'))

    elif graph_type.lower() == 'yy-line':
        # graphs the csv data
        basic_line('temp/new_file.csv')
        await ctx.send(file=discord.File(open('temp/Line.png', 'rb'), 'Line.png'))

    elif graph_type.lower() == 'yy-scatter':
        # graphs the csv data
        basic_scatter('temp/new_file.csv')
        await ctx.send(
            file=discord.File(open('temp/scatter.png', 'rb'), 'scatter.png'))

    elif graph_type.lower() == 'y-pie':
        basic_pie('temp/new_file.csv')
        await ctx.send(
            file=discord.File(open('temp/pie.png', 'rb'), 'pie.png'))

    elif graph_type.lower() == 'geodot':
        geo_dot('temp/new_file.csv')
        await ctx.send(
            file=discord.File(open('temp/map.png', 'rb'), 'map.png'))

    elif graph_type.lower() == 'geospatial':
        geo_spatial('temp/new_file.csv')
        await ctx.send(
            file=discord.File(open('temp/spatial.png', 'rb'), 'spatial.png'))


bot.run(os.getenv('BOT_TOKEN'))
