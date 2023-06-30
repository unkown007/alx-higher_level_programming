#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message You got me!, in the body of the response
curl -sd "You+got+me!" -X PUT "0.0.0.0:5000/catch_me" 
