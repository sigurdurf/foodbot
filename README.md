# Food bot.
Foodbot is a simple way to add the Málið menu to your discord server  
Contact me via email  at (sigurdurf21 at ru.is) if you want to use the bot but don't want to host it yourself

Foodbot is currently being enjoyed by 2 discord servers :)  
Docker support coming soon.
## Available commands 
!l or !lunch: Todays dishes at Málið  
!lw {restaurant}: Gets lunch menu from specified restaurant  
!ar: Show available restaurants  
!help: Displays the help menu  
  
## API
The food bot api is a simple REST api written in Python.
#### Installing dependancies
To install the dependancies for it by pip installing all modules listed in the src/api/app/requirements.txt file  
(I assume you are running in a virtual environment :) )
```
$ pip install -r src/api/app/requirements.txt 
```
#### Running the webserver
(Inside the src/api folder)
```
$ uvicorn app.main:app --reload --port 8111
```
## Discord Bot
The food bot discord bot is written in Go
#### installing the dependancies
This assumes you have Go installed on your system.
```
$ go get github.com/bwmarrin/discordgo
```
#### Running the bot
(Inside the src/bot folder)
```
go build
./bot -t <DISCORD_TOKEN_FOR_YOUR_BOT>
```
