import requests
import yaml
import json
import praw
from Scripts.Configuration import ConfigurationClass

class RedditData:
    def __init__(self):
        self.config = ConfigurationClass(key = "REDDIT").loadConfiguration()

    def auth(self):
        config = self.config
        client_id= config['REDDIT_CLIENT_ID']
        client_secret= config['REDDIT_CLIENT_SECRET']
        username = config['REDDIT_USERNAME']
        password = config['REDDIT_PASSWORD']
        user_agent = config['REDDIT_USER_AGENT']
        reddit = praw.Reddit(client_id=client_id,
                             client_secret= client_secret,
                             username= username,
                             password= password,
                             user_agent= user_agent)
        reddit.read_only = True    
        return reddit
    
    def make_request(self, sub, limit_posts, filterby):
        reddit = self.auth()
        subreddit = reddit.subreddit(sub)
        if filterby.lower() == 'top':
            posts = subreddit.top(limit=int(limit_posts))
        elif filterby.lower() == 'hot':
            posts = subreddit.hot(limit=int(limit_posts))
        elif filterby.lower() == 'new':
            posts = subreddit.new(limit=int(limit_posts))
        else:
            posts = subreddit.hot(limit=int(limit_posts))

        body = ''
        for post in posts:
            post_body = ''
            post_body += f'<div><strong>{post.author}</strong></div>\n'
            if post.is_video:
                post_body += f'<p><h3>{post.title} [VIDEO]</h3></p>\n'
            else:
                post_body += f'<p><h3>{post.title}</h3></p>\n'
        
            if post.selftext:
                post_body += f'<p>{post.selftext}</p>\n'

            if hasattr(post, 'preview') and 'images' in post.preview:
                all_images = [x['source'] for x in post.preview['images']]
                for image in all_images:
                    post_body += f'<img src="{image["url"]}" alt="Post Image">\n'

            post_body += f'<p>Upvotes: {post.ups} Comments: {post.num_comments}</p>'
        
            if post.is_video:
                post_body += f"<br><a class='watch-video-btn' href='https://reddit.com{post.permalink}'> Watch Video</a>"
            else:
                post_body += f"<br><a class='watch-video-btn' href='https://reddit.com{post.permalink}'> See on Reddit</a>"
        
            post_body += '</div>\n'
            post_body += "<hr>"
            body += post_body

        body += "<p>Wishing you a wonderful day!</p>"
        return body


