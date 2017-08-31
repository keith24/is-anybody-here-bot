#!./env/bin/python
# main.py


import praw, pdb, re, os

# Setup reddit and subs
reddit = praw.Reddit('DEFAULT')
rall = reddit.subreddit('all')
sub = reddit.subreddit('IsAnybodyHere')

# Search latest comments in r/all
for comment in rall.stream.comments():
	
	# Match with regex
	match = re.search("(does|has|is)(n't)? (any one|anyone|someone|anybody) (here)? (.*?)\?", comment.body, re.IGNORECASE)
	if match:
		
		# Extract a description of the needed person
		needed = match.group(3) + ' who ' + match.group(1) + ' ' + match.group(5)
		print(match.group(),'\n',needed.title(),'\n')
		
		# Reply to the comment
		#try:
		#	response = comment.reply( "I'll look for someone who", ' '.join(match.group(1,5)).lower() )
		#except: 
		#	print("Failed to reply to comment"+comment.id); raise
		#else:
		#	print("Replied to comment "+comment.id+":",response.permalink())
		
		# Post to our sub
		try:
			post = sub.submit(needed.title(), url='https://www.reddit.com'+comment.permalink(), resubmit=False)
		except:
			print("Failed to post to our sub"); raise
		else:
			print("Posted to sub:",post.shortlink)
