from discord.ext import commands
from api import query_search

class QueryCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @commands.command(name="test")
    async def test(self, ctx: commands.Context) -> None:
        await ctx.send("Jello!")

    @commands.command(name="search")
    @commands.cooldown(rate=1, per=2)
    async def search(self, ctx: commands.Context, *, text: str):
        """Search the API for games by name."""
        search_results = query_search("games", search=text)
        names = []
        for item in search_results:
            names.append(item["name"])
        msg = ""
        place = 1
        for name in names:
            msg = msg + f"{place}. {name}\n"
            place += 1
        await ctx.send(msg)

def setup(bot: commands.Bot):
    bot.add_cog(QueryCog(bot))