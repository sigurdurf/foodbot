# Use an official Golang runtime as a parent image
FROM golang:1.17.6-alpine3.15

# Set the working directory to /app
WORKDIR /app

# Copy the source code into the container at /app
COPY main.go .
COPY config.json .
COPY go.mod .
RUN go get github.com/bwmarrin/discordgo

# Build the Go binary
RUN go build -o bot

# Run the command to start the application
CMD ["./bot"]
