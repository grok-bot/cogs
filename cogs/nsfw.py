'''
ここから入らんとする者は一切の希望を放棄せよ
DON'T COME CRYING WHEN YOU GET BANNED FOR ABUSING THIS COMMAND.
USE OR ABUSE RESTS SOLELY UPON THE USER, AND ANY ACTION TAKEN
BY ANY MODS, ADMINS, GUILD OWNERS, OR DISCORD STUFF TO SUSPEND
OR PERMABAN AN ACCOUNT HAS NOTHING TO DO WITH ME. I SIMPLY PFOVIDE
THESE COMMANDS FOR EDUCATIONAL AND ENTERTAINMENT PURPOSES ONLY.
'''

import discord
from discord.ext import commands
import bs4 as bs
import urllib.request
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

from lxml import etree
from ext import embedtobox
from PIL import Image
import random
# import requests
import pip
import os
import io
import colorthief

"""Nsfw commands."""

class Nsfw:
    def __init__(self, bot):
        self.bot = bot
        self.session = discord.http.HTTPClient

    # Here are the commands, just make sure you use them
    # inside NSFW channels. And since they are random, well
    # they don't always show bobs or veganas... keep trying.

    @commands.command(aliases=['konachan'])
    async def kona(self, ctx):
        """Random image from Konachan"""
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass

            await ctx.channel.trigger_typing()
            # For some effedup reason, some fields must have " instead of ',
            # learn to live with it.
            query = urllib.request.urlopen("https://konachan.com/post/random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            sans = soup.find_all('div', {'class': 'highres-show'})
            partial = soup.find(id="highres").get("href")
            image = 'https:' + partial
            # If we made it here, then we have all the info required for the embed
            em = discord.Embed()
            # Also, if you don't have colorthief this won't work !!!
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.description = f'[Full Size Link*]({image})'
            em.set_image(url=image)
            em.set_footer(text='* click link at your own risk!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                em_list = await embedtobox.etb(em)
                for page in em_list:
                    await ctx.send(page)
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'konachan.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            # This is for debug purposes, if you get an error, you've messed the code
            await ctx.send(f'```{e}```', delete_after=5)

    @commands.command()
    async def gelbooru(self, ctx):
        """Random image from Gelbooru"""
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass

            await ctx.channel.trigger_typing()
            query = urllib.request.urlopen("http://www.gelbooru.com/index.php?page=post&s=random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            sans = soup.find_all('div', {'class': 'highres-show'})
            partial = soup.find(id="image").get("src")
            image = partial.replace('//', '/').replace(':/', '://')

            em = discord.Embed()
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.description = f'[Full Size Link*]({image})'
            em.set_image(url=image)
            em.set_footer(text='* click link at your own risk!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                em_list = await embedtobox.etb(em)
                for page in em_list:
                    await ctx.send(page)
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'gelbooru.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            await ctx.send(f'```{e}```')

    @commands.command()
    async def tbib(self, ctx):
        """Random image from TbIb"""
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass

            await ctx.channel.trigger_typing()
            query = urllib.request.urlopen("http://www.tbib.org/index.php?page=post&s=random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            sans = soup.find_all('div', {'class': 'highres-show'})
            partial = soup.find(id="image").get("src")
            image = 'https:' + partial
            last = str(image.split('?')[-2]).replace('//', '/').replace(':/', '://')
            # Whew, that last part is ugly sf, but it works !!
            em = discord.Embed()
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.description = f'[Full Size Link*]({last})'
            em.set_image(url=last)
            em.set_footer(text='* click link at your own risk!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                em_list = await embedtobox.etb(em)
                for page in em_list:
                    await ctx.send(page)
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'tbib.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            await ctx.send(f'```{e}```')

   @commands.command(no_pm=True)
    async def xbooru(self, ctx):
        """Random image from Xbooru"""
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass

            await ctx.channel.trigger_typing()
            query = urllib.request.urlopen("http://xbooru.com/index.php?page=post&s=random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            sans = soup.find_all('div', {'class': 'highres-show'})
            image = soup.find(id="image").get("src")
            last = str(image.split('?')[-2]).replace('//', '/').replace(':/', '://')
            em = discord.Embed()
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.description = f'[Full Size Link*]({last})'
            em.set_image(url=last)
            em.set_footer(text='* click link at your own risk!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                em_list = await embedtobox.etb(em)
                for page in em_list:
                    await ctx.send(page)
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'xbooru.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            await ctx.send(f'```{e}```')

    @commands.command(aliases=['r34'], no_pm=True)
    async def rule34(self, ctx):
        """Random image from rule34"""
        try:
            try:
                await ctx.message.delete()
            except discord.Forbidden:
                pass

            await ctx.channel.trigger_typing()
            query = urllib.request.urlopen("http://rule34.xxx/index.php?page=post&s=random").read()
            soup = bs.BeautifulSoup(query, 'html.parser')
            sans = soup.find_all('div', {'class': 'highres-show'})
            partial = soup.find(id="image").get("src")
            image = 'https:' + partial
            last = str(image.split('?')[-2]).replace('//', '/').replace(':/', '://')

            em = discord.Embed()
            em.color = await ctx.get_dominant_color(url=ctx.author.avatar_url)
            em.description = f'[Full Size Link*]({last})'
            em.set_image(url=last)
            em.set_footer(text='* click link at your own risk!')
            try:
                await ctx.send(embed=em)
            except discord.HTTPException:
                em_list = await embedtobox.etb(em)
                for page in em_list:
                    await ctx.send(page)
                try:
                    async with ctx.session.get(image) as resp:
                        image = await resp.read()
                    with io.BytesIO(image) as file:
                        await ctx.send(file=discord.File(file, 'rule34.png'))
                except discord.HTTPException:
                    await ctx.send(image)

        except Exception as e:
            await ctx.send(f'```{e}```')

        
def setup(bot):
    return bot.add_cog(Nsfw(bot))
