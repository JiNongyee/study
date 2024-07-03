import discord
from discord.ext import commands
import feedparser

# Discord 봇의 기본 인텐트(권한) 설정
intents = discord.Intents.default()
intents.message_content = True  # 메시지 내용 접근 권한 설정

class MyClient(discord.Client):
    # 봇이 준비되면 실행되는 이벤트 핸들러
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')  # 봇이 Discord에 연결되었음을 출력

    # 메시지가 도착하면 실행되는 이벤트 핸들러
    async def on_message(self, message):
        # 메시지 저자가 봇 자신이면 무시
        if message.author == self.user:
            return

        # 메시지 내용이 '!news'이면 실행
        if message.content.lower() == '!news':
            # RSS 피드 URL
            url = "http://www.boannews.com/media/news_rss.xml?mkind=1"
            # RSS 피드 파싱
            feed = feedparser.parse(url)

            # 최근 5개 뉴스 기사 정보 추출
            for entry in feed.entries[:5]:
                # Discord Embed 메시지 생성
                embed = discord.Embed(title=entry.title, url=entry.link, description=entry.description)
                embed.set_author(name=entry.author)
                # 채널에 Embed 메시지 전송
                await message.channel.send(embed=embed)

# Discord 봇 토큰
TOKEN = 'your_token

# Discord 봇 인스턴스 생성 및 실행
bot = MyClient(intents=intents)
bot.run(TOKEN)
