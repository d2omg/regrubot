# regrubot
## Convenient access to managing virtual servers via telegram bot.

If you are a user of cloud servers from **reg.ru**, substitute your data in the ```conf.py``` file:

```SERVER_ID = '*******'``` - Your server id. You can take REG.RU> Cloud servers> ID (it will be in the line after the name of your server)

```TOKEN = '*******'``` - Token received in REG.RU tab>Cloud servers>Settings

```BOT_TOKEN = "*******"``` - Token of your bot. Get from @botfather>/newbot

Install python if you don't already have it! And start the bot with the command: ```python bot.py``` or ```python3 bot.py```

I used the PYTelegramBotApi capabilities in this project, as well as the official REG.RU documentation, which is described [here](https://developers.cloudvps.reg.ru/).
