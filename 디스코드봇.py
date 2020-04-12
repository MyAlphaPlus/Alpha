import discord
import time
import os
from discord.ext import commands
import random
notice = list()
notice = list()
bot = commands.Bot(command_prefix='<')
client = discord.Client()


@bot.event
async def on_ready():
    print(f'로그인 성공: {bot.user.name}!')
    game = discord.Game("<도움")
    await bot.change_presence(status=discord.Status.online, activity=game)
@bot.command()
async def 공지(msg, *, text:str):
    if msg.author.id == 548749468514648078:
        for i in notice:
            channel = bot.get_channel(i)
            await channel.send(text)
        await msg.send("공지 완료!")

@bot.command()
async def 공지채널설정(msg):
    if msg.channel.id in notice:
        await msg.send('이미 등록됨')
    else:
        notice.append(msg.channel.id)
        await msg.send(f'<#{msg.channel.id}> 채널에 공지가 올거에요')
@bot.command()
async def 공지채널삭제(msg):
    if msg.channel.id not in notice:
        await msg.send('원래 공지채널이 아니였는데;;')
    else:
        notice.remove(msg.channel.id)
        await msg.send(f'<#{msg.channel.id}> 채널에 이제 공지가 오지 않을거에요')

@bot.command()
async def 도움(ctx):
    embed = discord.Embed(title="<도움", description="<제작자\n<말해\n<주의사항\n<초대링크\n<만세\n<정보", color=0x00ff00)
    await ctx.channel.send(embed=embed)
    embed = discord.Embed(title="서버 관리자용 커맨드", description="<공지채널설정\n<공지채널삭제", color=0x00ff00)
    await ctx.channel.send(embed=embed)
@bot.command()
async def 말해(ctx):
    ran = random.randint(1, 5)
    if ran == 1:
        {
           await ctx.channel.send('싫은데')
        }
    elif ran == 2:
        {
            await ctx.channel.send('왜? 심심해?')
        }
    elif ran == 3:
        {
            await ctx.channel.send('(뭘 말할지 생각중....)')
        }
    elif ran == 4:
        {
            await ctx.channel.send('어...?')
        }
    elif ran == 5:
        {
            await ctx.channel.send('알파 만세!')
        }
@bot.command()
async def 제작자(ctx):
    embed = discord.Embed(title="제작자",description="총 제작 : 알파\n수련님(프로필 사진 그려주심)\n 미니박스님(봇 만드는데 도움 주심)",color=0x00ffff)
    await ctx.channel.send(embed=embed)
@bot.command()
async def 주의사항(ctx):
    embed = discord.Embed(title="※주의사항※", description="알파를 팔로우하고 알파의 프로젝트에 좋아요 즐겨찾기를 누를것\n아직 개발중이여서 꺼졌다 켜졌다 할수 있음",color=0x00ffff)
    await ctx.channel.send(embed=embed)
@bot.command()
async def 초대링크(ctx):
    embed = discord.Embed(title="초대",description="다음 링크로 봇 초대\nhttps://discordapp.com/oauth2/authorize?client_id=698409750173450331&scope=bot",color=0x00ffff)
    await ctx.channel.send(embed=embed)
@bot.command()
async def 만세(ctx):
    ran = random.randint(1, 2)
    if ran == 1:
        {
            await ctx.channel.send('알파 만세!')
        }
    elif ran == 2:
        {
            await ctx.channel.send('푸딩 만세!')
        }
@bot.command()
async def 정보(ctx):
    embed = discord.Embed(title="푸딩", description="푸딩. 그냥 쓰자\n 함께하는 유저 수 : " + str(len(bot.users)), color=0x00ffff)
    await ctx.channel.send(embed=embed)
@bot.command()
async def 디엠(ctx, user:discord.Member, *, text:str):
    if ctx.author.id == 548749468514648078:
       await user.send("푸딩 관리자로부터 온 DM : "+ str(text))
       await ctx.send("보내기 완료!")
       time.sleep(1)
       await ctx.channel.purge(limit=2)
    else:
        await ctx.send("디엠 기능은 관리자만 사용할수 있습니다!")
@bot.command()
async def 서버목록(msg):
    for i in bot.guilds:
        await msg.send(i)
access_token = os.environ["BotToken"]
bot.run(access_token)
