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
                        for msg in messages:
                            await asyncio.sleep(0.7)
                            await msg.delete()
                    except Exception as e:
                        print(str(e))
                    await message.channel.send(f"Deleted {str(message.content)} message(s)", delete_after=3)
                elif message.content == "gc-leave-all":
                    for channel in self.private_channels:
                        if "Direct Message" not in str(channel):
                            await channel.leave()

    def __init__(self, token):
        super().__init__()
        self.add_events()
        self.run(token, bot=False)


if __name__ == "__main__":
    CleanUpClient(sys.argv[1])
