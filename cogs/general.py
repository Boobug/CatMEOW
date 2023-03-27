""""
Copyright © Krypton 2019-2023 - https://github.com/kkrypt0nn (https://krypton.ninja)
Description:
🐍 A simple template to start to code your own and personalized discord bot in Python programming language.

Version: 5.5.0
"""


import platform
import random
import re
import requests
import re
from bs4 import BeautifulSoup
import aiohttp
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import Context

from helpers import checks

class General(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command(
        name="help", description="List all commands the bot has loaded."
    )
    @checks.not_blacklisted()
    async def help(self, context: Context) -> None:
        prefix = self.bot.config["prefix"]
        embed = discord.Embed(
            title="Help", description="List of available commands:", color=0x9C84EF
        )
        for i in self.bot.cogs:
            cog = self.bot.get_cog(i.lower())
            commands = cog.get_commands()
            data = []
            for command in commands:
                description = command.description.partition("\n")[0]
                data.append(f"{prefix}{command.name} - {description}")
            help_text = "\n".join(data)
            embed.add_field(
                name=i.capitalize(), value=f"```{help_text}```", inline=False
            )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="botinfo",
        description="Get some useful (or not) information about the bot.",
    )
    @checks.not_blacklisted()
    async def botinfo(self, context: Context) -> None:
        """
        Get some useful (or not) information about the bot.
        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description="Used [Krypton's](https://krypton.ninja) template",
            color=0x9C84EF,
        )
        embed.set_author(name="Bot Information")
        embed.add_field(name="Owner:", value="Krypton#7331", inline=True)
        embed.add_field(
            name="Python Version:", value=f"{platform.python_version()}", inline=True
        )
        embed.add_field(
            name="Prefix:",
            value=f"/ (Slash Commands) or {self.bot.config['prefix']} for normal commands",
            inline=False,
        )
        embed.set_footer(text=f"Requested by {context.author}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="serverinfo",
        description="Get some useful (or not) information about the server.",
    )
    @checks.not_blacklisted()
    async def serverinfo(self, context: Context) -> None:
        """
        Get some useful (or not) information about the server.
        :param context: The hybrid command context.
        """
        roles = [role.name for role in context.guild.roles]
        if len(roles) > 50:
            roles = roles[:50]
            roles.append(f">>>> Displaying[50/{len(roles)}] Roles")
        roles = ", ".join(roles)

        embed = discord.Embed(
            title="**Server Name:**", description=f"{context.guild}", color=0x9C84EF
        )
        if context.guild.icon is not None:
            embed.set_thumbnail(url=context.guild.icon.url)
        embed.add_field(name="Server ID", value=context.guild.id)
        embed.add_field(name="Member Count", value=context.guild.member_count)
        embed.add_field(
            name="Text/Voice Channels", value=f"{len(context.guild.channels)}"
        )
        embed.add_field(name=f"Roles ({len(context.guild.roles)})", value=roles)
        embed.set_footer(text=f"Created at: {context.guild.created_at}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="ping",
        description="Check if the bot is alive.",
    )
    @checks.not_blacklisted()
    async def ping(self, context: Context) -> None:
        """
        Check if the bot is alive.
        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            title="🏓 Pong!",
            description=f"The bot latency is {round(self.bot.latency * 1000)}ms.",
            color=0x9C84EF,
        )
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="invite",
        description="Get the invite link of the bot to be able to invite it.",
    )
    @checks.not_blacklisted()
    async def invite(self, context: Context) -> None:
        """
        Get the invite link of the bot to be able to invite it.
        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"Invite me by clicking [here](https://discordapp.com/oauth2/authorize?&client_id={self.bot.config['application_id']}&scope=bot+applications.commands&permissions={self.bot.config['permissions']}).",
            color=0xD75BF4,
        )
        try:
            # To know what permissions to give to your bot, please see here: https://discordapi.com/permissions.html and remember to not give Administrator permissions.
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except discord.Forbidden:
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="server",
        description="Get the invite link of the discord server of the bot for some support.",
    )
    @checks.not_blacklisted()
    async def server(self, context: Context) -> None:
        """
        Get the invite link of the discord server of the bot for some support.
        :param context: The hybrid command context.
        """
        embed = discord.Embed(
            description=f"Join the support server for the bot by clicking [here](https://discord.gg/mTBrXyWxAF).",
            color=0xD75BF4,
        )
        try:
            await context.author.send(embed=embed)
            await context.send("I sent you a private message!")
        except discord.Forbidden:
            await context.send(embed=embed)

    @commands.hybrid_command(
        name="8ball",
        description="Ask any question to the bot.",
    )
    @checks.not_blacklisted()
    @app_commands.describe(question="The question you want to ask.")
    async def eight_ball(self, context: Context, *, question: str) -> None:
        """
        Ask any question to the bot.
        :param context: The hybrid command context.
        :param question: The question that should be asked by the user.
        """
        answers = [
            "It is certain.",
            "It is decidedly so.",
            "You may rely on it.",
            "Without a doubt.",
            "Yes - definitely.",
            "As I see, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again later.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        ]
        embed = discord.Embed(
            title="**My Answer:**",
            description=f"{random.choice(answers)}",
            color=0x9C84EF,
        )
        embed.set_footer(text=f"The question was: {question}")
        await context.send(embed=embed)

    @commands.hybrid_command(
        name="bitcoin",
        description="Get the current price of bitcoin.",
    )
    @checks.not_blacklisted()
    async def bitcoin(self, context: Context) -> None:
        """
        Get the current price of bitcoin.
        :param context: The hybrid command context.
        """
        # This will prevent your bot from stopping everything when doing a web request - see: https://discordpy.readthedocs.io/en/stable/faq.html#how-do-i-make-a-web-request
        async with aiohttp.ClientSession() as session:
            async with session.get(
                "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
            ) as request:
                if request.status == 200:
                    data = await request.json(
                        content_type="application/javascript"
                    )  # For some reason the returned content is of type JavaScript
                    embed = discord.Embed(
                        title="Bitcoin price",
                        description=f"The current price is {data['bpi']['USD']['rate']} :dollar:",
                        color=0x9C84EF,
                    )
                else:
                    embed = discord.Embed(
                        title="Error!",
                        description="There is something wrong with the API, please try again later",
                        color=0xE02B2B,
                    )
                await context.send(embed=embed)





    @commands.hybrid_command(
        name="maple",
        description="Pass something to me",
    )
    @checks.not_blacklisted()

    async def maple_command(self, context: Context, *, input_str: str) -> None:
        
        def get_response(legends_url):
            # """
            # Function that takes in a URL as a parameter, sends a GET request to the URL using the requests module, 
            # and returns the URL of the response received.
            
            # Parameters:
            # legends_url (str): URL of the website to which the GET request is to be sent
            
            # Returns:
            # str: URL of the response received
            # """
            
            # Send a GET request to the given URL and store the response in a variable called 'response'
            response = requests.get(legends_url)
            
            # Return the URL of the response received
            return response.url

        def check_valid_url(url):
            # """
            # Function that takes in a URL as a parameter, sends a GET request to the URL using the requests module, 
            # and checks if the response is a valid image file (JPEG, PNG or GIF). Returns True if the URL is valid 
            # and points to an image file, and False otherwise.
            
            # Parameters:
            # url (str): URL of the image file to be checked
            
            # Returns:
            # bool: True if the URL is valid and points to an image file, False otherwise
            # """
            
            try:
                # Send a GET request to the given URL and store the response in a variable called 'response'
                response = requests.get(url)
                
                # Check if the status code of the response is 200 (OK)
                if response.status_code == 200:
                    
                    # Check if the content type of the response is an image file (JPEG, PNG or GIF)
                    if response.headers.get('content-type') in ['image/jpeg', 'image/png', 'image/gif']:
                        return True  # Return True if the URL points to a valid image file
                    else:
                        return False  # Return False if the URL points to a file that is not an image
                        
                else:
                    return False  # Return False if the GET request was not successful (status code other than 200)
            
            except:
                return False  # Return False if there was an error while sending the GET request or processing the response



        def detect_emotion(emotion_str):
            # """
            # Function that takes in a string representing an emotion and returns an integer code for the emotion. 
            # If the input string matches a pre-defined keyword for an emotion, the corresponding integer code is returned. 
            # If the input string matches a specific pattern, it is assumed to be a custom emotion code and is returned as an integer.
            # If the input string does not match any of the predefined emotions or the custom pattern, False is returned.
            
            # Parameters:
            # emotion_str (str): String representation of the emotion to be detected
            
            # Returns:
            # int or False: Integer code for the emotion, or False if the input string does not match any predefined emotion or pattern
            # """
            
            # Check if the input string matches the pattern for custom emotion codes (starting with the letter 'f')
            if re.match(r'^f[1-9]\d*$', emotion_str):
                # If so, extract the numeral and return it as an integer
                return int(emotion_str[1:])

            # Check if the input string matches any of the emotion keywords
            emotion_str = emotion_str.lower()
            if emotion_str == "default":
                return 0
            elif emotion_str == "hit":
                return 1
            elif emotion_str == "smile":
                return 2
            elif emotion_str == "troubled":
                return 3
            elif emotion_str == "cry":
                return 4
            elif emotion_str == "angry":
                return 5
            elif emotion_str == "bewildered":
                return 6
            elif emotion_str == "stunned":
                return 7
            elif emotion_str == "queasy":
                return 8
            elif emotion_str == "flaming":
                return 9
            elif emotion_str == "whoa":
                return 10
            elif emotion_str == "ray":
                return 11
            elif emotion_str == "panicky":
                return 12
            elif emotion_str == "sweetness":
                return 13
            elif emotion_str == "sparkling":
                return 14
            elif emotion_str == "goo":
                return 15
            elif emotion_str == "smoochies":
                return 16
            elif emotion_str == "wink":
                return 17
            elif emotion_str == "ouch":
                return 18
            elif emotion_str == "bowing":
                return 19
            elif emotion_str == "bleh":
                return 20
            elif emotion_str == "dragon":
                return 21
            elif emotion_str == "constant":
                return 22

            # If no match is found, return False
            return False





        def get_gender(name):
            # """
            # Function that takes in a Maple Legends character name as a string and returns the gender of the character.
            
            # Parameters:
            # name (str): The name of the Maple Legends character whose gender is to be determined
            
            # Returns:
            # str: The gender of the character with the given name, as determined by the Maple Legends API. If the gender cannot
            #      be determined, the function returns "female" by default.
            # """
            url = f"https://maplelegends.com/api/character?name={name}"  # Constructing the URL for the API call
            response = requests.get(url)  # Sending a GET request to the API and storing the response
            data = response.json()  # Parsing the response data into a JSON object
            try:
                gender = data["gender"]  # Extracting the gender of the character from the JSON data
            except KeyError:
                gender = "female"  # If the gender field is not found in the JSON data, default to "female"
            return gender  # Return the gender of the character as a string




        def replace_item_id(link, replacement):
            # """
            # Function that takes in a Maple Legends item link as a string and replaces the first 4 digits of the item ID with a new
            # set of digits.
            
            # Parameters:
            # link (str): The Maple Legends item link whose item ID is to be replaced
            # replacement (str): The new 4-digit prefix to use for the item ID
            
            # Returns:
            # str: The updated Maple Legends item link with the first 4 digits of the item ID replaced with the given prefix. If
            #      the link does not contain a valid item ID, the function returns the original link unchanged.
            # """
            # Find the index of the first occurrence of "itemId"
            start_index = link.find("itemId")
            if start_index == -1:
                return link  # "itemId" not found in link
            # Find the index of the colon (:) after "itemId"
            colon_index = link.find(":", start_index)
            if colon_index == -1:
                return link  # Colon not found after "itemId"
            # Find the index of the comma (,) after the colon
            comma_index = link.find(",", colon_index)
            if comma_index == -1:
                return link  # Comma not found after colon
            # Extract the item ID and replace the first 4 digits
            item_id = link[colon_index+1:comma_index].strip()  # Extracting the item ID from the link
            new_id = replacement + item_id[4:]  # Constructing the new item ID with the given replacement prefix
            # Construct the new link with the replaced item ID
            return link[:colon_index+1] + new_id + link[comma_index:]


        def replace_last_digit(url, new_digit):
            # Find the index of the first occurrence of "itemId"
            item_id_index = url.find("itemId")

            # If "itemId" is not found, return the original URL
            if item_id_index == -1:
                return url

            # Find the start index of the 5-digit number
            start_index = url.find(":", item_id_index) + 1

            # Find the end index of the 5-digit number
            end_index = url.find(",", start_index)

            # If the end index is not found, use the end of the string
            if end_index == -1:
                end_index = len(url)

            # Get the 5-digit number and replace the last digit
            number = url[start_index:end_index]
            new_number = number[:-1] + str(new_digit)

            # Replace the old number with the new number in the URL
            return url[:start_index] + new_number + url[end_index:]


        def get_optional_arg(url_str, arg_name):
            arg_value = re.findall(fr'{arg_name}=([^&]*)', url_str, re.IGNORECASE)
            return arg_value[0] if arg_value else None


        def hair_color_changing(url, color):
            color_dict = {
                'BLACK': 0,
                'RED': 1,
                'ORANGE': 2,
                'WHITE': 2,
                'BLONDE': 3,
                'GREEN': 4,
                'BLUE': 5,
                'PURPLE': 6,
                'BROWN': 7,
                0: 'BLACK',
                1: 'RED',
                2: 'WHITE',
                3: 'BLONDE',
                4: 'GREEN',
                5: 'BLUE',
                6: 'PURPLE',
                7: 'BROWN'
            }
            if isinstance(color, str):
                color_str = color.upper()
                if color_str not in color_dict:
                    raise ValueError(f'Invalid color: {color}')
                color_code = color_dict[color_str]
            elif isinstance(color, int):
                if color not in color_dict:
                    raise ValueError(f'Invalid color code: {color}')
                color_code = color
            else:
                raise TypeError(f'Invalid color type: {type(color)}')

            new_url = replace_last_digit(url, color_code)

            try:
                response = requests.get(new_url)
                response.raise_for_status()
            except (requests.exceptions.HTTPError, requests.exceptions.RequestException) as e:
                raise ValueError(f'Invalid URL or image not found: {new_url}') from e

            return new_url




        def hair_color_detect(color_str):
            color_dict = {
                'BLACK': 0,
                'RED': 1,
                'ORANGE': 2,
                'WHITE': 2,
                'BLONDE': 3,
                'GREEN': 4,
                'BLUE': 5,
                'PURPLE': 6,
                'BROWN': 7
            }
            regex_keys = [key for key in color_dict.keys() if isinstance(key, str)]
            regex = re.compile('|'.join(regex_keys), re.IGNORECASE)
            matches = regex.findall(color_str)
            if not matches:
                return False
            color_code = color_dict[matches[0].upper()]
            return color_code




        def kittifying(url,ign_now):
            #let's combine everything nicely above
            if get_gender(ign_now) == 'female':
                hair_digit_4 = '3445'
            else:
                hair_digit_4 = '3343'
            return replace_item_id(url, hair_digit_4)


        ##this is the start of all the important request and url edits##



        def get_avatar_image(input_str):
            variables = parse_input_string(input_str)
            ign = variables['ign']
            mount = variables['mount']
            animated = variables['animated']
            hair_color_change = variables['hair_color_change']
            detect_emotion_val = variables['detect_emotion']
            kittified = variables['kittify']
            # Create the URL string with the variables
            url = f'https://maplelegends.com/api/getavatar?name={ign}&mount={mount}&animated={animated}&face=f2'
            if detect_emotion_val != 2:
                url = url[:-1] + str(detect_emotion_val)
            # Get the image from the URL
            url = requests.get(url)
            url_str=url.url
            if kittified:
                url_str = kittifying(url_str, ign)
            if hair_color_change != 2 :
                if hair_color_change is not None:
                    url_str = hair_color_changing(url_str,hair_color_change)
            return url_str






        def parse_input_string(input_str):
            if isinstance(input_str, dict):
                return input_str

            variables = {'ign': None, 'mount': 0, 'animated': 0, 'hair_color_change': None, 'detect_emotion': 0, 'kittify': False}
            color_dict = {
                'BLACK': 0,
                'RED': 1,
                'ORANGE': 2,
                'WHITE': 2,
                'BLONDE': 3,
                'GREEN': 4,
                'BLUE': 5,
                'PURPLE': 6,
                'BROWN': 7
            }

            def color_detect(var):
                if var.isdigit() and int(var) in color_dict.values():
                    return int(var)
                elif var.upper() in color_dict:
                    return color_dict[var.upper()]
                else:
                    return None

            split_input = input_str.strip().split()
            variables['ign'] = split_input[0]

            for var in split_input[1:]:
                color = color_detect(var)
                if var in ('mount', 'Mount'):
                    variables['mount'] = 1
                elif var in ('animated', 'Animated'):
                    variables['animated'] = 1
                elif var in ('kittify', 'Kittify'):
                    variables['kittify'] = True
                elif color is not None:
                    variables['hair_color_change'] = color
                elif detect_emotion(var):
                    variables['detect_emotion'] = detect_emotion(var)

            return variables

        variables = get_avatar_image(parse_input_string(input_str))

        embed = discord.Embed(title="Maple Image", color=0xff0000)
        embed.set_image(url=variables)
        await context.send(embed=embed)





async def setup(bot):
    await bot.add_cog(General(bot))