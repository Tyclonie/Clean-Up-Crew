import sys
import discord
import asyncio

class CleanUpClient(discord.Client):
    def add_events(self):
        @self.event
        async def on_ready():
            print(f"Logged in as {self.user}")

        @self.event
        async def on_message(message):
            if message.author == self.user:
                if "a" not in message.content.lower() and "e" not in message.content.lower() and "i" not in message.content.lower() and "o" not in message.content.lower() and "u" not in message.content.lower():
                    await message.delete()
                    try:
                        messages = await message.channel.history(limit=int(message.content)).flatten()
                        for m in messages:
                            await asyncio.sleep(0.7)
                            await m.delete()
                    except Exception as e:
                        print(str(e))
                    await message.channel.send(f"Deleted {str(message.content)} message(s)", delete_after=3)

    def __init__(self, token):
        super().__init__()
        self.add_events()
        self.run(token, bot=False)

if __name__ == "__main__":
    CleanUpClient(sys.argv[1])
