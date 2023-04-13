# Food bot.
Foodbot is a simple way to add the Málið menu to your discord server  
Contact me via email  at (sigurdurf21 at ru.is) if you want to use the bot but don't want to host it yourself

Foodbot is currently being enjoyed by 2 discord servers :)  
## Running with Docker compose
Add the config file to the `src/bot` folder and update the configuration as per the instructions below.  
run the docker compose file
```
docker-compose up -d --build
```
The bot should be running with access to the api through a local docker network.
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
Edit and/or create a file called `config.json`  
The contents need to be 
```
{
    token: "Your discord api key",
    server: "api server address"
}
```
Note, the server address when running the bot in docker compose will be api,  
as defined in the docker-compose file. Othervise, just your api url.
```
go build
./bot
```
