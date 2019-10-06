import asyncio
import discord
import datetime
import time

from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext import tasks, commands

description = 'Relatively simple music bot example'

bot = commands.Bot(command_prefix=commands.when_mentioned_or("--"), description=description)

bdobossDB = [["003000","060000","100000","140000","190000","230000"],
        ["คจาคาร์","นูเวอร์","คจาคาร์","คูทุม","คจาคาร์","คารานด้า","คารานด้า"],
        ["คารานด้า","คูทุม","0","นูเวอร์","0","นูเวอร์","คูทุม"],
        ["0","คจาคาร์ และ คารานด้า","คจาคาร์","คจาคาร์","คูทุม","คจาคาร์ และ คูทุม","คจาคาร์ และ คารานด้า"],
        ["นูเวอร์","คูทุม","คารานด้า","คูทุม","คจาคาร์","นูเวอร์ และ คารานด้า","นูเวอร์ และ คูทุม"],
        ["คจาคาร์","นูเวอร์","คูทุม","คจาคาร์ และ คารานด้า","นูเวอร์","กวินท์ และ มูลัคคา","คารานด้า"],
        ["โอฟิน","นูเวอร์ และ คูทุม","โอฟิน","คจาคาร์ และ นูเวอร์","โอฟิน","0","นูเวอร์ และ คูทุม"]]

"""
@tasks.loop(seconds=3)
async def fun():
    print('Looping')

fun.start()
"""

class BlackDesert(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command()
    async def bdoboss(ctx):
        print('BlackDesert class is runing!!')
        while True:
            x = datetime.datetime.now()
            numofday = int(x.strftime("%w"))
            """
            htime = x.strftime("%H")
            mtime = x.strftime("%M")
            stime = x.strftime("%S")
            """
            htime = oldhtime = x.strftime("%H")
            mtime = oldmtime = x.strftime("%M")
            stime = oldstime = x.strftime("%S")

            ihtime = int(oldhtime)
            imtime = int(oldmtime)
            if (imtime + 20) == 60:
                mtime = "00"
                if ihtime < 9:
                    htime = "0"+str(ihtime + 1)
                else:
                    htime = str(ihtime + 1)
                if (ihtime + 1) > 23:
                    htime = "00"
            else:
                mtime = str(imtime + 20)

            timeinboss = htime + mtime + stime
            """print(timeinboss)"""

            if timeinboss in bdobossDB[0]:
                indexinboss = bdobossDB[0].index(timeinboss)
                bossisborn = bdobossDB[indexinboss+1][numofday-1]
                if bossisborn != "0":
                    await ctx.send("@here" + " บอส " + bossisborn + " กำลังจะเกิดในอีก 20 นาที เวลา " + htime + ":" + mtime + ":" + stime + " นาฬิกา")
                    print('have 1 in DB')
                else:
                    print('have 0 in DB')
            else:
                """
                await ctx.send("ไม่มีบอสที่กำลังจะเกิดใน 20 นาทีนี้")
                print('No Boss in Time')
                """
            print("Now time is " + str(x.strftime("%X")) + " Time Check Boss born is " + htime + ":" + mtime + ":" + stime)

            ihtime = int(oldhtime)
            imtime = int(oldmtime)
            if (imtime + 10) == 60:
                mtime = "00"
                if ihtime < 9:
                    htime = "0"+str(ihtime + 1)
                else:
                    htime = str(ihtime + 1)
                if (ihtime + 1) > 23:
                    htime = "00"
            else:
                mtime = str(imtime + 10)

            timeinboss = htime + mtime + stime
            """print(timeinboss)"""

            if timeinboss in bdobossDB[0]:
                indexinboss = bdobossDB[0].index(timeinboss)
                bossisborn = bdobossDB[indexinboss+1][numofday-1]
                if bossisborn != "0":
                    await ctx.send("@here" + " บอส " + bossisborn + " กำลังจะเกิดในอีก 10 นาที เวลา " + htime + ":" + mtime + ":" + stime + " นาฬิกา")
                    print('have 1 in DB')
                else:
                    print('have 0 in DB')
            else:
                """
                await ctx.send("ไม่มีบอสที่กำลังจะเกิดใน 10 นาทีนี้")
                print('No Boss in Time')
                """
            print("Now time is " + str(x.strftime("%X")) + " Time Check Boss born is " + htime + ":" + mtime + ":" + stime)

            ihtime = int(oldhtime)
            imtime = int(oldmtime)
            if (imtime + 1) == 60:
                mtime = "00"
                if ihtime < 9:
                    htime = "0"+str(ihtime + 1)
                else:
                    htime = str(ihtime + 1)
                if (ihtime + 1) > 23:
                    htime = "00"
            else:
                mtime = str(imtime + 1)

            timeinboss = htime + mtime + stime
            """print(timeinboss)"""

            if timeinboss in bdobossDB[0]:
                indexinboss = bdobossDB[0].index(timeinboss)
                bossisborn = bdobossDB[indexinboss+1][numofday-1]
                if bossisborn != "0":
                    await ctx.send("@here" + " บอส " + bossisborn + " กำลังจะเกิดในอีก 1 นาที เวลา " + htime + ":" + mtime + ":" + stime + " นาฬิกา")
                    print('have 1 in DB')
                else:
                    print('have 0 in DB')
            else:
                """
                await ctx.send("ไม่มีบอสที่กำลังจะเกิดใน 1 นาทีนี้")
                print('No Boss in Time')
                """
            print("Now time is " + str(x.strftime("%X")) + " Time Check Boss born is " + htime + ":" + mtime + ":" + stime)
            print("-----------------------------------------------------------------")
            time.sleep(0.5)     

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    async def write(ctx, txt: str):
        """Adds text"""
        await ctx.send(txt)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')

bot.run('NTc3MTA1ODAyMjg5MDg2NDY0.XY0QBg.rjwlgeB74vZlLo_reFTPoNYO7eA')