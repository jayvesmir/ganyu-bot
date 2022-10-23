# Ganyu bot
Ganyu is cool. Live, Laugh, Love, Ganyu.

- Extremely early in development!!! (So early in fact, that there aren't any other functions than ping.)
- The constant TEST_SERVER is currently being used as the bot is still in development and I need it to register slash commands quickly. (If you're going to self host Ganyu, you definitly want that too.) I might make a separate branch where this isn't a thing I still have to figure out how to work with github efficiently. (O_O;)

## How to self-host Ganyu (Windows only) (＾◡＾)

1. Run this command in the ganyu-bot directory to create a virtual environment for the bot to run in.  
`$ python -m venv venv`

2. Activate the virtual environment with:
`$ venv/scripts/activate.ps1`

3. Then, install the required libraries.
`$ pip install -r requirements.txt`

4. If that returns an error, try:
`$ python -m pip install -r requirements`

5. Create a config.json file in the root of this repo, this file contains the token to the account you want to host the bot on. commands_guild refers to the guild the bot is going to register it's commands to, as registering them globally usually takes ~1-2 hours. The file's content must match this format:
```json
{
  "token": "<account_token>",
  "commands_guild": "<your_server_id>"
}
```

6. Start the bot. The initial output should closely match this:
```
$ python src/Ayanami.py

<date n time> INFO     discord.client logging in using static token
<date n time> INFO     discord.gateway Shard ID None has connected to Gateway. (<session_id>)
<date n time> INFO     discord.Ganyu Ganyu is online as <bot_account_name>.
```
