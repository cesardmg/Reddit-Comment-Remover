import praw
import datetime
import time
import configparser

# Read credentials from the config file
config = configparser.ConfigParser()
config.read('config.ini')

# Replace these values with your own
client_id = config['reddit']['client_id']
client_secret = config['reddit']['client_secret']
user_agent = config['reddit']['user_agent']
username = config['reddit']['username']
password = config['reddit']['password']


# Number of posts to delete in each run
num_posts_to_delete = None  # Set to None to fetch all posts
delay = 2  # Delay in seconds between deletions to avoid rate limits

# Initialize the Reddit instance
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent,
                     username=username,
                     password=password)

# Fetch the user's posts
user = reddit.redditor(username)


# Collect and delete posts
posts_to_delete = list(user.submissions.new(limit=num_posts_to_delete))

for post in posts_to_delete:
    print(f"Deleting post from {datetime.datetime.fromtimestamp(post.created_utc)}: {post.title[:30]}...")
    post.delete()
    time.sleep(delay)  # Delay to avoid rate limits

print(f"Deletion process completed for {len(posts_to_delete)} posts.")
