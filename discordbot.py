#インストールした discord.py を読み込む
import discord

#接続に必要(らしい)オブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログインしたことが通知される
    print('ますエビが入室しました！')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # 送り主がBotだった場合反応したくないので
    if client.user != message.author:
        # /dog と発言したら「ワンッ！」と返信する処理
        if message.content == '/dog':
            await message.channel.send('ワンッ！')

# OTU1MDYyMDAzMjQyNzkwOTIy.G7aBcy.VCZhbR-rwGcrxbZ1A-Vem_m-7FHG_L2texzEHk
client.run("TOKEN")
