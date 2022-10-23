# Ganyu bot - Extremely early in development!!! (So early in fact, that there aren't any other functions than ping.)
Ganyu is cool. Live, Laugh, Love, Ganyu.

## How to self-host Ganyu (＾◡＾)

1. Run this command in the ganyu-bot directory to create a virtual environment for the bot to run in.  
`$ python -m venv venv`

2. Activate the virtual environment with:
`$ venv/scripts/activate.ps1`

3. Then, install the required libraries.
`$ pip install -r requirements.txt`

4. If that returns an error, try:
`$ python -m pip install -r requirements`

5. Create a config.json file in the root of this repo, this file contains the token to the account you want to host the bot on. The file's content must match this format:
```json
{
  "token": "<account_token>"
}
```

6. Start the bot. The initial output should closely match this:
```
$ python src/Ayanami.py

<date n time> INFO     discord.client logging in using static token
<date n time> INFO     discord.gateway Shard ID None has connected to Gateway. (<session_id>)
<date n time> INFO     discord.Ganyu Ganyu is online as <bot_account_name>.
```
