package main

import (
	"flag"
	"fmt"
	"os"
	"log"
	"os/signal"
	"syscall"
	"net/http"
	"io/ioutil"
	"github.com/bwmarrin/discordgo"
	"encoding/json"
	"time"
	"strings"
)
type ResponseWeek struct {
	Days []ResponseDay `json:"menu"`
}

type ResponseDay struct {
	Day string `json:"day"`
	Main string `json:"main"`
	Vegan string `json:"vegan"`
	Soup string `json:"soup"`
	Salat string `json:"salat"`

}


// Variables used for command line parameters
var (
	Token string
)

func init() {

	flag.StringVar(&Token, "t", "", "Bot Token")
	flag.Parse()
}

func main() {

	// Create a new Discord session using the provided bot token.
	dg, err := discordgo.New("Bot " + Token)
	if err != nil {
		fmt.Println("error creating Discord session,", err)
		return
	}

	// Register the messageCreate func as a callback for MessageCreate events.
	dg.AddHandler(messageCreate)

	// In this example, we only care about receiving message events.
	dg.Identify.Intents = discordgo.IntentsGuildMessages

	// Open a websocket connection to Discord and begin listening.
	err = dg.Open()
	if err != nil {
		fmt.Println("error opening connection,", err)
		return
	}

	// Wait here until CTRL-C or other term signal is received.
	fmt.Println("Bot is now running.  Press CTRL-C to exit.")
	sc := make(chan os.Signal, 1)
	signal.Notify(sc, syscall.SIGINT, syscall.SIGTERM, os.Interrupt, os.Kill)
	<-sc

	// Cleanly close down the Discord session.
	dg.Close()
}

// This function will be called (due to AddHandler above) every time a new
// message is created on any channel that the authenticated bot has access to.
func messageCreate(s *discordgo.Session, m *discordgo.MessageCreate) {

	// Ignore all messages created by the bot itself
	// This isn't required in this specific example but it's a good practice.
	if m.Author.ID == s.State.User.ID {
		return
	}

	if m.Content == "!help" {
		res := "```\nAvailable commands\n!l or !lunch: Todays dishes at Málið\n!lw {restaurant}: Gets lunch menu from specified restaurant\n!ar: Show available restaurants\n!help: Displays this menu```"
		s.ChannelMessageSend(m.ChannelID, res)
	}
	if m.Content == "!ar" {
		res := "```Málið í HR:\n\tCode: malid\n\tWeekly menu command: !lw {restaurant}\n\tTodays dishes: !l or !lunch```"
		s.ChannelMessageSend(m.ChannelID, res)
	}
	if m.Content == "!lunch" || m.Content == "!l" {

		weekday := time.Now().Weekday()
		if weekday == 0|| weekday == 7 {
			s.ChannelMessageSend(m.ChannelID, "```Enginn matur í dag```")
			return
		}
		url := "http://127.0.0.1:8111/lunch/malid?q="+strings.ToLower(weekday.String())
		api_res, err := http.Get(url)
		if err != nil{
			fmt.Println("error fetching lunch data,", err)
			res := fmt.Sprintf("```Error fetching lunch data```")
			s.ChannelMessageSend(m.ChannelID, res)
			return
		}
		responseData, err := ioutil.ReadAll(api_res.Body)
		if err != nil {
			log.Fatal(err)
			s.ChannelMessageSend(m.ChannelID, "```Error unpacking lunch data```")
			return
		}
		var responseObject ResponseDay
		json.Unmarshal(responseData, &responseObject)
		
		
		res := fmt.Sprintf("```%s: \nAðalréttur: %s\nVeganréttur: %s\n```", responseObject.Day, responseObject.Main, responseObject.Vegan)
		s.ChannelMessageSend(m.ChannelID, res)
	}
    if m.Content == "!badday"{
        s.ChannelMessageSend(m.ChannelID,"Everything’s gonna be okay. You did not come this far to give up. I believe in you.")
    }
	if m.Content == "!lw malid" {
		url := "http://127.0.0.1:8111/lunch/malid"
		api_res, err := http.Get(url)
		if err != nil{
			fmt.Println("error fetching lunch data,", err)
			res := fmt.Sprintf("```Error fetching lunch data```")
			s.ChannelMessageSend(m.ChannelID, res)
			return
		}
		responseData, err := ioutil.ReadAll(api_res.Body)
		if err != nil {
			log.Fatal(err)
			s.ChannelMessageSend(m.ChannelID, "```Error unpacking lunch data```")
			return
		}
		var responseObject ResponseWeek
		json.Unmarshal(responseData, &responseObject)
		var codeBlockStart = "```"
		var middle = ""
		for i := 0; i < len(responseObject.Days); i++ {
			middle = fmt.Sprintf("%s\n\n %s: \nAðalréttur: %s\nVeganréttur: %s\n", middle, responseObject.Days[i].Day, responseObject.Days[i].Main, responseObject.Days[i].Vegan)
		}
		var codeBlockEnd = "```"
		res := codeBlockStart + middle + codeBlockEnd
		s.ChannelMessageSend(m.ChannelID, res)
	}

}
