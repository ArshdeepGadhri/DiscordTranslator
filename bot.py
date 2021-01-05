import discord
from discord.ext import commands
import translators as ts
from config import params
import asyncio

bot = commands.Bot(command_prefix=params["prefix"], help_command=None, self_bot=True)

@bot.event
async def on_connect():
    print(f"Logged in as {bot.user.name}#{bot.user.discriminator}")


class SelfBot(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["tran", "tr"]) 
    async def translate(self, ctx, *args):
        await asyncio.sleep(0.35)
        await ctx.message.delete()
        args = ' '.join(args).split(" ", 2)
        try:
            if args[0] != "auto" and args[1] != "auto":
                msg = ts.google(args[2], from_language=args[0], to_language=args[1])
            elif args[0] == "auto" and args[1] != "auto":
                msg = ts.google(args[2], to_language=args[1])
            elif args[0] != "auto" and args[1] == "auto":
                msg = ts.google(args[2], from_language=args[1])
            else:
                msg = ts.google(args[2])
            await ctx.send(msg)
        except:
            print("Error")
    

def main():
    bot.add_cog(SelfBot(bot))
    bot.run(params["token"], bot=False)


if __name__ == "__main__":
    main()