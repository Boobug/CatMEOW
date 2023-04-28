import aiohttp
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
        description="Give me your IGN. Tell me if you want it to kittify, mount,"
                    " have it animated or hair color or any expression changes",
    )
    @checks.not_blacklisted()
    async def maple_command(self, context: Context, *, input_str: str) -> None:
        variables = get_avatar_image(parse_input_string(input_str))
        gif_name = input_str.replace(" ", "_") + ".gif"
        async with aiohttp.ClientSession() as session:
            async with session.get(variables) as resp:
                raw_gif = await resp.read()
                with open("temp.gif", "wb") as f:
                    f.write(raw_gif)
        gif = discord.File(fp=r"temp.gif", filename=gif_name)
        embed = discord.Embed(title="Maple Image", color=0xff0000)
        embed.set_image(url=f"attachment://{gif_name}")
        await context.send(embed=embed, file=gif)


async def setup(bot):
    await bot.add_cog(Maple(bot))
