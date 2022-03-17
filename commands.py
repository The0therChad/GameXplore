from discord.ext import commands
from api import query_search, query_video

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

    @commands.command(name="video")
    @commands.cooldown(rate=1, per=2)
    async def video(self, ctx: commands.Context, *, text: str):
        """Get a selection of Youtube links based on selected game"""
        search_results = query_search("games", search=text)
        game_id = search_results[0]["id"]
        query_results = query_video(where=game_id)
        ids = []
        for item in query_results:
            ids.append(item["video_id"])
        if ids == []:
            await ctx.send("There are no videos for that game. :confused:")
        for id in ids:
            msg = f"https://www.youtube.com/watch?v={id}"
            await ctx.send(msg)

def setup(bot: commands.Bot):
    bot.add_cog(QueryCog(bot))