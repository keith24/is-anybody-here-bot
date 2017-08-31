# Is Anybody Here Bot
###### v0.1.0
[Keith Irwin](https://keithirwin.us/)


*Is Anybody Here Bot* is a bot that finds experts for you, operating as [u/IsAnybodyHereBot](https://www.reddit.com/user/IsAnybodyHereBot).  It's triggered whenever someone posts "Is anyone here a doctor?" or "Has anyone here been to Fiji?" or something like that. The bot will post a link to that comment in [r/IsAnybodyHere](https://www.reddit.com/r/IsAnybodyHere/), and if you meet the requirements, you can go to the original comment and add your two cents!  

# Usage

I recommend setting up an environment with `virutalenv`: 

```sh
virtualenv -p python3 env
source env/bin/activate
pip install -r requirements.txt
```

To run the bot, simply run main.py with python3, setting environment variables for praw: 

```sh
praw_client_id=XXXXXXXXXXXXXX praw_client_secret=XXXXXXXXXXXXXXXXXXXXXXXXXXX praw_password=XXXXXXXX ./env/bin/python3 main.py
```
