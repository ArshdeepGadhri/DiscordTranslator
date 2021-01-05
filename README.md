# DiscordTranslator

DiscordTranslator is a Discord selfbot to translate messages for you!

#### SelfBots are against Discord's TOS as people tend to use them for malicious purposes, so use this at your own risk

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the needed modules.

```bash
pip install -r requirements.txt
```

## Installation

```coffee
#1 Open config.py in any text editor / IDE
#2 Replace "YOUR_TOKEN_HERE" with your discord token, do not share this token
#3 Change the prefix if you want to

# Run the script
python3 bot.py
```

## Help
How do I get my Discord Token? [Discord Tokens](https://github.com/Tyrrrz/DiscordChatExporter/wiki/Obtaining-Token-and-Channel-IDs)

How can I host this bot?
###### You can follow this [tutorial](https://repl.it/talk/learn/Hosting-discordpy-bots-with-replit/11008) and learn how to host a discord.py bot on repl.it for completely free! Fork the repo, sign into repl.it with your github account, open up the repo and set up a webserver as shown in the tutorial. Doing this allows your bot to be online 24/7.

## Usage
```
<Prefix>tr <from_language> <to_language> [Message]
```

![Like So](https://i.ibb.co/pb9D4k6/image.png)


This translates 'hello there' from en (English) to ja (Japanese). 
###### You can replace en with 'auto' to automatically detect the language. 
###### You can replace ja with 'auto' to automatically translate to English.
###### You can replace both en and ja with 'auto' to automatically detect the language and translate to English.


### License [MIT](https://choosealicense.com/licenses/mit/)