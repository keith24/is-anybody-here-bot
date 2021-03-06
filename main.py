#!./env/bin/python
# main.py

'''
Is Anybody Here Bot

VERSION: 0.1.0
DESCRIPTION: A reddit bot that helps find people in the know
AUTHOR: Keith Irwin <https://keithirwin.us/>
SOURCE: https://github.com/keith24/is-anybody-here-bot
'''


import praw, pdb, re, os

# Setup reddit and subs
reddit = praw.Reddit('DEFAULT')
rall = reddit.subreddit('all')
sub = reddit.subreddit('IsAnybodyHere')

# Blacklist (by mod request)
blacklist = {'test','neoliberal'}

print("Started IsAnybodyHereBot...")

# Search latest comments in r/all
for comment in rall.stream.comments():
	
	# Check for blacklist
	if comment.subreddit.display_name.lower() not in blacklist:
		
		# Match with regex
		match = re.search("(does|has|is)(n't)? (any one|anyone|someone|anybody) (here)? (.*?)\?", comment.body, re.IGNORECASE)
		if match:
			
			# Extract a description of the needed person
			needed = match.group(3) + ' who ' + match.group(1) + ' ' + match.group(5)
			print(match.group(),'\n',needed.title(),'\n')
			
			# Post to our sub
			try:
				post = sub.submit(needed.title(), url='https://www.reddit.com'+comment.permalink(), resubmit=False)
			except:
				print("Failed to post",comment.id,"to our sub")
			else:
				print("Posted to sub:",post.shortlink)
