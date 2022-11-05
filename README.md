# Ganyu bot
Ganyu is cool. Live, Laugh, Love, Ganyu.

- Extremely early in development!!! (So early in fact, that there aren't any other functions than ping.)

## How to self-host Ganyu (Windows only) (＾◡＾)

1. Run this command in the ganyu-bot directory to create a virtual environment for the bot to run in.  
`$ python -m venv venv`

2. Activate the virtual environment with:
`$ venv/scripts/activate.ps1`

3. Then, install the required libraries.
`$ pip install -r requirements.txt`

4. If that returns an error, try:
`$ python -m pip install -r requirements.txt`

5. Create a config.json file in the root of this repo, this file contains the token to the account you want to host the bot on. prefix refers to the prefix you want to use for prefix commands. Please keep in mind that slash commands may take up to 2 hours to register, prefix commands will be functional during this time. The file's content must match this format:
```json
{
  "token": "<account_token>",
  "prefix": "<prefix>"
}
```

6. Start the bot. The initial output should closely match this:
```
$ python Ayanami.py

<date n time> INFO     discord.client logging in using static token
<date n time> INFO     discord.gateway Shard ID None has connected to Gateway. (<session_id>)
<date n time> INFO     discord.Ganyu Ganyu is online as <bot_account_name>.
```
