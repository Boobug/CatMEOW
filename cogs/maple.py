import discord
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks
from meow.kittify import get_avatar_image, parse_input_string


class Maple(commands.Cog, name="maple"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="maple",
        description="Pass something to me",
    )
    @checks.not_blacklisted()
    async def maple_command(self, context: Context, *, input_str: str) -> None:
        variables = get_avatar_image(parse_input_string(input_str))

        embed = discord.Embed(title="Maple Image", color=0xff0000)
        embed.set_image(url=variables)
        await context.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Maple(bot))
