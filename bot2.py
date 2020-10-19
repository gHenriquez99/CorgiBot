import tweepy
import config 
import time 
import requests 
import praw 

def loginToReddit():
    try:
        print("-----------------------------------------------")
        print('*** Logging into Reddit Account ***')
        reddit = praw.Reddit(
            client_id=config.client_id,
            client_secret=config.client_secret,
            user_agent="EmmaBot v1.0",
            username=config.username,
            password=config.password
        )
        print('* Login successful')
        print('-----------------------------------------------')
        return reddit
    except:
        print('*** Login failed ***')
        print('-----------------------------------------------')

def getImage(url):
    try:
        print("-----------------------------------------------")
        print('*** Downloading your image from Reddit ***')
        req = requests.get(url)
        with open('img.jpg', 'wb') as image:
            image.write(req.content)
            image.close()
            print('*** Your image has been downloaded and saved! ***')
    except:
        print('*** Unable to download image ***')
        print("-----------------------------------------------")

def postTweet(content):
    try:
        print("-----------------------------------------------")
        print('*** Logging into twitter ***')
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.key,config.secret)

        api=tweepy.API(auth)
        print('*** Twitter login successful ***')

        tweet = content 
        image_path = 'img.jpg'

        print('*** Posting on Twitter ***')
        api.update_with_media(image_path, tweet)
        print("*** Successfully posted ***")
        print("-----------------------------------------------")
    except: 
        print('Something went wrong while trying to post tweet')
        print("-----------------------------------------------")

def main():
    reddit = loginToReddit()
    for submission in reddit.subreddit("corgi").hot(limit=10):
        if submission.stickied == False:
            print("-----------------------------------------------")
            print("*** Getting seubmission from Reddit ***")
            content = submission.title
            content = '"' + content + '"' + ' @TheNamedEmma'
            url = submission.url  
            if 'jpg' in url or 'png' in url:
                getImage(url)
                postTweet(content)
                print('Tweet has been posted!')
                time.sleep(20)
                break
            else: 
                print('*** No image found ***')

main()

        
