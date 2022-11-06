<div align="center" style="font-size:76px;">
  <img src="https://user-images.githubusercontent.com/67397386/200123150-25095e26-d4a5-4829-a382-3619d093bdba.png" width="300" height="300">
  <br>
  <h1 align="center">Ganyu</h1>
</div>

<details>
<summary>Table of Contents</summary>

- [About](#about)
- [How to Self-Host](#how-to-self-host-ganyu-windows-only-)
- [Contributing](#contributing)
- [License](#license)

</details>

## About
- Extremely early in development!!!
- yeah ( ‾́ ◡ ‾́ )	

## How to self-host Ganyu (Windows only) (＾◡＾)

- You can skip the first 4 steps by running this:  `$ ./prepare.ps1`

1. Run this command in the ganyu-bot directory to create a virtual environment for the bot to run in.  
`$ python -m venv venv`

2. Activate the virtual environment with:
`$ venv/scripts/activate.ps1`

3. Then, install the required libraries.
`$ pip install -r requirements.txt`

4. If that returns an error, try:
`$ python -m pip install -r requirements.txt`

5. Create a config.json file in the root of this repo, this file contains the token to the account you want to host the bot on. Please keep in mind that slash commands may take up to 2 hours to register. (I might implement prefix commands later on.) The file's content must match this format:
```json
{
  "token": "<account_token>"
}
```

6. Start the bot. The initial output should closely match this:
```
$ python Ayanami.py

<date n time> INFO     discord.client logging in using static token
<date n time> INFO     discord.gateway Shard ID None has connected to Gateway. (<session_id>)
<date n time> INFO     discord.Ganyu Ganyu is online as <bot_account_name>.
```

## Contributing

Very WIP, All contributions are welcome!

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute it as you like.

See [LICENSE](LICENSE) for more information.

# Ganyu
Ganyu is cool. Live, Laugh, Love, Ganyu.
