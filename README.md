# thehttpbot

An interactions-over-HTTP discord bot using discord.py.

## Outline

[discord.py][1] is mainly focused around discord's real-time gateway and
doesn't support receiving interactions via HTTP. However, using the discord.py
client's [`login()`][2] method, the bot can authenticate itself without
establishing a gateway connection, allowing discord.py to send API requests.
discord.py also has internal methods that allow manually dispatching interaction
events within the library from JSON payloads. As such, the bot could
simultaneously host a webserver using other libraries, in this case [uvicorn][3]
and [FastAPI][4], and then relay those interactions to discord.py.

## Dependencies

This bot requires Python 3.11+ to run. In addition, dependencies must be
configured using [Poetry][5].

## Usage

1. Download the repository and navigate to the project root.

2. Install the dependencies via Poetry (if you have not set up a
   [virtual environment][6], Poetry will create one for you):

```sh
poetry install
```

3. Copy the `example.env` file as `.env` and fill in the required credentials.

4. Start the bot and webserver:

```sh
poetry run uvicorn thehttpbot --reload --port 5000
```

5. Use the invite link provided in the terminal to invite your bot.

## License

This project uses the [MIT](LICENSE) license.

[1]: https://discordpy.readthedocs.io/en/stable/
[2]: https://discordpy.readthedocs.io/en/stable/api.html#discord.Client.login
[3]: https://www.uvicorn.org/
[4]: https://fastapi.tiangolo.com/
[5]: https://python-poetry.org/
[6]: https://docs.python.org/3/tutorial/venv.html
