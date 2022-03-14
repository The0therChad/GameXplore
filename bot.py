from discord.ext import commands

from settings import DISCORD

class NotificationCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @commands.command(name="test")
    async def test(self, ctx: commands.Context) -> None:
        await ctx.send("Jello!")

if __name__ == "__main__" and DISCORD is not None:
    bot = commands.Bot("!")
    bot.add_cog(NotificationCog(bot))
    bot.run(DISCORD)
