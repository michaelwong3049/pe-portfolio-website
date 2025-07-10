#!/bin/bash

# Start the Flask server in the background
flask run &

# Save its process ID to kill it later
FLASK_PID=$!

# Give the server time to start
sleep 2

# Send a POST request with curl
curl --request POST http://localhost:5000/api/timeline_post --data "name=Michael&email=michaelwong3049@gmail.com&content=Just Added DB to my portfolio site!"

# Stop the Flask server
kill $FLASK_PID

