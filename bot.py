import discord
import os
import gemini_api as gp
#Secret key
TOKEN = os.environ.get('DISCORD_TOKEN')


class MyClient(discord.Client):
    async def on_ready(self):
        print(self.user+' is Online!')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
        if message.content == ('Hello'):
            await message.channel.send('Hii!')
        #Check if we are tagged
        if self.user in message.mentions:
            gp.convo.send_message(message.content)
            await message.channel.send(gp.convo.last.text)        
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)