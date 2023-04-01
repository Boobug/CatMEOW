# Python Discord Bot Template

<p align="center">
  <a href="https://discord.gg/SPMGM3Z"><img src="https://img.shields.io/discord/426594227271499785?logo=discord"></a>
  <a href="https://github.com/Boobug/CatMEOW/releases"><img src="https://img.shields.io/github/v/release/Boobug/CatMEOW"></a>
  <a href="https://github.com/Boobug/CatMEOW/commits/main"><img src="https://img.shields.io/github/last-commit/Boobug/CatMEOW"></a>
  <a href="https://github.com/Boobug/CatMEOW/blob/main/LICENSE.md"><img src="https://img.shields.io/github/license/Boobug/CatMEOW"></a>
  <a href="https://github.com/Boobug/CatMEOW"><img src="https://img.shields.io/github/languages/code-size/Boobug/CatMEOW"></a>
  <a href="https://conventionalcommits.org/en/v1.0.0/"><img src="https://img.shields.io/badge/Conventional%20Commits-1.0.0-%23FE5196?logo=conventionalcommits&logoColor=white"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>



See [the license file](https://github.com/Boobug/CatMEOW/blob/master/LICENSE.md) for source 


## Support

This will be ready when a release of the bot is available


All the updates of the template are available [here](UPDATES.md).

## Disclaimer

Slash commands can take some time to get registered globally, so if you want to test a command you should use
the `@app_commands.guilds()` decorator so that it gets registered instantly. Example:

```py
@commands.hybrid_command(
  name="command",
  description="Command description",
)
@app_commands.guilds(discord.Object(id=GUILD_ID)) # Place your guild ID here
```

When using the template you confirm that you have read the [license](LICENSE.md) and comprehend that I can take down
your repository if you do not meet these requirements.

Please do not open issues or pull requests about things that are written in the [TODO file](TODO.md), they are **already** under work for a future version of the template.

## How to download it


## How to set up

To set up the bot I made it as simple as possible. I now created a [config.json](config.json) file where you can put the
needed things to edit.

Here is an explanation of what everything is:

| Variable                  | What it is                                                            |
| ------------------------- | ----------------------------------------------------------------------|
| YOUR_BOT_PREFIX_HERE      | The prefix you want to use for normal commands                        |
| YOUR_BOT_TOKEN_HERE       | The token of your bot                                                 |
| YOUR_BOT_PERMISSIONS_HERE | The permissions integer your bot needs when it gets invited           |
| YOUR_APPLICATION_ID_HERE  | The application ID of your bot                                        |
| OWNERS                    | The user ID of all the bot owners                                     |


## How to start

To start the bot you simply need to launch, either your terminal (Linux, Mac & Windows), or your Command Prompt (
Windows)
.

Before running the bot you will need to install all the requirements with this command:

```
python -m pip install -r requirements.txt
```

After that you can start it with

```
python bot.py
```

> **Note** You may need to replace `python` with `py`, `python3`, `python3.11`, etc. depending on what Python versions you have installed on the machine.

## Issues or Questions

If you have any issues or questions of how to code a specific command, you can:




Me or other people will take their time to answer and help you.

## Versioning

We use [SemVer](http://semver.org) for versioning. For the versions available, see


## Built With

* [Python 3.9.12](https://www.python.org/)

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details
